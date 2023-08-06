"""Contains implementations to iteratively simulate particle trajectory within flow-fields"""
__all__ = ["FlowTrajectory", "TurbulentTrajectory", "TimeVaryingVelocityField"]

from typing import List, Tuple

import tensorflow as tf
import numpy as np

from cmrsim.analytic.contrast import LookUpTableModule
from cmrsim.trajectory._base import BaseTrajectoryModule


# pylint: disable=abstract-method
class FlowTrajectory(BaseTrajectoryModule, LookUpTableModule):
    """ Numerically integrates the path of particles in a velocity field and simultaneoulsy
    looks up all additional field values for the previous particle positions.


    .. dropdown:: Example usage

        .. code-block:: python
            :caption: Instantiation

            velocity_field_3d = ...  # shape - (X, Y, Z, 3)
            map_dimensions = [(x_lo, x_hi), (y_lo, y_hi), (z_lo, z_hi)]
            field_list = []  # ... no addition a field mapping
            trajectory_module = FlowTrajectory(velocity_field_3d, map_dimensions, field_list)

        .. code-block:: python
            :caption: Call function

            r_init = ...  # initial_positions of shape (N, 3)
            timing = np.arange(0., 1.01, 0.01)
            r_at_timing, fields = trajectory_module(r_init, timing, dt_max=0.01,
                                                   return_velocities=True)

        .. code-block:: python
            :caption: increment particle positions

            r_init = ...  # initial_positions of shape (N, 3)
            delta_t = tf.constant(0.01, tf.float32)
            r_new, fields = self.trajectory_module.increment_particles(r_init, dt=delta_t)


    :param velocity_field: (X, Y, Z, 3+n) 3D map storing gridded velocities in m/s at positions
                                        X, Y, Z. Unit should be m/ms
                                        Additional dimensions past 3 are treated as additional
                                        data fields
    :param map_dimensions: (3, 2) -> [(xlow, xhigh), (ylow, yhigh), (zlow, zhigh)]
                                     Physical extend of the gridded velocity fields.
    :param additional_dimension_mapping: List of name/len pairs to unstack the looked up
                                        values. If not None this mapping must explain all
                                        'n' additional dimension in the parameter
                                        velocity-field e.g. [('off_res', 1)] meaning that
                                        off-resonance for all time points has a size of 1,
                                        starting from index 3 in velocity field.
    :param kwargs: - device: str defaults to CPU:0

    """
    def __init__(self, velocity_field: np.ndarray, map_dimensions: np.ndarray,
                 additional_dimension_mapping: List[Tuple[str, int]] = None, **kwargs):

        """
        :param velocity_field: (X, Y, Z, 3+n) 3D map storing gridded velocities in m/s at positions
                                            X, Y, Z. Unit should be m/ms
                                            Additional dimensions past 3 are treated as additional
                                            data fields
        :param map_dimensions: (3, 2) -> [(xlow, xhigh), (ylow, yhigh), (zlow, zhigh)]
                                         Physical extend of the gridded velocity fields.
        :param additional_dimension_mapping: List of name/len pairs to unstack the looked up
                                              values. If not None this mapping must explain all
                                              'n' additional dimension in the parameter
                                              velocity-field e.g. [('off_res', 1)] meaning that
                                              off-resonance for all time points has a size of 1,
                                              starting from index 3 in velocity field.
        :param kwargs: - device: str defaults to CPU:0
        """

        if not hasattr(self, 'n_adim'):
            self.n_adim = velocity_field[..., 3:].shape[-1]
        if additional_dimension_mapping is not None:
            field_dims = [v[1] for v in additional_dimension_mapping]
            field_labels = [v[0] for v in additional_dimension_mapping]
            check_n_dim = sum(field_dims)
            assert self.n_adim == check_n_dim

            field_dims = np.cumsum(field_dims).tolist()
            field_dims.insert(0, 0)
            self._field_names = {k: (field_dims[i], field_dims[i + 1])
                                 for i, k in enumerate(field_labels)}
        else:
            self._field_names = {}

        super().__init__(velocity_field, map_dimensions, name="flow_trajectory_evaluation",
                         **kwargs)
    # pylint: disable=too-many-arguments, too-many-locals
    def __call__(self, initial_positions: tf.Tensor, timing: tf.Tensor, dt_max: float,
                 verbose: bool = True, return_velocities: bool = False) -> (tf.Tensor, dict):
        """ Evaluates the increment particle function for multiple steps, and for the times matching
        the argument values, stores the position.

        :param initial_positions: (#particles, 3)
        :param timing: float - in seconds
        :param dt_max: Maximal temporal step width in milliseconds
        :param verbose: bool
        :param return_velocities: if True, the velocities for each time-step is saved and returned
                                    as entry of the additional fields dictionary
        :return: (#particles, n_steps, 3) - tf.Tensors, Trajectory,
                  dict(field-name: tf.Tensor with shape (#particles, n_steps, n_components))
                  field values at trajectory locations
        """
        time_grid = np.arange(0., timing[-1], dt_max)
        insertion_index = np.searchsorted(time_grid, timing)
        time_grid = np.unique(np.insert(time_grid, insertion_index, timing))
        saving_indices = iter(enumerate(np.concatenate([np.searchsorted(time_grid, timing), [-1]])))

        positions = np.empty([timing.shape[0], *initial_positions.shape], dtype=np.float32)

        additional_fields = []
        particle_positions = initial_positions
        result_idx, current_save_index = next(saving_indices)
        if current_save_index == 0:
            positions[result_idx] = particle_positions
            result_idx, current_save_index = next(saving_indices)
            data = self.linear_interpolation(r_vectors=particle_positions)
            fields = self._unstack_add_dims(data[:, 3:])
            if return_velocities:
                fields['velocity'] = data[:, 0:3]
            additional_fields.append(fields)

        for step_idx, dt in enumerate(np.diff(time_grid)):

            particle_positions, fields = self.increment_particles(
                                                        particle_positions, dt,
                                                        return_velocities=return_velocities)
            if step_idx+1 == current_save_index:
                positions[result_idx] = particle_positions
                result_idx, current_save_index = next(saving_indices)
                additional_fields.append(fields)
        trajectories = tf.transpose(positions, [1, 0, 2])
        return trajectories, additional_fields

    @tf.function(jit_compile=True, reduce_retracing=True)
    def increment_particles(self, particle_positions: tf.Tensor,
                            dt: tf.Tensor, return_velocities: bool = False) \
            -> (tf.Tensor, dict):
        # pylint: disable=anomalous-backslash-in-string
        """ For given particle positions and specified time-interval returns the values of all
        additional fields at the initial particle position and moves the particles according
        to:

        .. math::

            r_{t+1} = r_{t} + \delta t v(r_{t})

        where v is assumed to be specified in m/ms and :math:`\\delta t` in ms

        :param particle_positions: (-1, 3) batch of 3D particle coordinates
        :param dt: scalar value in ms
        :param return_velocities: if True the additional field lookup contains the field "velocity"
        :return: new particle positions (-1, 3), dict(\*\*additional_fields[-1, c])
        """
        data = self.linear_interpolation(r_vectors=particle_positions)
        additional_fields = self._unstack_add_dims(data[:, 3:])
        if return_velocities:
            additional_fields["velocity"] = data[..., 0:3]
        return particle_positions + data[:, 0:3] * dt, additional_fields

    def _unstack_add_dims(self, lookup_result: tf.Tensor) -> dict:
        """ Unstacks the channel axis [-1]  of the additional field lookup according to the
        internal field definitions.
        :param lookup_result: tensor of shape (..., #channel)
        :return: dict
        """
        return {name: lookup_result[..., lo:hi] for name, (lo, hi) in self._field_names.items()}


# pylint: disable=abstract-method
class TurbulentTrajectory(FlowTrajectory):
    """ Numerically integrates the path of particles in a mean velocity field and incorporates
    random turbulent velocity
    fluctuations based on Langevin updates from sampled RST values.
    Looks up and returns additional fields for the previous particle positions.

        .. dropdown:: Example usage

            .. code-block:: python
                :caption: Instantiation

                velocity_field_3d = ...  # shape - (X, Y, Z, 10)
                map_dimensions = [(x_lo, x_hi), (y_lo, y_hi), (z_lo, z_hi)]
                field_list = []  # ... no addition a field mapping
                trajectory_module = TurbulentTrajectory(velocity_field_3d, map_dimensions, field_list)

            .. code-block:: python
                :caption: Call function

                r_init = ...  # initial_positions of shape (N, 3)
                timing = np.arange(0., 1.01, 0.01)
                r_at_timing, fields = trajectory_module(r_init, timing, dt_max=0.01,
                                                       return_velocities=True)

            .. code-block:: python
                :caption: increment particle positions

                r_init = ...  # initial_positions of shape (N, 3)
                delta_t = tf.constant(0.01, tf.float32)
                r_new, fields = self.trajectory_module.increment_particles(r_init, dt=delta_t)


        :param velocity_field: (X, Y, Z, 10+n) 3D map storing gridded fields at positions X, Y, Z.
                                            Fields 0-2 : Mean velocities (X, Y, Z).  Unit should be m/ms
                                            Fields 3-8 : Lower triangular Cholesky decomposition of the turbulent
                                                         Reynolds stress tensor, L. Ordering is
                                                         (L11, L21, L22, L31, L32, L33)
                                            Field 9 : Langevin timescale tau, in Hz.
                                            Additional dimensions past 9 are treated as additional
                                            data fields and returned
        :param map_dimensions: (3, 2) -> [(xlow, xhigh), (ylow, yhigh), (zlow, zhigh)]
                                         Physical extend of the gridded velocity fields.
        :param additional_dimension_mapping: List of name/len pairs to unstack the looked up
                                              values. If not None this mapping must explain all
                                              'n' additional dimension in the parameter
                                              velocity-field e.g. [('off_res', 1)] meaning that
                                              off-resonance for all time points has a size of 1,
                                              starting from index 10 in velocity field.
        :param kwargs: - device: str defaults to CPU:0
        """

    def __init__(self, velocity_field: np.ndarray, map_dimensions: np.ndarray,
                 additional_dimension_mapping: List[Tuple[str, int]] = None, **kwargs):
        """
        :param velocity_field: (X, Y, Z, 10+n) 3D map storing gridded fields at positions X, Y, Z.
                                            Fields 0-2 : Mean velocities (X, Y, Z).  Unit should be m/ms
                                            Fields 3-8 : Lower triangular Cholesky decomposition of the turbulent
                                                         Reynolds stress tensor, L. Ordering is
                                                         (L11, L21, L22, L31, L32, L33)
                                            Field 9 : Langevin timescale tau, in Hz.
                                            Additional dimensions past 9 are treated as additional
                                            data fields and returned
        :param map_dimensions: (3, 2) -> [(xlow, xhigh), (ylow, yhigh), (zlow, zhigh)]
                                         Physical extend of the gridded velocity fields.
        :param additional_dimension_mapping: List of name/len pairs to unstack the looked up
                                              values. If not None this mapping must explain all
                                              'n' additional dimension in the parameter
                                              velocity-field e.g. [('off_res', 1)] meaning that
                                              off-resonance for all time points has a size of 1,
                                              starting from index 10 in velocity field.
        :param kwargs: - device: str defaults to CPU:0
        """
        self.prev_v_turb = tf.Variable(tf.zeros([1, 3]), shape=(None, 3), dtype=tf.float32)
        self.n_adim = velocity_field[..., 10:].shape[-1]
        super().__init__(velocity_field, map_dimensions, **kwargs)

    # pylint: disable=too-many-arguments, redefined-builtin
    def __call__(self, initial_positions: tf.Tensor, timing: tf.Tensor, dt_max: float,
                 verbose: bool = True, return_velocities: bool = False) -> (tf.Tensor, dict):
        # pylint: disable=unused-variable
        __doc__ = super().__call__.__doc__
        return super().__call__(initial_positions, timing, dt_max,
                                verbose=verbose, return_velocities=return_velocities)

    # pylint: disable=too-many-arguments, too-many-locals
    @tf.function(jit_compile=False, reduce_retracing=True)
    def increment_particles(self, particle_positions: tf.Tensor, dt: tf.Tensor,
                            return_velocities: bool = False):
        """ For given particle positions and specified time-interval returns the values of all
        additional fields at the initial particle position and moves the particles according
        to:

        .. math::

            r_{t+\\delta t} = r_{t} + \\delta t (U(r_{t}) + u_{t})

            u_{t} = u_{t-\\delta t} e^{-\\frac{\\delta t}{\\tau}} + \\zeta \\sqrt{1-e^{-2 \\frac{\\delta t}{\\tau}}}

        where U is the mean velocity in m/ms, u is fluctuating velocity in m/ms, :math:`\\tau` is the Langevin timescale
        in ms, and :math:`\\zeta` is a random Gaussian sample from the Reynolds stress tensor.

        :param particle_positions: (-1, 3) batch of 3D particle coordinates
        :param dt: scalar value in ms
        :param return_velocities: if True the additional field lookup contains the field "velocity"
        :return: new particle positions (-1, 3), dict(\*\*aditional_fields[-1, c])
        """
        data = self.linear_interpolation(r_vectors=particle_positions)
        v_mean = data[:, 0:3]

        # Random sample from RST (Cholesky decomposition)
        impuls = tf.random.normal([tf.shape(particle_positions)[0], 3])
        vtu = impuls[:, 0] * data[:, 3]
        vtv = tf.reduce_sum(impuls[:, :2] * data[:, 4:6], axis=1)
        vtw = tf.reduce_sum(impuls * data[:, 6:9], axis=1)

        # Damping term for previous turbulence velocity
        damping = tf.exp(-dt * data[:, 9] / 1000)
        damping = tf.where(tf.math.is_finite(damping), damping, tf.zeros_like(damping))

        # Damping term for new turbulence velocity
        damping_update = tf.sqrt(1. - damping ** 2)
        damping_update = tf.where(tf.math.is_finite(damping_update), damping_update,
                                  tf.zeros_like(damping_update))

        # New turbulence velocity
        v_turb = damping_update[:, tf.newaxis] * tf.stack([vtu, vtv, vtw], axis=1)

        #refmap = tf.reshape(tf.floor(data[:, 10]), [tf.shape(v_turb)[0], 1])

        # Old + new turbulence velocity
        v_turb = self.prev_v_turb * tf.reshape(damping, [tf.shape(v_turb)[0], 1]) + v_turb

        #v_turb = refmap * v_turb + (refmap - 1) * self.prev_v_turb

        v_total = v_mean + v_turb
        additional_fields = self._unstack_add_dims(data[:, 10:])
        self.prev_v_turb.assign(v_turb)
        if return_velocities:
            additional_fields["velocity"] = v_total

        return particle_positions + v_total * dt, additional_fields

    def warmup_step(self, particle_positions: tf.Tensor):
        """ Updates turbulence velocity of all particles based on sampled RST values at their positions.
        Used to initialize turbulence velocity to prevent transient states due to long Langevin timescales

        :param particle_positions: (-1, 3) batch of 3D particle coordinates
        """
        data = self.linear_interpolation(r_vectors=particle_positions)
        impuls = tf.random.normal([tf.shape(particle_positions)[0], 3])

        vtu = impuls[:, 2] * data[:, 3]
        vtv = tf.reduce_sum(impuls[:, 1:] * data[:, 4:6], axis=1)
        vtw = tf.reduce_sum(impuls * data[:, 6:9], axis=1)
        self.prev_v_turb.assign(tf.stack([vtu, vtv, vtw], axis=1))

    def turbulence_reseed_update(self, in_tol, new_particle_positions: tf.Tensor):
        """ Updates turbulence velocity for a subset of particles based on their positions.
         Intended for use when initializing newly seeded particles during reseeding.

        :param in_tol: Indices of subset of particles
        :param new_particle_positions: (-1, 3) 3D particle coordinates for subset of particles
        """
        old_vturb = self.prev_v_turb.numpy()[in_tol]
        data = self.linear_interpolation(r_vectors=new_particle_positions)
        impuls = tf.random.normal([tf.shape(new_particle_positions)[0], 3])
        vtu = impuls[:, 2] * data[:, 3]
        vtv = tf.reduce_sum(impuls[:, 1:] * data[:, 4:6], axis=1)
        vtw = tf.reduce_sum(impuls * data[:, 6:9], axis=1)
        new_vturb = tf.concat([old_vturb, tf.stack([vtu, vtv, vtw], axis=1)], axis=0)
        self.prev_v_turb.assign(new_vturb)


# pylint: disable=abstract-method
class TimeVaryingVelocityField(FlowTrajectory):
    """Implements a the the path integration for particles in a temporally varying velocity field
    and also lookups for temporally varying fields. The internal representation of the field is
    of shape (T, X, Y, Z, 3+n). By keeping track of the current time in an internal variable, the
    current interval of the zeroth axis is determined. Temporal linear interpolation of the looked
    up values is used.

    .. dropdown:: Example usage

        .. code-block:: python
            :caption: Instantiation

            const_velocities = Quantity(np.zeros([21, 21, 200, 3], dtype=np.float32), "m/s")
            const_velocities[..., 2] = Quantity(10, "cm/s")
            linear_increasing_v = np.tile(const_velocities.m_as("cm/s")[np.newaxis],
                                          [11, 1, 1, 1, 1])
            linear_increasing_v = Quantity(lin_inc_velocities *
                                            np.linspace(0, 1, 11).reshape(11, 1, 1, 1, 1), "cm/s")
            time_grid = Quantity(np.arange(0, 51, 5), "ms")
            map_dimension = Quantity([[-4, 4], [-4, 4], [-10, 30]], "cm").to("m")
            field_list = []
            trajectory_module = TimeVaryingVelocityField(
                                    time_grid.m_as("ms"),
                                    np.array(lin_inc_velocities.m_as("m/ms"), dtype=np.float32),
                                    np.array(map_dimension.m_as("m"), dtype=np.float32), field_list)

    :param time_grid: (T, ) time in milliseconds defining the grid points of the varying
                        velocity_fields
    :param velocity_field: (T, X, Y, Z, 3+n) 3D map storing gridded velocities in m/s at
                                positions X, Y, Z. Unit should be m/ms. Additional dimensions
                                past 3 are treated as additional data fields.
    :param map_dimensions: (3, 2) -> [(xlow, xhigh), (ylow, yhigh), (zlow, zhigh)]
                                     Physical extend of the gridded velocity fields.
    :param additional_dimension_mapping: List of name/len pairs to unstack the looked up
                        values. If not None this mapping must explain all 'n' additional
                        dimension in the parameter velocity-field e.g. ('off_res', 1) meaning
                        that the 1 index (starting from 3) in velocity field describes the
                        off-resonance at all time points.
    :param kwargs: - device: str defaults to CPU:0
    """
    def __init__(self, time_grid: np.array, velocity_field: np.ndarray, map_dimensions: np.ndarray,
                 additional_dimension_mapping: List[Tuple[str, int]] = None,
                 **kwargs):
        """

        :param time_grid: (T, ) time in milliseconds defining the grid points of the varying
                            velocity_fields
        :param velocity_field: (T, X, Y, Z, 3+n) 3D map storing gridded velocities in m/s at
                                    positions X, Y, Z. Unit should be m/ms. Additional dimensions
                                    past 3 are treated as additional data fields.
        :param map_dimensions: (3, 2) -> [(xlow, xhigh), (ylow, yhigh), (zlow, zhigh)]
                                         Physical extend of the gridded velocity fields.
        :param additional_dimension_mapping: List of name/len pairs to unstack the looked up
                            values. If not None this mapping must explain all 'n' additional
                            dimension in the parameter velocity-field e.g. ('off_res', 1) meaning
                            that the 1 index (starting from 3) in velocity field describes the
                            off-resonance at all time points.
        :param kwargs: - device: str defaults to CPU:0
        """
        super().__init__(velocity_field, map_dimensions, additional_dimension_mapping, **kwargs)
        with tf.device(self.device):
            self.time_grid = tf.constant(time_grid, dtype=tf.float32)
            self._current_time = tf.Variable(self.time_grid[0], shape=(), dtype=tf.float32)

    # pylint: disable=too-many-arguments, redefined-builtin
    def __call__(self, initial_positions: tf.Tensor, timing: tf.Tensor, dt_max: float,
                 verbose: bool = True, return_velocities: bool = False) -> (tf.Tensor, dict):
        # This explicit definition is a hacky trick to make the super().__call__ docstring show
        # in documentation without showing all inherited members
        # pylint: disable=unused-variable
        __doc__ = super().__call__.__doc__
        return super().__call__(initial_positions, timing, dt_max,
                                verbose=verbose, return_velocities=return_velocities)

    # pylint: disable=anomalous-backslash-in-string
    @tf.function(jit_compile=False, reduce_retracing=True)
    def increment_particles(self, particle_positions: tf.Tensor, dt: tf.Tensor,
                            return_velocities: bool = False) -> (tf.Tensor, dict):
        """ For given particle positions and specified time-interval returns the values of all
        additional fields at the initial particle position and moves the particles according
        to:

        .. math::

            r_{t+1} = r_{t} + \\delta t v(r_{t}, t)

        where :math:`v(r_{t}, t)` is assumed to be specified in m/ms and :math:`\\delta t` in ms.
        The temporal dependency for :math:`v(r_{t}, t)` is evaluated by linear interpolation
        of lookups at the reference times given as zeroth dimension of the look-up map.
        The current interval is determined by the variable self._current_time.

        :param particle_positions: (-1, 3) batch of 3D particle coordinates
        :param dt: scalar value in ms
        :param return_velocities: if True the additional field lookup contains the field "velocity"
        :return: new particle positions (-1, 3), dict(\*\*aditional_fields[-1, c])
        """
        with tf.device(self.device):
            time_idx = tf.searchsorted(self.time_grid, [self._current_time], side="left")[0]
            data = self.linear_interpolation(particle_positions,
                                             batch_index=tf.stack([time_idx, time_idx + 1]))
            v_left, v_right = tf.unstack(data[..., :3], axis=0)
            time_idx = tf.reshape(time_idx, [])
            time_interval = self.time_grid[time_idx + 1] - self.time_grid[time_idx]
            t_interp = (self._current_time - self.time_grid[time_idx]) / time_interval
            v_interp = (1 - t_interp) * v_left + t_interp * v_right
            additional_data = (1 - t_interp) * data[0, ..., 3:] + t_interp * data[1, ..., 3:]
            self._current_time.assign_add(dt)

            additional_data = self._unstack_add_dims(additional_data)
            if return_velocities:
                additional_data["velocity"] = v_interp
            return particle_positions + v_interp * dt, additional_data

    def reset_time(self):
        """ Sets the internal time-tracker to the first value of time grid"""
        self._current_time.assign(self.time_grid[0])
