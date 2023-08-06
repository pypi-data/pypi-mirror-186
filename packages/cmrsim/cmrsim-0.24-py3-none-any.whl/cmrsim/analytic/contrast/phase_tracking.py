""" This modules contains signal model based signal modification due to bulk-motion """
__all__ = ["PhaseTracking"]

import tensorflow as tf

from cmrsim.analytic.contrast.base import BaseSignalModel


# pylint: disable=abstract-method
class PhaseTracking(BaseSignalModel):
    # pylint: disable=anomalous-backslash-in-string
    """ Evalulates Phase accrual for pre-defined particle trajectories

    Phase calculation for a simple spatially constant gradient wave form and for
    moving particles according to:

    .. math::

        \phi(t) = \int \\vec{G}(t) \\cdot \\vec{r}(t) dt

    :param wave_form: (#repetition, #steps, [t, x, y, z]) - time and wave-form-grid
    :param gamma: Gyromagnetic ratio in rad/ms/mT
    """
    required_quantities = ('trajectory', )

    def __init__(self, expand_repetitions: bool,  wave_form: tf.Tensor,
                 gamma: float,  **kwargs):
        # pylint: disable=anomalous-backslash-in-string
        """
        :param wave_form: (#repetition, #steps, [t, x, y, z]) - time and wave-form-grid
        :param gamma: Gyromagnetic ratio in rad/ms/mT
        """
        super().__init__(expand_repetitions=expand_repetitions, name="phase_tracking", **kwargs)
        self.wave_form = tf.Variable(wave_form, shape=(None, None, 4),
                                     dtype=tf.float32, name='wave_form')
        self.n_steps = tf.Variable(0, shape=(), dtype=tf.int64, name="n_steps")
        self.gamma = tf.constant(gamma, dtype=tf.float32)
        self.expansion_factor = tf.shape(self.wave_form)[0]
        self.update()

    def __call__(self, signal_tensor: tf.Tensor, trajectory: tf.Tensor, **kwargs) -> tf.Tensor:
        """ Evaluates the phase integration for given trajectories

        :param signal_tensor: (#voxel, #repetitions, #k-space-samples) last two dimensions
                              can be 1
        :param trajectory: (#voxel, #repetitions, #k-space-samples, #time-steps, 3)
                            last dimension corresponds to (x, y, z) in meter
                            #time-steps must be the same as self.wave_form
        :return: - if expand_repetitions == True: (#voxel, #repetitions \* self.wave_form.shape[0],
                                                 #k-space-samples)
                 - if expand_repetitions == False: (#voxel, #repetitions, #k-space-samples)

        """
        with tf.device(self.device):
            tf.Assert(tf.shape(trajectory)[-2] == tf.shape(self.wave_form.read_value())[1],
                      ["[PhaseTracking] Wave-form and trajectory grid dont match!"])

            input_shape = tf.shape(signal_tensor)
            k_space_axis_tiling = tf.cast((tf.floor(input_shape[2]/tf.shape(trajectory)[2])),
                                          tf.int32)

            # trapezoidal integration
            tf.Assert(tf.shape(trajectory)[1] == 1 or
                      tf.shape(trajectory)[1] == self.expansion_factor,
                      ["Shape missmatch for input argument trajectory"])
            delta_t = self.wave_form[:, 1:, 0] - self.wave_form[:, 0:-1, 0]
            g_dot_r = tf.einsum('...ti, b...kti -> b...kt', self.wave_form[:, :, 1:], trajectory)
            phases = tf.reduce_sum(delta_t[tf.newaxis, :, tf.newaxis]
                                   * (g_dot_r[..., 1:] + g_dot_r[..., :-1]) / 2,
                                   axis=-1) * self.gamma
            complex_phase = tf.exp(tf.complex(0., phases))
            complex_phase = tf.tile(complex_phase, [1, 1, k_space_axis_tiling])

            # Case 1: expand-dimensions
            if self.expand_repetitions or self.expansion_factor == 1:
                temp = tf.einsum('vrk, vnk -> vrnk', signal_tensor, complex_phase)
                result = tf.reshape(temp, (input_shape[0], -1, input_shape[2]))
            # Case 2: repetition-axis of signal_tensor must match self.expansion_factor
            else:
                tf.Assert(input_shape[1] == self.expansion_factor,
                          ["Shape missmatch for input argument signal_tensor for case no-expand",
                           input_shape, self.expansion_factor])
                result = signal_tensor * complex_phase
            return result

    def update(self):
        super().update()
        self.n_steps.assign(self.wave_form.read_value().shape[1])
        self.expansion_factor = tf.shape(self.wave_form)[0]
