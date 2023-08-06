"""Contains the implementation of a proper orthogonal decomposition module for trajectory modules"""

__all__ = ["PODTrajectoryModule"]

import tensorflow as tf
import numpy as np

from cmrsim.trajectory._taylor import TaylorTrajectoryN


# pylint: disable=abstract-method
class PODTrajectoryModule(TaylorTrajectoryN):
    # pylint: disable=anomalous-backslash-in-string
    """Captures the trajectories of an arbitrary set of particles  (e.g. Nodes of structured meshes)
    by computing the proper orthogonal decomposition (POD) from a set of snapshots.

    .. math::

      u(t) = \Sigma_j^{N_{modes}} \phi_j w_j(t),

    where :math:`\phi_j` are the computed basis functions (modes) $w_j(t)$ are the corresponding
    mode-weights as function of time. To allow the motion state to be reconstructed from the
    low-rank representation at arbitrary time-points within the interval of specified snapshots,
    the mode-weights are represented as Taylor-series.

    The use of this module is not limited to represent trajectories only is generalized to any set
    vectors, e.g. mesh node position combined with a local basis resulting in input-shapes
    (per snapshot) of (#particles, 3+3+3+3).

    .. dropdown:: Example Usage:

        .. code::

            data, t = ...  # get snapshots of states and corresponding time-points
            # Shapes: data.shape == (#particles, #snapshots, #channels)
            #         t.shape == (#steps, )

            pod_module = cmrsim.trajectory.PODTrajectoryModule(data, t, n_modes=5, poly_oder=8)

            new_time_grid = np.linspace(t[0].m, t[-1].m, 100).astype(np.float32)

            reconstructed_states, _ = pod_module(new_time_grid)
            ## reconstructed_states.shape == (#particles, 100, #channels)


    :param time_grid: (#time_steps)
    :param data: (#particles, #time_steps, #channels)
    :param n_modes: Number of modes used for reduce-order representation
    :param poly_order: Order of the Taylor-series used to fit the mode-weights
    """
    #: Number of modes used for reduce-order representation
    n_modes: tf.Variable
    #: Computed basis-functions (modes) :math:`\phi_j` used to represent the input data in
    #: a reduced order. Shape (#particles * #channels, #modes)
    basis_function: tf.Variable

    _nchannels: tf.Variable

    def __init__(self, time_grid: np.ndarray, data: np.ndarray, n_modes: int,
                 poly_order: int):

        self.n_modes = tf.Variable(n_modes, shape=(), dtype=tf.int32)
        self._nchannels = tf.Variable(data.shape[2], shape=(), dtype=tf.int32)
        phi, mode_weights = self.calculate_pod(time_grid, data, n_modes, remove_mean=False)
        self.basis_function = tf.Variable(phi, shape=(None, n_modes), dtype=tf.float32)

        super().__init__(order=poly_order, time_grid=time_grid,
                         particle_trajectories=mode_weights.T.reshape(n_modes, -1, 1),
                         batch_size=None, fit_on_init=True)

    @staticmethod
    def calculate_pod(time_grid: np.ndarray, data: np.ndarray, n_modes: int,
                      remove_mean: bool = False) -> (np.ndarray, np.ndarray):
        """Computes the proper orthogonal decomposition of data snapshots at points defined in
        `time_grid`. Returns only the `n_modes` number of most significant modes

        :param time_grid: (#time_steps) time-points corresponding to snapshots
        :param data: (#particles, #time_steps, #channels) snapshots of data
        :param n_modes: number of most significant modes to return
        :param remove_mean: if true removes the temporal mean of all snapshots before computing POD
        :return: - POD base modes, shape: (#particles * #channels, n\_modes),
                 - scaling of modes per time-step (#time_steps, n\_modes)
        """
        n_tsteps = time_grid.shape[0]
        flat_sv = data.transpose(0, 2, 1).reshape(-1, n_tsteps)

        if remove_mean:
            sv_temporal_mean = np.mean(flat_sv, axis=1, keepdims=True)
            flat_sv -= sv_temporal_mean

        # compute square matrix C of shape (t, P) @ (P, t) -> (t, t)
        covariance_matrix = np.dot(flat_sv.T, flat_sv)

        # shapes: (t, ), (t, t)
        eigen_values, eigen_vectors = np.linalg.eigh(covariance_matrix)

        # Sort eigenvalues in descending order and take N largest -> shapes: (N,), (t, N)
        descending_sort_idx = np.argsort(eigen_values)[::-1][0:n_modes]
        eigen_values = eigen_values[descending_sort_idx]
        eigen_vectors = eigen_vectors[:, descending_sort_idx]

        # Scale eigen-vectors with inverse sqrt of eigen-value:
        # modes_cut = eigen_vectors.dot(np.diag(np.power(eigen_values, -0.5)))
        modes_cut = eigen_vectors / np.sqrt(eigen_values).reshape(1, -1)

        # (P*ch, t) @ (t, N) -> (P*ch, N)
        phi = np.dot(flat_sv, modes_cut)

        weights = np.einsum('pn, pt -> nt', flat_sv, phi)
        return phi, weights

    def __call__(self, timing: tf.Tensor, **kwargs) -> (tf.Tensor, dict):
        """Reconstructs the data state at given times t, by evaluating the taylor series
        of mode-weights and computing the weighted sum.

        :param timing: (#timesteps) in milliseconds
        :return: (#particles, #timesteps, self._channels), {}
        """
        return self._evaluate_trajectory(timing), {}

    @tf.function
    def increment_particles(self, r: tf.Tensor, dt: tf.Tensor, **kwargs) -> (tf.Tensor, dict):
        """Evaluates the particle position for the time self.current_time_ms + dt and adds the
        delta t to the current_time_ms variable

        :param r: unused parameter (to adhere to calling signature of trajectory modules)
        :param dt: temporal step lengths
        :param kwargs: unused parameter (to adhere to calling signature of trajectory modules)
        :return: (#batch, self._channels), {}
        """
        self.current_time_ms.assign_add(dt)
        new_pos = self._evaluate_trajectory(tf.reshape(self.current_time_ms, [1, ]))
        return new_pos[:, 0], {}

    @tf.function
    def _evaluate_trajectory(self, t: tf.Tensor) -> tf.Tensor:
        """Reconstructs the data state at given times t, by evaluating the taylor series
        of mode-weights and computing the weighted sum.

        :param t: (#steps) time-points to reconstruct at
        :return: data-states (#particles, #steps, #channels)
        """
        # Evaluate mode weights from taylor-expansion of super class shape: (t, N)
        mode_weights = tf.transpose(super()._evaluate_trajectory(t)[:, :, 0], [1, 0])
        # Compute weighted sum of basis functions / modes to reconstruct data
        values_at_t = tf.einsum('pn, tn -> pt', self.basis_function, mode_weights)
        # Reshape according to input shapes (#particles, #steps, #channels)
        _shape = tf.stack([-1, self._nchannels, tf.shape(mode_weights)[0]], axis=0)
        return tf.transpose(tf.reshape(values_at_t, _shape), [0, 2, 1])
