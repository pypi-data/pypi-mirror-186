"""Contains implementation of Bloch-solving operator including multiple receive coils"""

__all__ = ["ParallelReceiveBlochOperator"]

from typing import List, Tuple, Union, TYPE_CHECKING

import tensorflow as tf
import numpy as np

from cmrsim.bloch._generic import GeneralBlochOperator
from cmrsim.bloch.submodules import BaseSubmodule
from cmrsim.trajectory import StaticParticlesTrajectory

if TYPE_CHECKING:
    import cmrsim.analytic.contrast.coil_sensitivities


class ParallelReceiveBlochOperator(GeneralBlochOperator):
    """Extends the GeneralBlochOperator with parallel receive functionality. The only additionally
    required input is an instance of a CoilSensitivity contrast module from the
    cmrsim.analytic.contrast submodule, which is used internally to apply a spatially dependent
    weight to the transverse magnetization before summing, in the process of acquiring signals.

    The resulting signal is also stored in the 'time_signal_acc' attribute, where for the
    parallel receive case each entry has an additional axis corresponding to the number of coils.

    :param name: Verbose name of the module (non-functionally relevant)
    :param gamma: gyromagnetic ratio in rad/ms/m
    :param coil_module:
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
    #: Instance of the cmrsim.analytic.contrast.CoilSensitivity class that is used to compute
    #: the positionally dependent sensitivity factors prior to sampling
    coil_lookup_module: 'cmrsim.analytic.contrast.coil_sensitivities.CoilSensitivity'

    #:
    n_coils: int

    def __init__(self, name: str,
                 gamma: float,
                 coil_module: Union['cmrsim.analytic.contrast.coil_sensitivities.CoilSensitivity'],
                 time_grid: tf.Tensor,
                 adc_events: tf.Tensor,
                 gradient_waveforms: tf.Tensor = None,
                 rf_waveforms: tf.Tensor = None,
                 submodules: Tuple[BaseSubmodule, ...] = (),
                 device: str = None):
        """


        """
        super().__init__(name=name, gamma=gamma, time_grid=time_grid,
                         gradient_waveforms=gradient_waveforms, rf_waveforms=rf_waveforms,
                         adc_events=adc_events, submodules=submodules, device=device)
        self.coil_lookup_module = coil_module
        self.n_coils = self.coil_lookup_module.expansion_factor

        # Expand the dimension of the signal accumulator to incorporate coil-maps
        with tf.device("CPU"):
            self.time_signal_acc = [
                tf.Variable(initial_value=tf.zeros([v.read_value().shape[0], self.n_coils], dtype=tf.complex64),
                            shape=(None, self.n_coils), dtype=tf.complex64, trainable=False,
                            name=f"k_segment_{idx}") for idx, v in enumerate(self.time_signal_acc)]

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
                 - batch_signal (#reps, #samples, #coils) -> used for signal accumulation
        """
        (rf_waveforms, gradient_waveforms, adc_events, adc_phase, adc_writing_indices,
         batch_signal) = super()._init_tensors(n_samples, n_repetitions, repetition_index)
        batch_signal = tf.zeros(shape=(n_samples, n_repetitions, self.n_coils), dtype=tf.complex64)
        return (rf_waveforms, gradient_waveforms, adc_events, adc_phase,
                adc_writing_indices, batch_signal)

    def _sample(self, adc_events: tf.Tensor, adc_phase: tf.Tensor, adc_writing_idx: tf.Tensor,
                magnetization: tf.Tensor, M0: tf.Tensor, r: tf.Tensor, batch_signal: tf.Tensor):
        """Sums up the :math:`m_{xy}^{+}` magnetization weighted with the associated proton-density
        of the particles and adds the signal to the batch-signal accumulator ad index specified
        in adc_writing_index. Before summation, a coil-sensitivity weighting is applied

        :param adc_events: (#reps, )
        :param adc_phase: (#reps, )
        :param adc_writing_idx: (#reps, )
        :param magnetization: (#batch, )
        :param M0: (n_repetitions/1, #batch)
        :param r: (n_repetitions/1, #batch, 3) particle positions
        :param batch_signal: (#samples, #reps, #coils)
        :return:
        """
        n_active_adc_channels = tf.reduce_sum(adc_events, axis=0)
        if n_active_adc_channels >= 1.:
            # Sum over all M+ = Mx+iMy weighted by M0 and the coil-sensitivity to compute signal
            sense_factors = self.coil_lookup_module.lookup_complex_coil_factors(r)
            weighted_magnetization = magnetization[..., 0, tf.newaxis] * sense_factors
            weighted_magnetization= weighted_magnetization * tf.complex(M0[..., tf.newaxis], 0.)
            signal = tf.reduce_sum(weighted_magnetization, axis=1)

            # Demodulate signal with receiver phase
            demodulated_signal = signal * tf.exp(tf.complex(0., -adc_phase[..., tf.newaxis]))

            # Gather and accumulate signal only for repetitions that have an active ADC-event
            n_reps = tf.shape(adc_writing_idx)[0]
            in_bounds = tf.where(adc_writing_idx > -1)[:, 0]
            # batch signal has shape (#samples, #reps, #coils) which defines the stacking-order here
            indices = tf.stack([adc_writing_idx, tf.range(n_reps, dtype=tf.int32)], axis=1)
            indices = tf.gather(indices, in_bounds)
            demodulated_signal = tf.gather(demodulated_signal, in_bounds)
            batch_signal = tf.tensor_scatter_nd_add(batch_signal, indices, demodulated_signal)
        return batch_signal
