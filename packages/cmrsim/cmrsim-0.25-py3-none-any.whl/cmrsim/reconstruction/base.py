""" This module contains the base implementation that should be used for all reconstruction
implementations """
__all__ = ["BaseRecon", ]

from typing import Union, Tuple
from abc import abstractmethod

import tensorflow as tf


class BaseRecon(tf.Module):
    """ Abstract base class of reconstruction modules """
    #: Tensor defining the shape of the returned, reconstructed images which can be
    # different from the sampling matrix
    output_matrix_size: tf.Tensor = None

    def __init__(self, output_matrix_size: Union[Tuple[int, int, int], Tuple[int, ...], tf.Tensor],
                 name: str, device: str = None):
        """ Base class for type hinting

        :param output_matrix_size: Stores the resulting image shape after reconstruction
        :param name: str Defines the name-space for the reconstruction module
        """
        super().__init__(name=name)

        if device is None:
            if tf.config.get_visible_devices('GPU'):
                self.device = 'GPU:0'
            else:
                self.device = 'CPU:0'
        else:
            self.device = device

        self.output_matrix_size = tf.constant(output_matrix_size, dtype=tf.int32)

    @abstractmethod
    def __call__(self, flat_samples: tf.Tensor):
        """ Performs reconstruction algorithm defined by sub-class for defined input-signature!

        :param flat_samples: (#repetitions, x*y) or
                             (#repetitions, #noise_instatiations, x*y)
                             representing the discretized k-space
        :return: iFFT of input (#repetitions, [#noise_instantiations], x, y)
        """

        raise NotImplementedError('You tried to call an abstract build-class method. '
                                  'Please refer to another specific reconstruction-subclass!')
