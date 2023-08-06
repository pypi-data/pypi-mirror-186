__all__ = ["T2starDistributionModel", "ConcomitantFields", "OffResonance"]

import abc
from typing import Tuple

import tensorflow as tf
import numpy as np


# pylint: disable=abstract-method
class BaseSubmodule(tf.Module):
    """ Base implementation for Bloch simulation submodules.


    :param name: Name of instances for subclasses
    :param device: name for device placing
    """
    required_quantities: Tuple[str, ...] = None

    def __init__(self, name: str, device: str):
        """

        :param name:
        :param device:
        """
        super().__init__(name)
        if device is None:
            if tf.config.get_visible_devices('GPU'):
                self.device = 'GPU'
            else:
                self.device = 'CPU'
        else:
            self.device = device

    @abc.abstractmethod
    def __call__(self, **kwargs) -> tf.Tensor:
        """ Evaluates the formula associated with the submodule instance

        :param kwargs:
        :return:
        """
        return tf.constant([0.])


# pylint: disable=abstract-method
class T2starDistributionModel(BaseSubmodule):
    # pylint: disable=anomalous-backslash-in-string
    """Submodule for Bloch simulations that implements T2 start weighting by accumulating a phase
    per particle. The particle properties should be assigned randomly according to a Lorentzian
    distribution. The phase difference is evaluated according to:

    .. math::

        \delta \phi = \omega_{T_2^\*} \delta t

    :param device: name for device placing
    """
    #: Tuple of names specifying the input quantities (datasets) to run this submodule
    required_quantities: Tuple[str, ...] = ("trajectories", "omega_t2s")

    def __init__(self, device: str = 'GPU'):
        super().__init__(name="t2star_distribution", device=device)

    @tf.function(jit_compile=True, reduce_retracing=True)
    def __call__(self, omega_t2s: tf.Tensor, dt: tf.Tensor, **kwargs) -> tf.Tensor:
        """Evaluates the module equation for given inputs.

        :param omega_t2s: (#particles, ) angular frequency contribution per particle
                            by T2star effect This should be sampled using a distribution as
                            implemented in cmrsim.utils.particle_properties.t2star_lorentzian.
        :param dt: (, ) angular frequency contribution per particle by T2star effect
        :return: (1, #particles, 1) phase increment per timestep due to T2star effects
        """
        with tf.device(self.device):
            tf.Assert(tf.shape(tf.shape(omega_t2s))[0] == 1,
                      ["Shape missmatch in T2star submodule", tf.shape(omega_t2s)])
            omega_t2s = tf.reshape(omega_t2s, [1, -1, 1])
            return omega_t2s * dt


# pylint: disable=abstract-method
class ConcomitantFields(BaseSubmodule):
    # pylint: disable=anomalous-backslash-in-string
    """Submodule for Bloch simulations that evaluates the concomitant field variation in
    z-direction (field variation in direction of the main magnetic field) at all particle positions
    contained in the trajectories according to:

    .. math::

        r = (x, y, z)^T \\
        G = (G_x, G_y, G_z)^T \\
        \Delta \phi = (\gamma \Delta t / 2B_0) \cdot
                    \left[ (G_x z + G_z x/2)^2 + (G_y z - G_z y/2)^2 \\right]

    :param gamma: gyromagnetic ratio in MHz/T (=1/ms/mT)
    :param b0: in T
    """
    required_quantities: Tuple[str] = ("gradient_wave_form", "trajectory", "dt")

    def __init__(self, gamma: float, b0: float, device: str = 'GPU'):
        """

        :param gamma: gyromagnetic ratio in MHz/T (=1/ms/mT)
        :param b0: in T
        """
        super().__init__(name="concomitant_fields", device=device)
        with tf.device(self.device):
            self._gamma = tf.Variable(gamma, shape=(), dtype=tf.float32, trainable=False)
            # b0 times 1000 to match the units in __call__
            self._b0 = tf.Variable(b0 * 1000, shape=(), dtype=tf.float32, trainable=False)

    # pylint: disable=too-many-locals, invalid-name
    @tf.function(jit_compile=False, reduce_retracing=True)
    def __call__(self, gradient_wave_form: tf.Tensor, trajectories: tf.Tensor, dt: tf.Tensor,
                 **kwargs) -> tf.Tensor:
        """Evaluates the module equation for given inputs.

        :param gradient_wave_form: (#reps, #time, 3) in mT/m
        :param trajectories: (Optional[#reps/1], #batch, #time, 3) in m
        :param dt: float -> delta time on which the gradient waveform is defined (usually ms)
        :return: phase increment per time-step (#reps, #batch, #time)
        """
        with tf.device(self.device):
            tf.Assert(tf.shape(tf.shape(gradient_wave_form))[0] == 3,
                      ["Shape missmatch in ConcomitantFields for specified gradient",
                       tf.shape(gradient_wave_form)])
            gradient_wave_form = tf.expand_dims(gradient_wave_form, axis=1)

            if tf.shape(tf.shape(trajectories))[0] == 3:
                trajectories = tf.expand_dims(trajectories, axis=0)
            tf.Assert(tf.shape(tf.shape(gradient_wave_form))[0] == 4,
                      ["Shape missmatch in ConcomitantFields for trajectories",
                      tf.shape(trajectories)])

            max_shape = tf.reduce_max(tf.stack([tf.shape(gradient_wave_form),
                                                tf.shape(trajectories)]), axis=0)[0:3]

            n_reps, n_batch, n_steps = tf.unstack(max_shape, axis=0)
            x, y, z = trajectories[...,0],trajectories[...,1],trajectories[...,2]
            gx, gy, gz = gradient_wave_form[...,0],gradient_wave_form[...,1],gradient_wave_form[...,2]
            omega = ((gx * z + gz * x / 2) ** 2 + (
                        gy * z - gz * y / 2) ** 2) / self._b0 / 2. * self._gamma
            phi = omega * dt
            return tf.reshape(phi, [n_reps, n_batch, n_steps])


# pylint: disable=abstract-method
class OffResonance(BaseSubmodule):
    # pylint: disable=anomalous-backslash-in-string
    """Submodule for Bloch simulations that evaluates the off-resonance phase according to:

    .. math::

        \delta \phi = \gamma \Delta B \delta t

    .. note::

        This function currently does not support jit-compilation due to reshape inside
        conditionals. (Tensorflow 2.9.1)

    :param gamma: in MHz/T (1/ms/mT)
    """
    required_quantities: Tuple[str] = ("off_res")

    def __init__(self, gamma: float, device: str = 'GPU'):
        """
        :param gamma: in MHz/T (1/ms/mT)
        """
        super().__init__(name="Off_resonance", device=device)
        with tf.device(self.device):
            self._gamma = tf.constant(gamma * 2. * np.pi, shape=(), dtype=tf.float32)

    @tf.function(jit_compile=False, reduce_retracing=True)
    def __call__(self, off_res: tf.Tensor, dt: tf.Tensor, **kwargs) -> tf.Tensor:
        """ Evaluates the phase increment per time-step for given off resonances.

        :param off_res: (Optional[#reps], #particles, Optional[#steps], 1) in mT. If #reps dimension
                        is not present, expands the first dimension to yield consistent output.
        :param dt: timestep in milliseconds
        :return: (#reps/1, #particles, #steps)
        """
        with tf.device(self.device):
            off_res = tf.squeeze(off_res, axis=[-1])
            n_dims = tf.squeeze(tf.shape(tf.shape(off_res)))
            if n_dims == 1:
                off_res = tf.reshape(off_res, [1, -1, 1])
            elif n_dims == 2:
                new_shape = tf.concat([[1, ], tf.shape(off_res)], axis=0)
                off_res = tf.reshape(off_res, new_shape)
            else:
                off_res = off_res

            tf.Assert(tf.shape(tf.shape(off_res))[0] == 3,
                      ["Shape missmatch in off-resonance submodule", tf.shape(off_res)])

            phi_per_step = off_res * self._gamma * dt
            return phi_per_step
