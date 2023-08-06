"""Contains the implementation of a module that fits a taylor expansion to particle trajectories"""
__all__ = ["TaylorTrajectoryN"]

import numpy as np
import tensorflow as tf

from cmrsim.trajectory._base import BaseTrajectoryModule


# pylint: disable=abstract-method
class TaylorTrajectoryN(BaseTrajectoryModule):
    """Fits a taylor Polynomial of specified order to the given 3D particle trajectories and stores
    the resulting coefficients per particle. When called, evaluates the Taylor-expansion at given
    timing in a tf.function compatible definition.

    Incrementing particle positions is done by keeping track of the current timing. Batching the
    particles for all evaluations is done by setting the attributes self.batch_size and
    self.current_batch_idx. This results in the indexing:
    [self.batch_size*self.current_batch_idx : self.batch_size*self.current_batch_idx+1]

    .. dropdown:: Example Usage

        .. code-block:: python
            :caption: Instantiation

            ref_timing = ... # shape (T, )
            ref_trajectory = ... # shape (N, T, dims)
            module = TaylorTrajectoryN(order=3, time_grid=ref_timing,
                                      particle_trajectories=ref_trajectory)

    :param order: Order of the fitted TaylorPolynomial
    :param time_grid: (#timesteps, )
    :param particle_trajectories: (#particles, #timesteps, 3)
    :param batch_size: used for evaluating the particle trajectories in batches
    :param fit_on_init: If True, the Polynomial is fitted on instantiation of the module.
    """
    #: Keeps track of the current timing when increment_particles is called.
    current_time_ms: tf.Variable
    #: Allows to only evaluate the position for a batch of stored particle trajectories
    current_batch_idx: tf.Variable
    #: Together with self.current_batch_size determines the subset of particle trajectories that
    #: is evaluated on call and increment_particles
    batch_size: tf.Variable
    #: Stores the order of the TaylorPolynomial, defined on instantiation
    order: tf.Variable
    #: Stores the result of fitting the TaylorPolynomial for all particle trajectories
    optimal_parameters: tf.Variable

    # pylint: disable=too-many-arguments
    def __init__(self, order: int, time_grid: np.ndarray, particle_trajectories: np.ndarray,
                 batch_size: int = None, fit_on_init: bool = True):
        """
        :param order: Order of the fitted TaylorPolynomial
        :param time_grid: (#timesteps, )
        :param particle_trajectories: (#particles, #timesteps, 3)
        :param batch_size: used for evaluating the particle trajectories in batches
        :param fit_on_init: If True, the Polynomial is fitted on instantiation of the module.
        """
        if batch_size is not None:
            self.batch_size = tf.Variable(batch_size, dtype=tf.int32, shape=(), trainable=False)
        else:
            self.batch_size = tf.Variable(particle_trajectories.shape[0],
                                          dtype=tf.int32, shape=(), trainable=False)
        self.ref_time = tf.Variable(time_grid[0].astype(np.float32),
                                    dtype=tf.float32, shape=(), trainable=False)
        self.end_time = tf.Variable(time_grid[-1].astype(np.float32),
                                    dtype=tf.float32, shape=(), trainable=False)

        self.current_batch_idx = tf.Variable(0, dtype=tf.int32, shape=(), trainable=False)
        self.current_time_ms = tf.Variable(self.ref_time, dtype=tf.float32, shape=(),
                                           trainable=False)
        self.order = tf.Variable(order, dtype=tf.int32, shape=(), trainable=False)
        self._int_order = order
        self.optimal_parameters = tf.Variable(
            tf.zeros((particle_trajectories.shape[0], order + 1, 3), dtype=tf.float32),
            dtype=tf.float32, shape=(None, None, None), trainable=False)

        super().__init__(name=f"taylor_trajectory_order{order}")
        if fit_on_init:
            t_zero_ref = time_grid - self.ref_time
            self.fit(t_zero_ref, particle_trajectories)

    def fit(self, t_grid: np.ndarray, particle_trajectories: np.ndarray):
        """ Fits a Taylor polynomial of order self.order to each particle trajectory.

        :param t_grid: (T, ) times corresponding to the particle positions
        :param particle_trajectories: (N, T, dim)
        :return: optimal motion parameters (N, order, dim) containing all parameters
                (r0, v, a, j, ...) for N particles
        """
        n_particles, n_steps, n_dims = particle_trajectories.shape
        flattened_trajectories = np.swapaxes(particle_trajectories, 0, 1).reshape(n_steps, -1)
        flat_coefficients = np.polynomial.polynomial.polyfit(t_grid, flattened_trajectories,
                                                             deg=self._int_order)
        coefficients = np.swapaxes(
            flat_coefficients.reshape(self._int_order + 1, n_particles, n_dims)
            , 0, 1)
        self.optimal_parameters.assign(coefficients.astype(np.float32))

    @tf.function
    def _evaluate_trajectory(self, t: tf.Tensor) -> tf.Tensor:
        """ Evaluates the taylor expansion for a the current batch of particles at the specified
        times t.

        :param t: (#timesteps)
        :return: (#particles, #timesteps, 3)
        """
        t = t - self.ref_time
        batch_start = self.current_batch_idx * self.batch_size
        batch_end = batch_start + self.batch_size
        factors = self.optimal_parameters[batch_start:batch_end]
        exponents = tf.range(0, tf.cast(self.order + 1, dtype=tf.float32))[:, tf.newaxis]
        t_pow_n = t[np.newaxis] ** exponents  # (order, time)
        out = tf.reduce_sum(factors[:, :, tf.newaxis] * t_pow_n[tf.newaxis, :, :, tf.newaxis],
                            axis=1)
        return out

    def __call__(self, timing: tf.Tensor, **kwargs) -> (tf.Tensor, dict):
        """ Evaluates the taylor expansion for the current batch of particles at the specified
        times t.

        :param timing: (#timesteps) in milliseconds
        :return: (#particles, #timesteps, 3) in meter

        """
        return self._evaluate_trajectory(timing), {}

    @tf.function
    def increment_particles(self, r: tf.Tensor, dt: tf.Tensor, **kwargs) -> (tf.Tensor, dict):
        """ Evaluates the particle position for the time self.current_time_ms + dt and adds the
        delta t to the current_time_ms variable

        :param r: unused parameter (to adhere to calling signature of trajectory modules)
        :param dt: temporal step lengths
        :param kwargs: unused parameter (to adhere to calling signature of trajectory modules)
        :return: (#batch, 3)
        """
        self.current_time_ms.assign_add(dt)
        new_pos = self._evaluate_trajectory(tf.reshape(self.current_time_ms, [1, ]))
        return new_pos[:, 0], {}
