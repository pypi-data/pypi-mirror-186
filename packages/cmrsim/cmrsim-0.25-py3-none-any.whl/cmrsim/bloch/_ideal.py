""" This module contains Ideal bloch operators making simplifying assumptions"""
__all__ = ["InstantaneousPulse", "PerfectSpoiling"]

import tensorflow as tf
import numpy as np

from cmrsim.bloch._base import BaseBlochOperator


# pylint: disable=abstract-method
class InstantaneousPulse(BaseBlochOperator):
    """ Module designed debug simulation by assuming instananeous excitation with a given flip angle
    and slice-profile

    :param complex_flip_angle: (n, ) - tf.complex64
    :param slice_position:
    :param slice_thickness:
    :param slice_normal:
    :param slice_profile:
    :param device:
    """
    # pylint: disable=too-many-arguments
    def __init__(self, complex_flip_angle: tf.Tensor,
                 slice_position: tf.Tensor, slice_thickness: float,
                 slice_normal: tf.Tensor, slice_profile: str = None,
                 device: str = None):
        super().__init__(name="instantaneous_pulse", device=device)

        self.flip_angle = tf.Variable(complex_flip_angle, shape=(None, ), dtype=tf.complex64)
        self.slice_normal = tf.Variable(slice_normal, shape=(3,), dtype=tf.float32)
        self.slice_position = tf.Variable(slice_position, shape=(3,), dtype=tf.float32)
        self.slice_thickness = tf.Variable(slice_thickness, shape=(), dtype=tf.float32)
        self.n_steps = 1
        self.slice_profile = slice_profile
        self.n_repetitions = complex_flip_angle.shape[0]

    def __call__(self, trajectory_module: callable, initial_position: tf.Tensor,
                 magnetization: tf.Tensor, repetition_index: tf.Tensor = 0, **kwargs):
        positions, _ = trajectory_module.increment_particles(initial_position, dt=0.)

        with tf.device(self.device):
            if self.flip_angle.shape[0] == 1:  # override pulse index in case of single FA
                repetition_index = 0
            flip_angle, phase = self._fa_from_slice_profile(positions, pulse_index=repetition_index)
            complex_alpha = tf.complex(flip_angle, 0.) * tf.exp(tf.complex(0., phase))
        return self.hard_pulse(complex_alpha, magnetization)

    def _fa_from_slice_profile(self, r_vectors: tf.Tensor,
                               pulse_index: tf.Tensor = tf.constant(0, tf.int32)):
        distance_to_slice = tf.einsum("ni, i",  r_vectors - self.slice_position[tf.newaxis, :],
                                      self.slice_normal)
        normalized_distance = tf.abs(distance_to_slice) / self.slice_thickness

        if self.slice_profile == "Sinc1":
            profile = np.sinc(normalized_distance)
        else:
            profile = tf.where(tf.abs(normalized_distance) < 0.5,
                               tf.ones_like(distance_to_slice), tf.zeros_like(distance_to_slice))
        flip_angle = tf.abs(self.flip_angle[pulse_index]) * profile
        phase = tf.math.angle(self.flip_angle[pulse_index]) * tf.ones_like(distance_to_slice)
        return flip_angle, phase


# pylint: disable=abstract-method
class PerfectSpoiling(BaseBlochOperator):
    """ Module designed to debug simulations by making residual magnetization effects negligible"""
    def __call__(self, magnetization: tf.Tensor, **kwargs):
        """ Simply sets the transverse magnetization to 0.

        :param magnetization: (#batch, 3)
        :return: (#batch, 3)
        """
        mask_tensor = tf.reshape(tf.constant([0, 0, 1], dtype=tf.complex64), [1, 3])
        return magnetization * mask_tensor
