""" This modules contains signal model based signal modification due to Diffusion """
__all__ = ["GaussianDiffusionTensor"]

import tensorflow as tf

from cmrsim.analytic.contrast.base import BaseSignalModel


# pylint: disable=abstract-method, disable=anomalous-backslash-in-string
class GaussianDiffusionTensor(BaseSignalModel):
    """ Model based Gaussian diffusion contrast.

    Instantiates a module that evaluates the diffusion signal representation:

    .. math::

        F = \exp(-\mathbf{b}^T\mathbf{D}\mathbf{b})

    Assumes the b-vector to be the diffusion direction be scaled
    with the square-root of the b-value: :math:`\mathbf{b} = \sqrt{b}\mathbf{d}`

    Instead of two dimensions for direction and b-value just uses one dimension of scaled b-vectors.

    :param b_vectors: - (#directions * #bvalues, 3) in units sqrt(s/mm*2)
    :param expand_repetitions: See BaseSignalModel for explanation
    """

    required_quantities = ('diffusion_tensor', )

    def __init__(self, b_vectors: tf.Tensor, expand_repetitions: bool, **kwargs):
        """
        :param b_vectors: - (#directions * #bvalues, 3) in units sqrt(s/mm*2)
        :param expand_repetitions: See BaseSignalModel for explanation
        """
        super().__init__(name="dti_gauss", expand_repetitions=expand_repetitions, **kwargs)
        self.b_vectors = tf.Variable(b_vectors, shape=(None, 3), dtype=tf.float32, name='b_vectors')
        self.update()

    @tf.Module.with_name_scope
    def __call__(self, signal_tensor: tf.Tensor, diffusion_tensor: tf.Tensor, **kwargs)\
            -> tf.Tensor:
        """ Evaluates the diffusion operator.

        :param signal_tensor: (#voxel, #repetitions, #k-space-samples) last two dimensions can be 1
        :param diffusion_tensor: diffusion_tensor (#voxels, #repetitions, #k_space_samples, 3, 3)
        :return: - if expand_repetitions == True: (#voxel, #repetitions * #self.b_vectors,
                                                    #k-space-samples)
                 - if expand_repetitions == False: (#voxel, #repetitions, #k-space-samples)
        """
        with tf.device(self.device):
            # All Cases : --> repetitions-axis of argument diffusion_tensor must be either 1 or
            # equal to self.expansion_factor
            tf.Assert(tf.shape(diffusion_tensor)[1] == 1 or
                      tf.shape(diffusion_tensor)[1] == self.expansion_factor,
                      ["Shape missmatch for input argument diffusion_tensor"])

            input_shape = tf.shape(signal_tensor)
            k_space_axis_tiling = tf.cast((tf.floor(input_shape[2]/tf.shape(diffusion_tensor)[2])),
                                          tf.int32)

            # Case 1: expand-dimensions
            if self.expand_repetitions or self.expansion_factor == 1:
                exponent = tf.einsum('ni, vrkij, nj -> vrnk', self.b_vectors, diffusion_tensor,
                                     self.b_vectors)
                decay_factor = tf.cast(tf.exp(-exponent), tf.complex64)
                decay_factor = tf.tile(decay_factor, [1, 1, 1, k_space_axis_tiling])
                temp = tf.einsum('v...k, v...nk -> v...nk', signal_tensor, decay_factor)
                result = tf.reshape(temp, (input_shape[0], -1, input_shape[2]))
            # Case 2: repetition-axis of signal_tensor must match self.expansion_factor
            else:
                tf.Assert(input_shape[1] == self.expansion_factor,
                          ["Shape missmatch for input argument signal_tensor for case no-expand"])
                exponent = tf.einsum('...i, v...kij, ...j -> v...k',
                                     self.b_vectors, diffusion_tensor, self.b_vectors)
                decay_factor = tf.cast(tf.exp(-exponent), tf.complex64)
                decay_factor = tf.tile(decay_factor, [1, 1, k_space_axis_tiling])
                result = signal_tensor * decay_factor
            return result

    def update(self):
        super().update()
        self.expansion_factor = self.b_vectors.read_value().shape[0]
