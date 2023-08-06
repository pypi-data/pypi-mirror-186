"""Contains implementation of Bloch-solving operator"""

__all__ = ["GeneralBlochOperator"]

from typing import List, Tuple, Union

import tensorflow as tf
import numpy as np

from cmrsim.bloch._base import BaseBlochOperator
from cmrsim.bloch.submodules import BaseSubmodule
from cmrsim.trajectory import StaticParticlesTrajectory


# pylint: disable=abstract-method
class GeneralBlochOperator(BaseBlochOperator):
    # pylint: disable=anomalous-backslash-in-string
    """ General bloch-simulation module: accepts RF-Waveforms, Gradient-Waveforms and ADC-events as
    input and integrates the Bloch-equation (trapezoidal numerical integration). The specified
    time-grid does not need to be uniform, but must match the definition of the specified
    waveforms/adc definitions. The required input format matches the common format of a
    sequence diagram

    The integration allows for moving isochromates, as well as the addition of effects defined
    in the submodules. For more information on how the isochromate motion is incorporated
    refer to the \_\_call\_\_ method.

    .. dropdown:: Example usage

        .. code-block:: python
            :caption: Instantiation

            # time_raster.shape, grad_grid.shape, rf_grid.shape, adc_grid.grid
            # >>> (n_reps, t), (n_reps, t, 2), (n_reps, t), (n_reps, t, 2)
            gammarad = system_specs.gamma_rad.m_as("rad/mT/ms")
            bloch_mod = cmrsim.bloch.GeneralBlochOperator(name="example",
                                                           device="GPU:0,
                                                           gamma=gammarad,
                                                           time_grid=time_raster,
                                                           gradient_waveforms=grad_grid,
                                                           rf_waveforms=rf_grid,
                                                           adc_events=adc_grid)

        .. code-block:: python
            :caption: Sequential call

            properties = ...  # From input definition
            n_samples = tf.shape(module.gradient_waveforms)[1]
            n_repetitions = tf.shape(module.gradient_waveforms)[0]
            data_iterator = tf.data.Dataset.from_tensor_slices(properties)
            for phantom_batch in tqdm(data_iterator.batch(int(3e5))):
                m, r = bloch_mod(trajectory_module=trajectory_module,
                                 run_parallel=True, **phantom_batch)

        .. code-block:: python
            :caption: Sequential call

            properties = ...  # From input definition
            n_samples = tf.shape(module.gradient_waveforms)[1]
            n_repetitions = tf.shape(module.gradient_waveforms)[0]

            data_iterator = tf.data.Dataset.from_tensor_slices(properties)
            for phantom_batch in tqdm(data_iterator.batch(int(3e5))):
                r = phantom_batch.pop("initial_position")
                m = phantom_batch.pop("magnetization")
                for rep_idx in tqdm(range(n_repetitions)):
                    m, r = module(trajectory_module=trajectory_module, initial_position=r,
                                  magnetization=m, repetition_index=rep_idx, run_parallel=False,
                                  **phantom_batch)

    :param name: Verbose name of the module (non-functionally relevant)
    :param gamma: gyromagnetic ratio in rad/ms/m
    :param time_grid: (n_steps) - tf.float32 - time definition for numerical integration steps
    :param gradient_waveforms: (#repetitions, #steps, 3) - tf.float32 - Definition of gradients
                        in mT/m
    :param rf_waveforms: (#repetitions, #steps) - tf.complex64 -
    :param adc_events: (#repetition, #steps, 2) - tf.float32 - last axis contains the adc-on
                            definitions and the adc-phase
    :param submodules: List[tf.Modules] implementing the __call__ function returning the
                            resulting phase increment contribution
    :param device: str
    """
    #: (Non-uniform) temporal raster defining the simulation steps in milliseconds - shape: (T, )
    time_grid: tf.Variable = None

    #: Grid containing the differences of specified time_grid -  shape: (T-1, )
    dt_grid: tf.Variable

    #: Gradient waveforms at times of self.time_grid in mT/m for R repetitions - shape: (R, T, 3)
    gradient_waveforms: tf.Variable = None

    #: Complex radio-frequency pulse definition at times of self.time_grid in uT for R repetitions
    #: - shape: (R, T)
    rf_waveforms: tf.Variable = None

    #: Sampling events definitions for each time in self.time_grid for R repetitions - shape
    #: (R, T, 2), where the two channels have the following meaning: 1. ADC On/Off [1/0] at time t
    #: and 2. Demodulation phase of the ADC at time t in radians
    adc_events: tf.Variable = None

    #: Accumulator variables for the signal acquired at specified adc-events. This is empty if no
    #: ADC==On events where specified. The length of the List is equal to the number of repetitions
    #: and the shape of each tf.Variable is (sum(ADC[R]==1), ), which can result different length
    #: if the repetitions have different numbers of samples.
    time_signal_acc: List[tf.Variable] = None

    #: Number of repetitions derived from specified waveforms
    n_repetitions: int

    #: Gyromagnetic ration in rad/ms/m specified on instantiation
    gamma: float

    def __init__(self, name: str,
                 gamma: float,
                 time_grid: tf.Tensor,
                 gradient_waveforms: tf.Tensor = None,
                 rf_waveforms: tf.Tensor = None,
                 adc_events: tf.Tensor = None,
                 submodules: Tuple[BaseSubmodule, ...] = (),
                 device: str = None):
        """
        :param name: Verbose name of the module (non-functionaly relevant)
        :param gamma: gyromagnetic ratio in rad/ms/m
        :param time_grid: (n_steps) - tf.float32 -
        :param gradient_waveforms: (#repetitions, #steps, 3) - tf.float32 - Definition of gradients
                            in mT/m
        :param rf_waveforms: (#repetitions, #steps) - tf.complex64 -
        :param adc_events: (#repetition, #steps, 2) - tf.float32 - last axis contains the adc-on
                                definitions and the adc-phase
        :param submodules: List[tf.Modules] implementing the __call__ function returning the
                                resulting phase increment contribution
        :param device: str
        """
        super().__init__(name, device=device)

        # Validate input waveforms such that they match in shape
        waveforms = [gradient_waveforms, rf_waveforms, adc_events]
        shape_matching_time = [g.shape[1] == time_grid.shape[0] for g in waveforms if g is not None]
        shape_matching_reps = set([g.shape[0] for g in waveforms if g is not None])
        if len(shape_matching_time) == 0:
            raise ValueError("No wave-forms (rf/grads) specified")
        if not all(shape_matching_time):
            raise ValueError("Number of time-steps in specified wave-forms do not "
                             f"match {shape_matching_time}")
        if not len(shape_matching_reps) == 1:
            raise ValueError("Number of iterations in specified waveforms do not match")

        self.n_repetitions = list(shape_matching_reps)[0]
        self.gamma = tf.constant(gamma, dtype=tf.float32)

        # Create the Variable instances for actual simulation calls
        with tf.device(self.device):
            self.time_grid = tf.Variable(time_grid, dtype=tf.float32, shape=(None,),
                                         trainable=False)
            self.dt_grid = tf.Variable(np.diff(time_grid), dtype=tf.float32, shape=(None,),
                                       trainable=False)

        if gradient_waveforms is not None:
            with tf.device(self.device):
                self.gradient_waveforms = tf.Variable(gradient_waveforms, dtype=tf.float32,
                                                      shape=(None, None, 3), trainable=False)
        if rf_waveforms is not None:
            with tf.device(self.device):
                self.rf_waveforms = tf.Variable(rf_waveforms, dtype=tf.complex64,
                                                shape=(None, None), trainable=False)
        if adc_events is not None:
            with tf.device(self.device):
                self.adc_events = tf.Variable(adc_events[:, :, 0], dtype=tf.float32,
                                              shape=(None, None), trainable=False)
                self.adc_phase = tf.Variable(adc_events[:, :, 1], dtype=tf.float32,
                                             shape=(None, None), trainable=False)

            n_events_per_rep = [tf.where(e > 0).shape[0] for e in self.adc_events.read_value()]
            shape_rep = [(n,) for n in n_events_per_rep]
            with tf.device("CPU"):
                self.time_signal_acc = [tf.Variable(initial_value=tf.zeros(s, dtype=tf.complex64),
                                                    shape=(None,),
                                                    dtype=tf.complex64, trainable=False,
                                                    name=f"k_segment_{idx}")
                                        for idx, s in enumerate(shape_rep)]

        # Register submodules
        self._submodules = submodules

    # pylint: disable=invalid-name
    def __call__(self, initial_position: tf.Tensor, magnetization: tf.Tensor,
                 T1: tf.Tensor, T2: tf.Tensor, M0: tf.Tensor,
                 trajectory_module: tf.Module = StaticParticlesTrajectory(),
                 repetition_index: tf.Tensor = 0,
                 run_parallel: bool = False, **kwargs):
        """ Runs bloch simulation for the specified RF/Gradients and accumulates the signal for the
        times specified in adc_events. For each interval on the time grid, a trapezoidal
        integration of the flip angle and the gradient phase increment (including the submodules)
        is performed and subsequently used to rotate the magnetization vectors.

        :param initial_position: (#batch, 3) - tf.float32 - initial positions of particles
        :param magnetization: ([repetitions/1], #batch, 3) - tf.complex64 -
                                    [Mx+iMy, Mx-iMy, Mz] magnetization per particle. The first
                                    optional axis is only used if `run_parallel==True`.
        :param T1: (#batch, ) - tf.float32 - Longitudinal relaxation time in milliseconds
                                per particle
        :param T2: (#batch, ) - tf.float32 - Transversal relaxtion time in milliseconds per particle
        :param M0: (#batch, ) - tf.float32 - Equilibrium magnetization of each particle
                                            (representing a volume)
        :param trajectory_module: tf.function accepting the arguments
            [r[:, 3](tf.float32), dt[,](tf.float32)] and returning the updated position
            r_new[:, 3](tf.float32) as well as a dictionary of tensors denoting arbitrary look-up
            values for the new particle positions. Defaults to static particles
        :param repetition_index: (, ) - tf.int32 - index of the current repetition index to simulate
                                    this corresponds to indexing the first dimension of the
                                    specified waveforms. Only used if `run_parallel==False`
        :param run_parallel: bool - defaults to False. If True, the repetitions of the specified
                                    waveforms are simulated for the same particle trajectories.
                                    Otherwise only the waveforms for given `repetition_index` is
                                    simulated.
        :param kwargs: additional properties of particles, that are required for evaluating the
                        submodules
        :return: m, r  with shapes
            - [#reps, #particles, 3] if repetitions are run in parallel
            - [#particles, 3] if run sequential
        """
        # Add leading axis for repetitions in case it is not present, to allow for correct
        # broadcasting in _call_core
        if len(tf.shape(magnetization)) == 2:
            magnetization = magnetization[tf.newaxis]
        initial_position, T1, T2, M0 = [v[tf.newaxis] for v in (initial_position, T1, T2, M0)]

        if run_parallel:
            # m.shape = (#repetitions, #batch, 3)  | r.shape = (#batch, 3)
            m, r = self._call_par(trajectory_module=trajectory_module,
                                  initial_position=initial_position,
                                  magnetization=magnetization, T1=T1, T2=T2, M0=M0,
                                  **kwargs)
        else:
            # m.shape = (#batch, 3)  | r.shape = (#batch, 3)
            m, r = self._call_seq(trajectory_module=trajectory_module,
                                  initial_position=initial_position,
                                  magnetization=magnetization, T1=T1, T2=T2, M0=M0,
                                  repetition_index=repetition_index, **kwargs)
        return m, r

    # pylint: disable=invalid-name
    def _call_seq(self, trajectory_module: callable, initial_position: tf.Tensor,
                  magnetization: tf.Tensor, T1: tf.Tensor, T2: tf.Tensor,
                  M0: tf.Tensor, repetition_index: Union[tf.Tensor, int] = 0, **kwargs):
        """ Calculates n_samples and calls `self._call_core` for sequential simulation.
        Writes the simulated signal to the time_signal_acc of the corresponding repetition index
        :return: m (#batch, 3), r (#batch, 3)
        """
        if self.adc_events is not None:
            n_samples = tf.shape(self.time_signal_acc[int(repetition_index)])[0]
        else:
            n_samples = tf.constant(0, dtype=tf.int32)

        # this call does the heavy lifting in form of a compiled Kernel
        rep_idx = tf.constant(repetition_index, dtype=tf.int32)
        m, r, batch_signal = self._call_core(repetition_index=rep_idx,
                                             n_repetitions=1,
                                             n_samples=n_samples,
                                             trajectory_module=trajectory_module,
                                             initial_position=initial_position,
                                             magnetization=magnetization,
                                             T1=T1, T2=T2, M0=M0, **kwargs)
        # Squeeze zeroth axis by indexing
        if self.adc_events is not None:
            self.time_signal_acc[int(repetition_index)].assign_add(batch_signal[0])
        return m[0], r[0]

    # pylint: disable=invalid-name
    def _call_par(self, trajectory_module: callable, initial_position: tf.Tensor,
                  magnetization: tf.Tensor, T1: tf.Tensor, T2: tf.Tensor,
                  M0: tf.Tensor, **kwargs):
        """ Calculates n_samples and n_repetitions to  `self._call_core` for parallel simulation.
        Writes the simulated signal to the time_signal_acc of the corresponding repetition index
        :return: m (#batch, 3), r (#batch, 3)
        """
        if self.adc_events is not None:
            active_adc_channels_per_time = tf.cast(tf.reduce_sum(self.adc_events, axis=0) >= 1.,
                                                   tf.int32)
            n_samples = tf.cast(tf.reduce_sum(active_adc_channels_per_time, axis=0), tf.int32)
        else:
            n_samples = tf.constant(0, dtype=tf.int32)

        if self.gradient_waveforms is not None:
            n_repetitions = tf.shape(self.gradient_waveforms)[0]
        elif self.rf_waveforms is not None:
            n_repetitions = tf.shape(self.rf_waveforms)[0]
        elif self.adc_events is not None:
            n_repetitions = tf.shape(self.adc_events)[0]
        else:
            # This case can only be reached if all above components are deleted after instantiation
            raise ValueError("No waveforms specified")

        if magnetization.shape[0] == 1:
            magnetization = tf.tile(magnetization, [n_repetitions, 1, 1])
        elif magnetization.shape[0] != n_repetitions:
            raise ValueError(magnetization.sha)

        m, r, batch_signal = self._call_core(repetition_index=tf.constant(0, tf.int32),
                                             n_repetitions=int(n_repetitions),
                                             n_samples=n_samples,
                                             trajectory_module=trajectory_module,
                                             initial_position=initial_position,
                                             magnetization=magnetization,
                                             T1=T1, T2=T2, M0=M0, **kwargs)
        if self.adc_events is not None:
            for idx, sig in enumerate(batch_signal):
                first_n_entries = tf.cast(tf.reduce_sum(self.adc_events[idx]), tf.int32)
                self.time_signal_acc[idx].assign_add(sig[:first_n_entries])
        return m, r[0]

    # pylint: disable=invalid-name
    @tf.function(jit_compile=False, reduce_retracing=True)
    def _call_core(self, repetition_index: tf.Tensor, n_repetitions: Union[tf.Tensor, int],
                   n_samples: tf.Tensor, trajectory_module: callable,
                   initial_position: tf.Tensor, magnetization: tf.Tensor,
                   T1: tf.Tensor, T2: tf.Tensor, M0: tf.Tensor, **kwargs):
        """

        .. note::

             Assumes the last interval is never an active ADC-sample

        :param repetition_index: 0 for par, actual index for sequential
        :param n_repetitions: actual n_reps for par, 1 for sequential
        :param n_samples:
        :param trajectory_module:
        :param initial_position: (#batch, 3)
        :param magnetization: (n_repetitions/1, #batch, 3)
        :param T1: (n_repetitions/1, #batch)
        :param T2: (n_repetitions/1, #batch)
        :param M0: (n_repetitions/1, #batch)
        :param kwargs:
        :return:  - magnetization
                  - r_next
                  - signal at adc_on==True with shape (n_repetitions, n_samples)
        """
        with tf.device(self.device):
            rf_waveforms, grad_waveforms, adc_on, adc_phase, adc_widx, batch_signal = \
                self._init_tensors(n_samples, n_repetitions, repetition_index)

            r_prev = tf.reshape(initial_position, [1, -1, 3])
            r_next = r_prev

            # Iterate over all time intervals to obtain the magnetization evolution
            for t_idx in tf.range(1, tf.shape(self.dt_grid)[0]+1):

                # The shape of the magnetization tensor must always be (#reps, #batch, 3), with
                # needs to be specified for tf.autograph as:
                tf.autograph.experimental.set_loop_options(
                    shape_invariants=[(magnetization, tf.TensorShape([None, None, 3])),
                                      (r_next, tf.TensorShape([None, None, 3]))])

                # Increment particle positions and if available field definitions at given locations
                # r_next.shape = (#particles, #nsteps=1)
                r_next, additional_fields = trajectory_module.increment_particles(r_prev[0], self.dt_grid[t_idx-1])
                r_next = r_next[tf.newaxis]   # add dummy #reps-dim for subsequent broadcasting

                # Evaluate effective flip angle for given interval and apply the hard-pulse rotation
                if self.rf_waveforms is not None:
                    rf = rf_waveforms[:, t_idx-1:t_idx+1]
                    alpha = (tf.complex(self.dt_grid[t_idx-1] * self.gamma, 0.)
                             * (rf[:, 1] + rf[:, 0]) / 2)
                    magnetization = self.hard_pulse(alpha[:, tf.newaxis], magnetization)

                # Evaluate effective phase increment for given interval including the submodule
                # effects and apply the corresponding rotation of the magnetization vectors
                delta_phi = tf.zeros_like(M0, dtype=tf.float32)
                if self.gradient_waveforms is not None:
                    grad = grad_waveforms[..., t_idx-1:t_idx+1, :]
                    gdotr_l = tf.reduce_sum(grad[..., 0, :] * r_prev, axis=-1)
                    gdotr_r = tf.reduce_sum(grad[..., 1, :] * r_next, axis=-1)
                    delta_phi += (gdotr_l + gdotr_r) / 2. * self.gamma * self.dt_grid[t_idx-1]

                for submod in self._submodules:
                    phi_s = submod(
                        gradient_wave_form=grad_waveforms[:, 0, t_idx:t_idx+1, :],
                        trajectories=r_next[:, :, tf.newaxis], dt=self.dt_grid[t_idx-1],
                        **additional_fields, **kwargs)
                    if tf.shape(phi_s)[0] < tf.shape(delta_phi)[0]:
                        phi_s = tf.tile(phi_s, [tf.shape(delta_phi)[0], 1, 1])
                    # phi_s shape = (#reps, #particles, #nsteps=1)
                    tf.ensure_shape(phi_s, (None, None, 1))
                    delta_phi = tf.reshape(delta_phi + phi_s[:, :, 0], [n_repetitions, -1])

                # delta phi for current interval with (nreps, nbatch) dimension
                tf.ensure_shape(delta_phi, (None, None))
                magnetization = self.phase_increment(delta_phi[:, tf.newaxis], magnetization)

                # Relax magnetization for the time interval
                magnetization = self.relax(T1, T2, self.dt_grid[t_idx-1], magnetization)

                # If adc-events are specified and the current interval is set to 'on' calculate
                # the weighed sum over all particles and demodulate according to the current ADC
                # phase. The result is then written into the signal return array.
                if self.adc_events is not None:
                    batch_signal = self._sample(adc_on[:, t_idx], adc_phase[:, t_idx],
                                                adc_widx[:, t_idx], magnetization, M0,
                                                r_next, batch_signal)
                    
                r_prev = r_next

            # This transposition is made complicated to enable function reuse for methods that add
            # axes to the batch signal (such as multiple coils). It is functionally the same as
            # np.swapaxes(arr, 0, 1), as this method's signature defines the returned signal have
            # the repetition at 0th position.
            transpose_indices = tf.range(tf.shape(tf.shape(batch_signal))[0])
            transpose_indices = tf.tensor_scatter_nd_update(transpose_indices, [[0], [1]], [1, 0])
            batch_signal = tf.transpose(batch_signal, transpose_indices)

            return magnetization, r_next, batch_signal

    def _init_tensors(self, n_samples: int, n_repetitions: int, repetition_index: int):
        """ Initializes / slices the waveforms according to the specified current repetitions and
        number of samples.

        :param n_samples:
        :param n_repetitions:
        :param repetition_index:
        :return: - rf_waveform (#reps, #steps) or None
                 - grad_waveform (#reps, #steps, 3) or None
                 - adc_events (#reps, #steps) or None
                 - adc_phase (#reps, #steps) or None
                 - adc_writing_idx (#reps, #steps) or None
                 - batch_signal (#reps, #samples) -> used for signal accumulation
        """
        batch_signal = tf.zeros(shape=(n_samples, n_repetitions), dtype=tf.complex64)
        repetitions = tf.range(repetition_index, repetition_index + n_repetitions, 1)

        # If rf waveforms are specified, gather all required repetitions (either all or 1)
        if self.rf_waveforms is not None:
            current_rf_waveforms = tf.gather(self.rf_waveforms, repetitions, axis=0)
        else:
            current_rf_waveforms = None

        # If gradient waveforms are specified, gather all required repetitions (either all or 1)
        # and calculate the left value of for trapezoidal phase integration
        if self.gradient_waveforms is not None:
            current_gradient_waveforms = tf.gather(self.gradient_waveforms, repetitions,
                                                   axis=0)[:, tf.newaxis]
        else:
            current_gradient_waveforms = None

        # If adc events are specified, gather all required repetitions (either all or 1)
        # or otherwise create a default zero return value for the batch signal as this it is
        # required autographing this function by tensorflow
        if self.adc_events is not None:
            current_adc_events = tf.gather(self.adc_events, repetitions, axis=0)
            current_adc_phase = tf.gather(self.adc_phase, repetitions, axis=0)
            adc_writing_indices = tf.cast(tf.math.cumsum(current_adc_events, axis=1) * current_adc_events - 1, tf.int32)
        else:
            current_adc_events, current_adc_phase, adc_writing_indices = None, None, None

        return (current_rf_waveforms, current_gradient_waveforms, current_adc_events,
                current_adc_phase, adc_writing_indices, batch_signal)

    @staticmethod
    def _sample(adc_events: tf.Tensor, adc_phase: tf.Tensor, adc_writing_idx: tf.Tensor,
                magnetization: tf.Tensor, M0: tf.Tensor, r: tf.Tensor, batch_signal: tf.Tensor):
        """Sums up the :math:`m_{xy}^{+}` magnetization weighted with the associated proton-density
        of the particles and adds the signal to the batch-signal accumulator ad index specified
        in adc_writing_index.

        :param adc_events: (#reps, )
        :param adc_phase: (#reps, )
        :param adc_writing_idx: (#reps, )
        :param magnetization: (#batch, )
        :param M0: (n_repetitions/1, #batch)
        :param r: (n_repetitions/1, #batch, 3)
        :param batch_signal: (#samples, #reps)
        :return:
        """
        n_active_adc_channels = tf.reduce_sum(adc_events, axis=0)
        if n_active_adc_channels >= 1.:
            # Sum over all M+ = Mx+iMy weighted by M0 and demodulate with receiver phase
            signal = tf.reduce_sum(magnetization[..., 0] * tf.complex(M0, 0.), axis=1)
            demodulated_signal = signal * tf.exp(tf.complex(0., -adc_phase))

            # Gather signal for active adc-channels and add to signal accumulator
            n_reps = tf.shape(adc_writing_idx)[0]
            in_bounds = tf.where(adc_writing_idx > -1)[:, 0]
            # batch signal has shape (#samples, #reps) which defines the order of stacking here:
            indices = tf.stack([adc_writing_idx, tf.range(n_reps, dtype=tf.int32)], axis=1)
            indices = tf.gather(indices, in_bounds)
            demodulated_signal = tf.gather(demodulated_signal, in_bounds)
            batch_signal = tf.tensor_scatter_nd_add(batch_signal, indices, demodulated_signal)
        return batch_signal

    def reset(self):
        """ Resets the time-signal accumulators, i.e. sets all entries to 0"""
        if self.time_signal_acc is not None:
            for v in self.time_signal_acc:
                v.assign(np.zeros_like(v.numpy()))
