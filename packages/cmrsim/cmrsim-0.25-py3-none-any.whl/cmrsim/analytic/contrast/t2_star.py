""" This module contains the implementation of T2Star decay """
__all__ = ["StaticT2starDecay"]

from typing import Union, TYPE_CHECKING

import tensorflow as tf

from cmrsim.analytic.contrast.base import BaseSignalModel

if TYPE_CHECKING:
    import numpy as np


# pylint: disable=abstract-method
class StaticT2starDecay(BaseSignalModel):
    """ Evaluation of T2-star effect. Initializes a module to calculate the T2* decay
     sampling times in milliseconds, according to:

    .. math::

        M_{xy}^{i, \\prime} = M_{xy}^{i} exp(-\\delta/T2*),

    where :math:`\\delta` is the duration from the RF-excitation center for GRE sequences
    while it is the temporal distance to the echo-center for SE sequences.


    If sequence is Spin-Echo, the sampling times before echo-center have to be negative.

    :param sampling_times: timing of acquisition (ADC) events in milliseconds
                            of shape (#reps, #k-space-points)
    """
    required_quantities = ('T2star', )

    #: timing of acquisition (ADC) events in milliseconds
    # Assumes the duration from the RF-excitation center for GRE sequences and the temporal
    # distance to the echo-center for SE sequences.
    sampling_times: tf.Variable

    def __init__(self, sampling_times: Union[tf.Tensor, 'np.ndarray'], expand_repetitions: bool, **kwargs):
        """ Initializes a module to calculate the T2* decay sampling times in milliseconds,
        according to:

        .. math::

            M_{xy}^{i, \\prime} = M_{xy}^{i} exp(-\\delta/T2*),

        where :math:`\\delta` is the duration from the RF-excitation center for GRE sequences
        while it is the temporal distance to the echo-center for SE sequences.

        .. note::
            This module does not expand the repetition axis, but it always broad-casts the internal
            calculations to work for all #repetions > 0

        :param sampling_times: timing of acquisition (ADC) events in milliseconds
                                of shape (#reps, #k-space-points)
        """
        super().__init__(expand_repetitions=expand_repetitions, name="static_t2star", **kwargs)

        if not(len(sampling_times.shape) == 1 or len(sampling_times.shape) == 2):
            raise ValueError("Invalid shape for specified sampling_times. "
                             "Must either be only (#k-space-points) or "
                             f"(#repetitions, #k-space-points), but is: {sampling_times.shape}")
        if len(sampling_times.shape) == 1:
            sampling_times = tf.reshape(sampling_times, [1, -1])

        self.sampling_times = tf.Variable(tf.constant(sampling_times, tf.float32),
                                          shape=(None, None), dtype=tf.float32)
        self.expansion_factor = sampling_times.shape[0]

    def update(self):
        super().update()
        self.expansion_factor == tf.shape(self.sampling_times.read_value())[0]

    # pylint: disable=signature-differs
    def __call__(self, signal_tensor: tf.Tensor, T2star: tf.Tensor,  **kwargs):
        """ Evaluates the T2* operator

        :param signal_tensor: (#voxel, #repetitions, #k-space-samples)
                            #repetitions and #k-space-samples can be1
        :param T2star: tf.Tensor (#voxel, 1, 1) in milliseconds
        :param segment_index: int, if k-space is segmented for Memory reasons. defaults to 0
        :return: signal_tensor (#voxel, #repetition, #k-space-samples) with #k-space-samples > 1
        """
        with tf.device(self.device):
            input_shape = tf.shape(signal_tensor)
            n_samples = tf.shape(self.sampling_times)[-1]

            tf.Assert(tf.shape(T2star)[1] == 1 or tf.shape(T2star)[1] == self.expansion_factor,
                      ["Shape missmatch for input argument T2star"])
            tf.Assert(input_shape[2] == 1 or input_shape[2] == n_samples,
                      ["Shape missmatch for input argument signal_tensor and self.sampling_times"])
            exponent = self.sampling_times / T2star
            decay_factor = tf.cast(tf.exp(-exponent), tf.complex64)  # (p, self.exp, k)

            if self.expand_repetitions or self.expansion_factor == 1:
                result = signal_tensor[:, :, tf.newaxis, :] * decay_factor[:, tf.newaxis, :, :]
                new_shape = tf.stack([input_shape[0], input_shape[1] * self.expansion_factor,
                                       n_samples], axis=0)
                result = tf.reshape(result, new_shape)
            else:
                tf.Assert(input_shape[1] == self.expansion_factor,
                          ["Shape missmatch for input argument signal_tensor for case no-expand"])
                result = signal_tensor * decay_factor
            return result

