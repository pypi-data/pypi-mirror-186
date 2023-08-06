""" This module contains all modules that are related to cartesian sampling strategies.
"""

__all__ = ["EPI", "SingleLinePerShot"]

from typing import List, Tuple, Union, Optional

import tensorflow as tf
from deprecated import deprecated

from cmrsim.analytic.encoding.base import BaseSampling


# pylint: disable=abstract-method
class SingleLinePerShot(BaseSampling):
    """ Encoding Module that assumes the handed in signal tensor in images space to be calculated
    according to one process per k-space line. Number of segments in this implementation
    corresponds to number of acquired k-space lines
    """
    # pylint: disable=too-many-arguments
    def __init__(self, field_of_view: Union[Tuple[float, float], List[float]],
                 sampling_matrix_size: Union[Tuple[int, int], List[int], 'numpy.ndarray'],
                 absolute_noise_std: float,
                 read_out_duration: float = None,
                 repetition_time: float = 0.,
                 acquisition_start: Optional[float] = 0.,
                 orientation: tf.Tensor = tf.eye(3, 3, dtype=tf.float32),
                 **kwargs):

        self.fov = tf.Variable(tf.constant(field_of_view), dtype=tf.float32, name='field_of_view')
        self.matrix_size = tf.Variable(tf.constant(sampling_matrix_size), dtype=tf.int32,
                                       name='acquisition_matrix')
        self.readout_duration = tf.Variable(tf.constant(read_out_duration), dtype=tf.float32,
                                            name='readout_duration')
        self.acquisition_time_offset = tf.Variable(tf.constant(acquisition_start), dtype=tf.float32,
                                                   name='acquisition_offset')
        self.repetition_time = tf.Variable(tf.constant(repetition_time), dtype=tf.float32,
                                           name='repetition_time')
        self.orientation = tf.constant(orientation, dtype=tf.float32)
        super().__init__(absolute_noise_std, name="single_line_pershot",
                         k_space_segments=sampling_matrix_size[1], **kwargs)

    def _calculate_trajectory(self) -> (tf.Tensor, tf.Tensor):
        """ Calculates the 2D k-space trajectory for a cartesian readout. The k_z component of all
        3D-k-space sampling points is set to 0 to calculate averaging in z-direction.

        For even as well as uneven matrix dimension, the first k-space sample is acquired at
        [-k_max, -k_max, 0] and it is guaranteed, that the mid, or mid+1/2 sampling point is
        at the k-space center.

        :return: k-space-vectors, sampling-times (tf.Tensor, tf.Tensor)
        """
        ro_steps = tf.cast(self.matrix_size[0], tf.float32)
        pe_steps = tf.cast(self.matrix_size[1], tf.float32)

        # Calculate k-space-vectors
        k_x, k_y, k_z = tf.meshgrid(tf.range(self.matrix_size[0]), tf.range(self.matrix_size[1]),
                                    1, indexing='xy')
        k_vectors = tf.stack((k_x, k_y, k_z), -1)
        k_vectors = k_vectors - tf.constant([int(ro_steps), int(pe_steps), 0], shape=(3,)) // 2
        delta_k = tf.math.divide_no_nan(1., self.fov)
        k_vectors = tf.cast(k_vectors, tf.float32) * tf.concat((delta_k, [0.]), 0)
        k_vectors = tf.reshape(k_vectors, [-1, 3])

        # Calculate Sampling times from matrix size, ADC-duration, blip-duration
        # and leading time offset
        dwell_time_borders = tf.range(0., ro_steps + 1.) / ro_steps * self.readout_duration
        dwell_time_centers = dwell_time_borders[:-1] + \
                             (dwell_time_borders[1:] - dwell_time_borders[:-1]) / 2
        sampling_times = tf.tile(dwell_time_centers,
                                 [self.matrix_size[1], ]) - self.readout_duration.read_value() / 2
        k_vectors = tf.einsum('ij, nj -> ni', tf.transpose(self.orientation), k_vectors)
        return k_vectors, sampling_times


@deprecated(reason="Consider using the cmrsim.analytic.encoding.GenericEncoding class in"
                   "combination with a cmrseq.sequence definition")
# pylint: disable=abstract-method
class EPI(BaseSampling):
    """ Encoding Module implementing a single shot echo planar imaging trajectory.
     The subdivision into segments is solely used to manage memory limitation during simulation.
    """
    # pylint: disable=too-many-arguments
    def __init__(self, field_of_view: Union[Tuple[float, float], List[float]],
                 sampling_matrix_size: Union[Tuple[int, int], List[int], 'numpy.ndarray'],
                 absolute_noise_std: float,
                 read_out_duration: float = None,
                 bandwidth_per_pixel: float = None,
                 blip_duration: Optional[float] = 0.,
                 acquisition_start: Optional[float] = 0., **kwargs):
        """ Calculates a trajectory for a 2D cartesian sampling and initializes a BaseSampling
        object with the given k-space vectors.

        :param field_of_view: Total length in (RO, PE) directions
        :param sampling_matrix_size: Integers determining the number of uniform sampling points in
                                        RO and PE directions
        :param absolute_noise_std: Passed through to build class.
        :param read_out_duration: in ms, used to calculate sampling times (centers of
                                        dwell time intervals)
        :param bandwidth_per_pixel: in Hz, used to calculate read_out_duration
                                        (only one can be specified)
        :param blip_duration: in ms, time between readout events
        :param acquisition_start: in ms, leading offset prior to acquisition (defaults to 0.)
        """
        if ((bandwidth_per_pixel is None and read_out_duration is None) or
                (bandwidth_per_pixel is not None and read_out_duration is not None)):
            raise ValueError(f'Only exactly one of the arguments (pixel_bandwith/read_out_duration)'
                             f' must be specified. Instead pixel_bandwith: {bandwidth_per_pixel} '
                             f'and read_out_duration: {read_out_duration}, was given!')

        self.fov = tf.Variable(tf.constant(field_of_view), dtype=tf.float32, name='field_of_view')
        self.matrix_size = tf.Variable(tf.constant(sampling_matrix_size), dtype=tf.int32,
                                       name='acquisition_matrix')
        if read_out_duration is None:
            read_out_duration = 1000. / bandwidth_per_pixel  # noqa
        self.readout_duration = tf.Variable(tf.constant(read_out_duration), dtype=tf.float32,
                                            name='readout_duration')
        self.acquisition_time_offset = tf.Variable(tf.constant(acquisition_start), dtype=tf.float32,
                                                   name='acquisition_offset')
        self.blip_duration = tf.Variable(tf.constant(blip_duration), dtype=tf.float32,
                                         name='blip_duration')
        super().__init__(absolute_noise_std, name="epi", **kwargs)

    def _calculate_trajectory(self) -> (tf.Tensor, tf.Tensor):
        """ Calculates the 2D k-space trajectory for a cartesian readout. The k_z component of all
         3D-k-space sampling points is set to 0 to calculate averaging in z-direction.

        For even as well as uneven matrix dimension, the first k-space sample is acquired at
         [-k_max, -k_max, 0] and it is guaranteed, that the mid, or mid+1/2 sampling point is at
         the k-space center.

        :return: k-space-vectors, sampling-times (tf.Tensor, tf.Tensor)
        """
        ro_steps = tf.cast(self.matrix_size[0], tf.float32)
        pe_steps = tf.cast(self.matrix_size[1], tf.float32)

        # Calculate k-space-vectors
        k_x, k_y, k_z = tf.meshgrid(tf.range(self.matrix_size[0]), tf.range(self.matrix_size[1]),
                                    1, indexing='xy')

        k_vectors = tf.stack((k_x, k_y, k_z), axis=-1)
        k_vectors = k_vectors - tf.constant([int(ro_steps), int(pe_steps), 0], shape=(3,)) // 2
        delta_k = tf.math.divide_no_nan(1., self.fov)
        k_vectors = tf.cast(k_vectors, tf.float32) * tf.concat((delta_k, [0.]), 0)
        k_vectors = tf.reshape(k_vectors, [-1, 3])

        # Calculate Sampling times from matrix size, ADC-duration, blip-duration
        # and leading time offset
        dwell_time_borders = tf.range(0., ro_steps + 1.) / ro_steps * self.readout_duration
        dwell_time_centers = dwell_time_borders[:-1] + \
                             (dwell_time_borders[1:] - dwell_time_borders[:-1]) / 2
        pe_offsets = tf.range(0., pe_steps) * (self.blip_duration + self.readout_duration)

        sampling_time_matrix = dwell_time_centers[tf.newaxis] + pe_offsets[:, tf.newaxis]
        alternating_sign = tf.reshape(
            tf.stack([tf.ones(self.matrix_size[1], dtype=tf.float32),
                      -tf.ones(self.matrix_size[1], dtype=tf.float32)], axis=1),
            [-1, 1])[0:self.matrix_size[1]]
        sampling_time_matrix = tf.where(alternating_sign > 0., sampling_time_matrix,
                                        tf.reverse(sampling_time_matrix, axis=[1, ]))
        sampling_times = tf.reshape(sampling_time_matrix, [-1]) - self.acquisition_time_offset
        return k_vectors, sampling_times
