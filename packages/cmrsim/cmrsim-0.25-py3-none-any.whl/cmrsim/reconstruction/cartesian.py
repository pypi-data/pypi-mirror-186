""" This module contains a collection of standard reconstruction methods using k-space data
 on a cartesian grid """
__all__ = ["Cartesian2D", "Cartesian2DMultiCoil"]

from typing import Union, Tuple, Iterable, Optional
import tensorflow as tf

from cmrsim.reconstruction.base import BaseRecon


class Cartesian2D(BaseRecon):
    """ Plain 2D FFT based reconstruction with zero-padding if enabled """

    def __init__(self, sample_matrix_size: Union[Tuple[int, int]],
                 padding: Optional[Union[Tuple[int, int], Iterable[Tuple[int, int]]]] = None,
                 device: str = "CPU"):
        """ Performs 2D inverse FFT on __call__. If padding argument is given, performs symmetric
         (per direction) padding with the given width prior to iFFT.

        The innermost two dimensions are assumed to represent the image axes after reshaping
         in __call__.

        :param sample_matrix_size: (int, int) This is used to reshape the flattened array/tensor
                                of k-space samples into the correct dimensions, to perform iFFT2d
        :param padding: Optional(int, int) Number of zero-element per border and axis. This means
                                for padding=(10, 5) the dimensions of the k-space array will grow
                                by (20, 10)
                        Iterable[(int, int)], For assymetric padding. i-th tuple contains the
                                padding length before and after for the i-th axis of the sampled
                                 k-space.
        :param device: tf device placement for __call__
        """
        self._sample_matrix_size = tf.constant(sample_matrix_size, dtype=tf.int32)

        if padding is None:
            out_matrix_size = self._sample_matrix_size
            self._padding = None
        else:
            _padding = tf.constant(padding, dtype=tf.int32)
            if tf.size(tf.shape(_padding)) == 1:
                _padding = tf.tile(tf.reshape(_padding, [2, 1]), [1, 2])
            self._padding = _padding
            out_matrix_size = tf.stack([base_size + p[0] + p[1] for base_size, p in
                                        zip(sample_matrix_size, self._padding.numpy())], axis=0)

        super().__init__(out_matrix_size, name="cartesian_2d", device=device)

    def __call__(self, flat_samples):
        """ Reshapes last axis of flat samples into 2D with shape specified in
         self._sampling_matrix_size, and performs 2DiFFT over the two innermost dimensions. Number
         and dimension of all other axis do not have to specified.

        :param flat_samples: (#image, ..., #noise_levels, #k-space-points)
        :return:
        """
        with tf.device(self.device):
            # Reshape to 2D k-space, _sampling_matrix_size is reverted because the k-space samples
            # for cartesian acquisition are ordered Row-Major [*kx1, *kx2, ...]. Reshape expects
            # Column major though. K-space-defintion is natural in row major.
            batch_sizes = tf.shape(flat_samples)[0:-1]

            k_space_shape = tf.concat([batch_sizes, tf.reverse(self._sample_matrix_size, [0, ])],
                                      axis=0)
            k_space_2d = tf.reshape(flat_samples, k_space_shape)
            if self._padding is not None:
                batch_padding = tf.tile(tf.zeros_like(batch_sizes, dtype=tf.int32)[:, tf.newaxis],
                                        [1, 2])
                k_space_2d = tf.pad(k_space_2d, tf.concat((batch_padding, self._padding), 0))

            # Order ifftshift -> ifft2d -> fftshift
            temp = tf.signal.ifftshift(k_space_2d, axes=[-2, -1])
            temp = tf.signal.ifft2d(temp)
            images = tf.signal.fftshift(temp, axes=[-2, -1])
            renormalization_factor = tf.cast(tf.reduce_prod(self.output_matrix_size /
                                                            self._sample_matrix_size), tf.complex64)
        return images * renormalization_factor


class Cartesian2DMultiCoil(Cartesian2D):
    """ Implementation of Roemer reconstruction for multi-coil data """

    def __init__(self, sample_matrix_size: Union[Tuple[int, int]],
                 coil_sensitivities: Union['np.ndarray', tf.Tensor],
                 padding: Optional[Union[Tuple[int, int], Iterable[Tuple[int, int]]]] = None,
                 coil_channel_axis: int = 0, device: str = "CPU"):
        """
        :param sample_matrix_size: (See Cartesian2D)
        :param coil_sensitivities: (#n_coils, X, Y)
        :param padding: (see Cartesian2D)
        """
        self._coil_sensitivities = tf.constant(coil_sensitivities, dtype=tf.complex64)
        self._coil_channel_axis = coil_channel_axis

        super().__init__(sample_matrix_size=sample_matrix_size, padding=padding, device=device)

    def __call__(self, flat_samples: tf.Tensor, coil_channel_axis: int = None):  # noqa
        """

        :param flat_samples: (..., #n_coils, ..., #noise_levels, #k-space-points)
        :param coil_channel_axis: defines the axis index that matches #n_coils must be less than
                                    len(flat_samples.shape) - 2, since the two innermost axes
                                     are exclusively reserved.

        :return: (..., #noise, X, Y, [Z]) reconstructed image batch
        """
        if coil_channel_axis is None:
            coil_channel_axis = self._coil_channel_axis

        single_coil_images = super().__call__(flat_samples)

        with tf.device(self.device):
            n_coils = tf.shape(single_coil_images)[coil_channel_axis:coil_channel_axis + 1]

            # tile sens maps to match the shape of the single_coil_images
            batch_shape = tf.shape(flat_samples)[0:-1]
            broad_cast_shape = tf.concat((batch_shape, tf.shape(self._coil_sensitivities)[1:]), 0)
            temp_shape = tf.ones_like(batch_shape)
            expanded_shape = tf.concat((temp_shape[:coil_channel_axis],
                                        n_coils,
                                        temp_shape[coil_channel_axis + 1:],
                                        tf.shape(self._coil_sensitivities)[1:]),
                                       axis=0)
            expanded_sens_maps = tf.reshape(self._coil_sensitivities, expanded_shape)
            tiled_sensitivity_maps = tf.broadcast_to(expanded_sens_maps, broad_cast_shape)
            numerator = tf.reduce_sum(single_coil_images * tf.math.conj(tiled_sensitivity_maps),
                                      axis=coil_channel_axis)
            denominator = tf.reduce_sum(
                tiled_sensitivity_maps * tf.math.conj(tiled_sensitivity_maps),
                axis=coil_channel_axis)
            roemer_image = numerator / denominator
        return roemer_image
