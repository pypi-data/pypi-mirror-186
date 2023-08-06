""" This module contains the base implementation for all bloch simulation based building blocks. """
__all__ = ["BaseBlochOperator"]

import tensorflow as tf
from numpy import pi as np_pi


# pylint: disable=abstract-method
class BaseBlochOperator(tf.Module):
    """Module implementing the basic bloch-simulation operations
    [phase-increment, hard-pulse, relax] """
    #: Number of repetitions that can be indexed during __call__
    n_repetitions: tf.Tensor  # of type tf.int32

    def __init__(self, name: str, device: str = None):
        super().__init__(name=name)
        if device is None:
            if tf.config.get_visible_devices('GPU'):
                self.device = 'GPU:0'
            else:
                self.device = 'CPU:0'
        else:
            self.device = device

    @staticmethod
    @tf.function(jit_compile=True, reduce_retracing=True)
    def phase_increment(phi: tf.Tensor, magnetization: tf.Tensor):
        """  Evaluates rotation of magnetization vectors for given phase increments corresponding
        to an applied gradient. Sums over time-dimension of phase incrementing steps and only
        returns the final magnetization.

        :param phi: (..., #time) tf.float32
        :param magnetization: (..., #time, 3) tf.complex64
        :return: rotated magnetization - (..., 3) - tf.complex64
        """
        final_phi = tf.reduce_sum(phi, axis=1)
        c_phi = tf.exp(tf.complex(0., final_phi))
        rotation = tf.stack([c_phi, tf.math.conj(c_phi), tf.ones_like(c_phi)], axis=-1)
        return magnetization * rotation

    @staticmethod
    @tf.function(jit_compile=True, reduce_retracing=True)
    def cumulative_phase_increment(phi: tf.Tensor, magnetization: tf.Tensor) -> tf.Tensor:
        """ Evaluates rotation of magnetization vectors for given phase increments corresponding
        to an applied gradient. Returns the phase per time step.

        :param phi: (#batch, #time, 3) - tf.float32 - rotation angle of transverse magnetization
        :param magnetization: (#batch, #time, 3) - tf.complex64 - containing the normalized
                                magnetization (Mx+jMy, Mx+jMy, Mz) per particle
        :return: rotated magnetization for each time step - (#batch, #time, 3) - tf.complex64
        """
        cumulative_phi = tf.math.cumsum(phi, axis=1)
        c_phi = tf.exp(tf.complex(0., cumulative_phi))
        cumulative_rotation = tf.stack([c_phi, tf.math.conj(c_phi), tf.ones_like(c_phi)], axis=-1)
        return tf.einsum('bti, bi -> bti', cumulative_rotation, magnetization)

    @staticmethod
    @tf.function(jit_compile=True, reduce_retracing=True)
    def hard_pulse(alpha: tf.Tensor, magnetization: tf.Tensor) -> tf.Tensor:
        """ Evaluates the rotation of magnetization vectors for a given complex flip angle
        corresponding to a RF pulse. A RF pulse with zero phase (only real values) is
        defined as rotation around the y-axis. This means, for the initial magnetization
        (0+0j, 0-0j, 1.) and a flip angle of 90 degrees, the returned magnetization is
        (1+0j, 1-0j, 0.).

        :param alpha: (...) - tf.complex64 - containing the complex flip angle
        :param magnetization: (#batch, ..., 3) - tf.complex64 - containing the normalized
                                        magnetization (Mx+jMy, Mx+jMy, Mz) per particle
        :return: rotated magnetization - (#batch, ..., 3) - tf.complex64
        """
        flip_angle = tf.abs(alpha)
        c_phase = tf.complex(0., tf.math.angle(alpha) + np_pi/2)
        exp_cphase = tf.exp(c_phase)
        exp_ncphase = tf.exp(-c_phase)
        sin_fa = tf.complex(tf.sin(flip_angle), 0.)
        cos_fa = tf.complex(tf.cos(flip_angle), 0.)
        sin_fa_2 = tf.complex(tf.sin(flip_angle / 2)**2, 0.)
        cos_fa_2 = tf.complex(tf.cos(flip_angle / 2)**2, 0.)

        row1 = tf.stack([cos_fa_2, tf.exp(2. * c_phase) * sin_fa_2, -1j * exp_cphase * sin_fa], -1)
        row2 = tf.stack([tf.exp(-2 * c_phase) * sin_fa_2, cos_fa_2, 1j * exp_ncphase * sin_fa], -1)
        row3 = tf.stack([-1j * exp_ncphase * sin_fa/2, 1j * exp_cphase * sin_fa/2, cos_fa], -1)
        rotation_operator = tf.stack([row1, row2, row3], axis=-2)
        return tf.einsum("...ij, ...j -> ...i", rotation_operator, magnetization)

    @staticmethod
    @tf.function(jit_compile=True, reduce_retracing=True)
    # pylint: disable=invalid-name
    def relax(T1: tf.Tensor, T2: tf.Tensor, dt: tf.Tensor, magnetization: tf.Tensor) -> tf.Tensor:
        """ Evaluates the relaxation over the given time interval dt for given relaxation times
        T1, T2 of specified magnetization.

        :param T1: (#batch, ) - tf.float32 - Longitudinal relaxation time in milliseconds
        :param T2: (#batch, ) - tf.float32 - Transversal relaxation time in milliseconds
        :param dt: ( ) - tf.float32 - time interval of relaxation in milliseconds
        :param magnetization: (#batch, #time, 3) - tf.complex64 - containing the normalized
                                magnetization (Mx+iMy, Mx+iMy, Mz) per particle
        """
        E1 = tf.complex(tf.exp(-dt / T1), 0.)
        E2 = tf.complex(tf.exp(-dt / T2), 0.)
        relax_operator = tf.stack([E2, tf.math.conj(E2), E1], axis=-1)
        longitudinal_summand = tf.stack([tf.zeros_like(E1), tf.zeros_like(E1), (1. - E1)], axis=-1)
        return relax_operator * magnetization + longitudinal_summand
