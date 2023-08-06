""" This module contains the analytical solutions to the bloch equation for commonly used
sequences """
__all__ = ["SpinEcho", "SaturationRecoveryGRE", "BSSFP"]

from typing import Union, Sequence

import tensorflow as tf
import numpy as np

from cmrsim.analytic.contrast.base import BaseSignalModel


# pylint: disable=abstract-method, disable=anomalous-backslash-in-string
class SpinEcho(BaseSignalModel):
    # pylint: disable=invalid-name
    """ Analytical Solution operator for a Single echo Spin echo sequence

    Evaluates the signal for the simple Spin-Echo sequence:

    .. math::

        M_{xy} = M_z \cdot e^{- TE / T_2} (1 - e^{-TR / T1})

    :raises: ValueError if the arguments echo and repetition time do not have the same length

    :param echo_time: in milliseconds
    :param repetition_time: in milliseconds
    :param expand_repetitions: See BaseSignalModel for explanation
    """
    required_quantities = ('T1', 'T2')
    #: Echo time in ms
    TE: tf.Variable = None
    #: Repetition time in ms
    TR: tf.Variable = None

    def __init__(self, echo_time: Union[float, tf.Tensor], repetition_time: Union[float, tf.Tensor],
                 expand_repetitions: bool, **kwargs):
        """
        :param echo_time: in milliseconds
        :param repetition_time: in milliseconds
        :param expand_repetitions: See BaseSignalModel for explanation
        """
        if isinstance(echo_time, (float, int)):
            echo_time = tf.constant(echo_time, shape=(1, ), dtype=tf.float32)
        if isinstance(repetition_time, (float, int)):
            repetition_time = tf.constant(repetition_time, shape=(1, ), dtype=tf.float32)

        if echo_time.shape[0] != repetition_time.shape[0]:
            raise ValueError("Arguments echo_time and repetition_time must have same number "
                             f"of elements. Got {echo_time.shape} and {repetition_time.shape}")

        super().__init__(expand_repetitions=expand_repetitions, name="spin_echo", **kwargs)
        self.TE = tf.Variable(echo_time, shape=(None, ), dtype=tf.float32, name='TE')
        self.TR = tf.Variable(repetition_time, shape=(None, ), dtype=tf.float32, name='TR')
        self.expansion_factor = self.TE.read_value().shape[0]
        self.update()

    @tf.Module.with_name_scope
    def __call__(self, signal_tensor: tf.Tensor, T1: tf.Tensor, T2: tf.Tensor, **kwargs):  # noqa
        """ Evaluates spin echo operator

        :param signal_tensor: (#batch, #voxel, #repetitions, #k-space-samples)
                                last two dimensions can be 1
        :param T1: (#batch, #voxel, 1, 1) in milliseconds
        :param T2: (#batch, #voxel, 1, 1) in milliseconds
        :return:
        """
        with tf.device(self.device):
            # All Cases --> repetitions-axis of argument T1 and T2 must be either 1 or equal to
            # self.expansion_factor
            tf.Assert(tf.shape(T1)[1] == 1 or tf.shape(T1)[1] == self.expansion_factor,
                      ["Shape missmatch for input argument T1"])
            tf.Assert(tf.shape(T2)[1] == 1 or tf.shape(T2)[1] == self.expansion_factor,
                      ["Shape missmatch for input argument T2"])

            te = tf.abs(tf.reshape(self.TE, (1, -1, 1)))
            tr = tf.abs(tf.reshape(self.TR, (1, -1, 1)))

            t1_term = 1 - tf.exp(-tf.math.divide_no_nan(tr, T1))
            t2_term = tf.exp(-tf.math.divide_no_nan(te, T2))
            factor = tf.cast(t1_term * t2_term, tf.complex64)

            input_shape = tf.shape(signal_tensor)
            # Case 1: expand-dimensions
            if self.expand_repetitions or self.expansion_factor == 1:
                temp = tf.einsum('vrk, vnk -> vrnk', signal_tensor, factor)
                result = tf.reshape(temp, (input_shape[0], -1, input_shape[2]))
            # Case 2: repetition-axis of signal_tensor must match self.expansion_factor
            else:
                tf.Assert(input_shape[1] == self.expansion_factor,
                          ["Shape missmatch for input argument signal_tensor for case no-expand"])
                result = tf.einsum('vrk, vrk -> vrk', signal_tensor, factor)
            return result

    def update(self):
        assert all((s1 == s2 for s1, s2 in zip(self.TE.read_value().shape,
                                               self.TR.read_value().shape)))
        self.expansion_factor = self.TE.read_value().shape[0]


# pylint: disable=abstract-method, disable=anomalous-backslash-in-string
class BSSFP(BaseSignalModel):
    """ Evaluates bssfp steady state contrast for :math:`TE/TR \\approx 1/2` according to:
    ` Ganter, MRM 56:687 (2006)`

    .. math::

        M(x \\cdot TR) = E_2^x e^{ix\\theta} \\left[ (E_2^{\prime})^x
         [1 + e^{i\\theta} E_2^{\\prime} A]^{-1} + (E_2^{\prime})^{1-x} e^{-i\\theta}
         \\Lambda/E_2 [1 + e^{-i\\theta} E_2^{\\prime} A]^{-1} \\right]

    Off-resonance theta results in banding according to the alternating RF phase scheme:

    .. dropdown:: Off-resonance Banding

        .. image:: ../../_static/api/bssfp_banding.png

    :raises: ValueError if the arguments echo, repetition time and flip angle do not have the
            same length

    :param flip_angle: in degree
    :param echo_time: im ms
    :param repetition_time: in ms
    :param expand_repetitions: See BaseSignalModel for explanation
    """
    # pylint: disable=invalid-name
    required_quantities = ('T1', 'T2', 'T2star', 'off_res')
    #: Echo time in ms
    TE: tf.Variable = None
    #: Repetition time in ms
    TR: tf.Variable = None
    #: Flip angle in degree
    FA: tf.Variable = None

    def __init__(self, flip_angle: Union[int, float, Sequence],
                 echo_time: Union[int, float, Sequence],
                 repetition_time: Union[int, float, Sequence],
                 expand_repetitions: bool, **kwargs):
        """
        :param flip_angle: in degree
        :param echo_time: im ms
        :param repetition_time: in ms
        :param expand_repetitions: See BaseSignalModel for explanation
        """
        if isinstance(echo_time, (float, int)):
            echo_time = tf.constant(echo_time, shape=(1, ), dtype=tf.float32)
        if isinstance(repetition_time, (float, int)):
            repetition_time = tf.constant(repetition_time, shape=(1, ), dtype=tf.float32)
        if isinstance(flip_angle, (float, int)):
            flip_angle = tf.constant(flip_angle, shape=(1, ), dtype=tf.float32)

        if len(echo_time) != len(repetition_time) or len(echo_time) != len(flip_angle):
            raise ValueError("Arguments echo_time and repetition_time must have same number "
                             f"of elements. Got {echo_time.shape} and {repetition_time.shape}")

        super().__init__(expand_repetitions=expand_repetitions, name="bssfp", **kwargs)
        self.FA = tf.Variable(flip_angle/180. * np.pi, shape=(None, ), dtype=tf.float32, name='FA')
        self.TE = tf.Variable(echo_time, shape=(None, ), dtype=tf.float32, name='TE')
        self.TR = tf.Variable(repetition_time, shape=(None, ), dtype=tf.float32, name='TR')
        self.expansion_factor = self.FA.read_value().shape[0]

    # pylint: disable=too-many-arguments
    def __call__(self, signal_tensor: tf.Tensor, T1: tf.Tensor, T2: tf.Tensor,
                 T2star: tf.Tensor, off_res: tf.Tensor, **kwargs):
        # pylint: disable=invalid-name, too-many-locals,
        """ Evaluates the signal Equation.

        :param signal_tensor: (#voxel, #repetitions, #k-space-samples) last two dimensions can be 1
        :param T1: in ms
        :param T2: in ms
        :param T2star: in ms
        :param off_res: b0 inhomogeneity in rad/ms (angular frequency difference)
        :return:  (#voxel, #repetitions, #k-space-samples)
        """

        #  phase in radians acquired over one TR due to off-resonance
        theta = off_res * tf.reshape(self.TR, [1, -1, 1])

        T2p = 1. / (1. / T2star - 1./T2)
        E1 = tf.exp(-tf.reshape(self.TR, [1, -1, 1]) / T1)
        E2 = tf.exp(-tf.reshape(self.TR, [1, -1, 1]) / T2)
        E2p = tf.exp(-tf.reshape(self.TR, [1, -1, 1]) / T2p)

        # Equation 6
        a = 1 - E1 * tf.math.cos(tf.reshape(self.FA, [1, -1, 1]))
        b = tf.math.cos(tf.reshape(self.FA, [1, -1, 1])) - E1

        # Equation 5
        Lambda = (a - E2**2 * b - tf.sqrt((a**2 - E2**2 * b**2) * (1 - E2**2))) / (a - b)

        # Equation 3
        A = ((a + b) * E2 / 2.) / (a - Lambda * (a - b) / 2.)

        # Equation 7/8
        Mxy = (1 - E1) / (a + b * Lambda) * tf.math.sin(tf.reshape(self.FA, [1, -1, 1]))
        Mxy = tf.complex(0., -Mxy)

        # Text right before Equation 10
        x = tf.reshape(self.TE / self.TR, [1, -1, 1])

        # Lorentzian distribution from Equation 13
        factor_1 = tf.math.exp(tf.complex(0., x * theta)) * tf.cast(E2 ** x, tf.complex64)

        # Equation 14
        exp_theta = tf.exp(tf.complex(0., theta))
        exp_theta_m = tf.exp(tf.complex(0., -theta))
        E2p_x = tf.cast(E2p ** x, tf.complex64)
        E2p_A = tf.cast(E2p * A, tf.complex64)

        summand_1 = E2p_x / (1. + exp_theta * E2p_A)
        factor_21 = tf.cast(E2p ** (1. - x) * (Lambda / E2), tf.complex64) * exp_theta_m
        factor_22 = 1. + exp_theta_m * E2p_A

        bfe = factor_1 * (summand_1 + factor_21 / factor_22) * Mxy
        return bfe * signal_tensor


# pylint: disable=abstract-method
class SaturationRecoveryGRE(BaseSignalModel):
    # pylint: disable=invalid-name
    """ Analytical solution for a Saturation Recovery GRE sequence used in
    1st-pass-perfusion imaging

    Evaluates the signal model for a saturation recovery spoiled gradient echo sequence.
    This modules assumes the cartesian line-by line k-space sampling. This yields the signal
    equation for a single k-space line:

    .. math::

        m_{xy} = \\rho(r) \\left[(1 - e^{-T_D \cdot R_1})
        (\cos(\\alpha)e^{-T_R \cdot R_1})^{n-1} + (1-e^{-T_R \cdot R_1})
         \\frac{1 - (\cos(\\alpha)e^{-T_R \cdot R_1})^{n-1}}
         {1 - (\cos(\\alpha)e^{-T_R \cdot R_1})} \\right]

    Where T_D is the saturation_delay, n is the number of profiles left until the
    k-space-center, alpha is the flip_angle and TR is the repetition time.

    for more info refer to https://gitlab.ethz.ch/jweine/cmrsim/-/issues/62

    **Note** This module assumes, that the keyword argument 'segment_index' is used in
    \_\_call\_\_`, such that each segment contains all k-space point acquired in one TR,
    otherwise the signal equation does not hold!

    :param repetition_time: in ms
    :param flip_angle: in degree
    :param saturation_delay: (float) time in ms from saturation pulse (t=0.) to the time of
                                    acquisition of the k-space center profile.
    :param n_profiles_to_k0: (int) profiles (=k-space lines) prior to acquisition of k0
    """

    required_quantities = ('T1', )
    #: Echo time in ms
    TE: tf.Variable = None
    #: Repetition time in ms
    TR: tf.Variable = None

    def __init__(self, repetition_time: Union[float, tf.Tensor],
                 flip_angle: Union[float, tf.Tensor], saturation_delay: float,
                 n_profiles_to_k0: int, expand_repetitions: bool, **kwargs):
        # pylint: disable=anomalous-backslash-in-string
        """

        :param repetition_time: in ms
        :param flip_angle: in degree
        :param saturation_delay: (float) time in ms from saturation pulse (t=0.) to the time of
                                        acquisition of the k-space center profile.
        :param n_profiles_to_k0: (int) profiles (=k-space lines) prior to acquisition of k0
        """
        super().__init__(expand_repetitions=expand_repetitions,
                         name="saturation_recovery_gre", **kwargs)
        self.TR = tf.Variable(repetition_time, dtype=tf.float32, name='TR')
        self.flip_angle = tf.Variable(flip_angle, dtype=tf.float32, name='flip_angle')
        self.saturation_delay = tf.Variable(saturation_delay, shape=(), dtype=tf.float32, name='TD')
        self._n_profiles_to_k0 = tf.Variable(n_profiles_to_k0, shape=(), dtype=tf.float32,
                                             name='n_tok0')
        self.expansion_factor=1

    def __call__(self, signal_tensor: tf.Tensor, T1: tf.Tensor, segment_index: tf.Tensor = 0.,
                 **kwargs):  # noqa
        # pylint: disable=invalid-name
        """ Evaluation of SaturationRecoveryGRE equation"""
        with tf.device(self.device):
            n = tf.maximum(tf.math.floor(self._n_profiles_to_k0 -
                                         tf.cast(segment_index, tf.float32)), 1.)
            a = tf.math.exp(- self.TR / T1)
            cos_alpha = tf.math.cos(self.flip_angle.read_value() / 180 * \
                                    tf.constant(np.pi, dtype=tf.float32))
            b = cos_alpha * a
            c = 1 - tf.math.exp(-self.saturation_delay / T1)
            d = tf.pow(b, n - 1.)
            factor = c * d + (1 - a) * (1 - d) / (1 - b)
            return signal_tensor * tf.cast(factor, tf.complex64)

    def update(self):
        return
