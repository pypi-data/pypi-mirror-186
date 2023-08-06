""" This module contains the generic implementation of encoding modules using sequence
 definitions from cmrseq """

__all__ = ["GenericEncoding"]

from typing import Union, Iterable

import tensorflow as tf
import cmrseq

from cmrsim.analytic.encoding.base import BaseSampling


# pylint: disable=abstract-method
class GenericEncoding(BaseSampling):
    """" Interface to use cmr-seq definitions of k-space samples as encoder"""
    def __init__(self, name: str,
                 sequence: Union[cmrseq.Sequence, Iterable[cmrseq.Sequence]],
                 absolute_noise_std: Union[float, Iterable[float]],
                 device: str = None):
        """

        :param name: Name of the module
        :param sequence: List or single instance of cmrseq.Sequence that implements the
                            calculate_kspace() function
        :param absolute_noise_std: Noise standard deviation
        :param device: Name of device that the operation is placed on
        """

        if isinstance(sequence, cmrseq.Sequence):
            sequence = [sequence, ]
        self.sequence_list = sequence
        super().__init__(absolute_noise_std, name, device=device,
                         k_space_segments=len(self.sequence_list))

    def _calculate_trajectory(self) -> (tf.Tensor, tf.Tensor):
        """ Calls the calculate_kspace() for all entries in self._sequence_list, stacks the k-space
        vectors and flattens the array()
        :return:  kspace-vectors, timing
        """
        k_space, timings = [], []
        for seq in self.sequence_list:
            _, k_adc, t_adc = seq.calculate_kspace()
            k_space.append(k_adc.T)
            timings.append(t_adc)

        # pylint: disable=no-value-for-parameter, unexpected-keyword-arg
        k_space = tf.cast(tf.concat(k_space, axis=0), tf.float32)
        # pylint: disable=no-value-for-parameter, unexpected-keyword-arg
        timings = tf.cast(tf.concat(timings, axis=0), tf.float32)
        return k_space, timings
