""" This module contains the implementation of a spatial Look-up based coil-sensitivity
weighting as signal module """
__all__ = ["CoilSensitivity", "BirdcageCoilSensitivities"]

from typing import Tuple, Union

import tensorflow as tf
import numpy as np

from cmrsim.analytic.contrast.base import LookUpTableModule


# pylint: disable=abstract-method
class CoilSensitivity(LookUpTableModule):
    """ Lookup for custom coil sensitivities

    Instantiates a Module that looks up coil sensitivities and multiplies the sensitivy
    value for the corresponding position to the signal vector when called.

    .. note::

        expand_repetitions is always set to True for coil-sensitivities, which means that
        the output hast a #repetions * #coils dimension on the repetitions axis

    :param coil_sensitivities: (X, Y, Z, #channels) with dtype complex64
    :param map_dimensions: (3, 2) -> [(xlow, xhigh), (ylow, yhigh), (zlow, zhigh)]
                            Extend of the map in scanner coordinate system. Used to sort
                            iso-chromat positions into bins. This is assumed to be the *length*
                            in meter in each spatial direction
    :param device: (str) Device on which all operations except for the look-up
                        are placed (default: GPU:0)
    :param device_lookup: (str) Device where the lookup table is places (defaults to CPU:0)

    """
    required_quantities = ('r_vectors', )
    _device2: str

    #: Spatial extend of the look up as: (3, 2) -> [(xlow, xhigh), (ylow, yhigh), (zlow, zhigh)]
    map_dimensions: tf.Variable  # float32
    #: Three dimensional look-up-table assuming a regular spacing derived from self.map-dimension
    look_up_map3d: tf.Variable  # float32

    def __init__(self, coil_sensitivities: Union['np.ndarray', tf.Tensor],
                 map_dimensions: np.ndarray, device: str = 'GPU:0', **kwargs):
        """
        :param coil_sensitivities: (X, Y, Z, #channels) with dtype complex64
        :param map_dimensions: (3, 2) -> [(xlow, xhigh), (ylow, yhigh), (zlow, zhigh)]
                                Extend of the map in scanner coordinate system. Used to sort
                                iso-chromat positions into bins. This is assumed to be the *length*
                                in meter in each spatial direction
        :param device: (str) Device on which all operations except for the look-up
                            are placed (default: GPU:0)
        :param device_lookup: (str) Device where the lookup table is places (defaults to CPU:0)
        """
        coils_real = tf.math.real(coil_sensitivities)
        coils_imag = tf.math.imag(coil_sensitivities)
        coils = tf.cast(tf.stack([coils_real, coils_imag], axis=-1), dtype=tf.float32)
        coils = tf.reshape(coils, [*coil_sensitivities.shape[:-1], -1])
        super().__init__(look_up_map3d=coils,
                         map_dimensions=np.array(map_dimensions, dtype=np.float32),
                         name="coil_sensitivities",
                         device=device,
                         expand_repetitions=True)
        self._device2 = device
        self.expansion_factor = coils.shape[-1] // 2

    def update(self):
        super().update()
        self.expansion_factor = self.look_up_map3d.read_value().shape[-1] // 2

    # pylint: disable=signature-differs, too-many-locals
    def __call__(self, signal_tensor: tf.Tensor, r_vectors: tf.Tensor, **kwargs) -> tf.Tensor:
        """Evaluation of coil-sensitivity weighting:

        .. math::

                M_{xy}^{n}(\\vec{r}) = M_{xy}(\\vec{r}) * C^{n}(\\vec{r})

        :param signal_tensor:
        :param r_vectors: (#voxels, #repetitions, #samples, 3)
        :return:
        """
        with tf.device(self._device2):
            input_shape = tf.shape(signal_tensor)
            tf.Assert(tf.shape(r_vectors)[1] == 1 or
                      tf.shape(r_vectors)[1] == input_shape[1],
                      ["Shape missmatch for input argument r_vectors "
                       "with respect to signal_tensor"])

            # sensitivity_factors shape: (#voxels, #repetitions, #samples, n_channels),
            # with axis 0,1,2 taken from r
            n_particles, n_reps, n_ksamples, _ = tf.unstack(tf.shape(r_vectors))
            with tf.name_scope(self.name + "/look_up/"):
                r_flat = tf.reshape(r_vectors, [-1, 3])
                # sense_factors = super().__call__(r_vectors=r_flat)
                sense_factors = self.linear_interpolation(r_vectors=r_flat)
                sense_factors = tf.reshape(sense_factors, [n_particles, -1, 2])
                sense_factors = tf.complex(sense_factors[:, :, 0], sense_factors[:, :, 1])
                sensitivity_factors = tf.reshape(sense_factors,
                                                 [n_particles, n_reps, n_ksamples, -1])

            # In case all repetitions have the same position, reuse the sensitivity factors
            lookup_shape = tf.shape(sensitivity_factors)
            k_space_axis_tiling = tf.cast(
                                    tf.reduce_max([tf.floor(input_shape[2] / lookup_shape[2]), 1]),
                                    tf.int32)

            temp = tf.tile(signal_tensor[..., tf.newaxis],
                           [1, 1, k_space_axis_tiling, self._n_channels//2])
            product = tf.multiply(temp, sensitivity_factors)

            # Flatten the new channels to repetition axis
            product = tf.transpose(product, [0, 1, 3, 2])
            new_shape = tf.stack([input_shape[0], input_shape[1] * self._n_channels//2, -1], axis=0)

            result = tf.reshape(product, new_shape)
            return result

    def lookup_complex_coil_factors(self, r_vectors: tf.Tensor):
        """ Looks the sensitivity values for all coils at specified locations.
        
        :param r_vectors: [..., 3] dtype: tf.float32
        :return: coil_factors [..., n_coils] dtype: tf.complex64
        """
        old_shape = tf.shape(r_vectors)
        new_shape = tf.concat([old_shape[:-1], [self.expansion_factor, ]], axis=0)
        r_flat = tf.reshape(r_vectors, [-1, 3])
        sense_factors = self.linear_interpolation(r_vectors=r_flat)
        sense_factors = tf.reshape(sense_factors, [-1, self.expansion_factor, 2])
        sense_factors = tf.complex(sense_factors[..., 0], sense_factors[..., 1])
        sense_factors = tf.reshape(sense_factors, new_shape)
        return sense_factors

    @property
    # pylint: disable=invalid-name
    def coil_maps(self):
        """ Property returning the complex coil-sensitivities"""
        temp = self.look_up_map3d.read_value()
        b, x, y, z, ch = tf.unstack(tf.shape(temp))
        if b == 1:
            temp = tf.reshape(temp, [x, y, z, ch//2, 2])
        else:
            temp = tf.reshape(temp, [b, x, y, z, ch // 2, 2])
        return tf.complex(temp[..., 0], temp[..., 1])

    @coil_maps.setter
    def coil_maps(self, coil_sensitivities: tf.Tensor):
        """ Property setting the complex coil-sensitivities with shape ([b], x, y, z, ch) """
        coils_real = tf.math.real(coil_sensitivities)
        coils_imag = tf.math.imag(coil_sensitivities)
        coils = tf.cast(tf.stack([coils_real, coils_imag], axis=-1), dtype=tf.float32)
        coils = tf.reshape(coils, [*coil_sensitivities.shape[1:-1], -1])
        self.look_up_map3d.assign(coils)

    @classmethod
    def from_3d_birdcage(cls, map_shape: Union['np.ndarray', tf.Tensor, Tuple],
                         map_dimensions: np.ndarray, relative_coil_radius: float = 1.5,
                         device: str = 'CPU:0', **kwargs):
        """Lookup for ideal bird-cage coil sensitivities.

        .. note::

            expand_repetitions is always set to True for coil-sensitivities, which means that
            the output hast a #repetions * #coils dimension on the repetitions axis

        :param map_shape: (X, Y, Z, #coils) array shape of the resulting coil-maps
        :param map_dimensions: (3, 2) -> [(xlow, xhigh), (ylow, yhigh), (zlow, zhigh)] Extend of
        :param relative_coil_radius: distance of the birdcage ring from the map center
            the map in scanner coordinate system. Used to sort iso-chromat positions into bins.
            This is assumed to be the *length* in meter in each spatial direction
        :param device: (str) Device on which all operations except for the look-up are
                        placed (default: GPU:0)
        :param device_lookup: (str) Device where the lookup table is places (defaults to CPU:0)

        """
        nx, ny, nz, nc = map_shape
        c, z, y, x = np.mgrid[:nc, :nz, :ny, :nx]
        coilx = relative_coil_radius * np.cos(c * (2 * np.pi / nc))
        coily = relative_coil_radius * np.sin(c * (2 * np.pi / nc))
        coilz = np.floor(c / nc) - 0.25  # * nc
        coil_phs = -(c + np.floor(c / nc)) * (2 * np.pi / nc)

        x_co = (x - nx / 2.0) / (nx / 2.0) - coilx
        y_co = (y - ny / 2.0) / (ny / 2.0) - coily
        z_co = (z - nz / 2.0) / (nz / 2.0) - coilz
        rr = (x_co ** 2 + y_co ** 2 + z_co ** 2) ** 0.5
        phi = np.arctan2(x_co, -y_co) + coil_phs
        out = (1 / rr) * np.exp(1j * phi)

        rss = sum(abs(out) ** 2, 0) ** 0.5
        out /= rss
        coil_maps3d = tf.constant(out.transpose(3, 2, 1, 0), dtype=tf.complex64)
        return cls(coil_maps3d, map_dimensions, device, **kwargs)


class BirdcageCoilSensitivities(CoilSensitivity):
    """ Lookup for ideal bird-cage coil sensitivities.

    Instantiates a Module that looks up coil sensitivities and multiplies the sensitivity
    value for the corresponding position to the signal vector when called. The coil
    sensitivities are constructed as ideal birdcage-sensitivities.

    .. note::

        expand_repetitions is always set to True for coil-sensitivities, which means that
        the output hast a #repetions * #coils dimension on the repetitions axis

    :param map_shape: (X, Y, Z, #coils) array shape of the resulting coil-maps
    :param relative_coil_radius: distance of the birdcage ring from the map center
    :param map_dimensions: (3, 2) -> [(xlow, xhigh), (ylow, yhigh), (zlow, zhigh)] Extend of
        the map in scanner coordinate system. Used to sort iso-chromat positions into bins.
        This is assumed to be the *length* in meter in each spatial direction
    :param device: (str) Device on which all operations except for the look-up are
                    placed (default: GPU:0)
    :param device_lookup: (str) Device where the lookup table is places (defaults to CPU:0)
    """

    required_quantities = ('r_vectors', )

    def __init__(self, map_shape: Union['np.ndarray', tf.Tensor, Tuple],
                 map_dimensions: np.ndarray,
                 relative_coil_radius: float = 1.5, device: str = 'CPU:0',
                 **kwargs):
        """
        :param map_shape: (X, Y, Z, #coils) array shape of the resulting coil-maps
        :param relative_coil_radius: distance of the birdcage ring from the map center
        :param map_dimensions: (3, 2) -> [(xlow, xhigh), (ylow, yhigh), (zlow, zhigh)] Extend of
            the map in scanner coordinate system. Used to sort iso-chromat positions into bins.
            This is assumed to be the *length* in meter in each spatial direction
        :param device: (str) Device on which all operations except for the look-up are
                        placed (default: GPU:0)
        :param device_lookup: (str) Device where the lookup table is places (defaults to CPU:0)
        """
        cmaps = self._birdcage_maps3d(map_shape, relative_coil_radius)
        super().__init__(cmaps, map_dimensions, device, **kwargs)

    @staticmethod
    # pylint: disable=invalid-name,too-many-locals
    def _birdcage_maps3d(shape: Tuple[int, int, int, int], r: float = 1.5):
        """Simulates ideal birdcage coil sensitivities.

        :param shape: Tuple(nx, ny, nz, #coils) Volume
        :param r: relative coil radius
        :return: Coil sensitivities (X, Y, Z, #channels) of dtype complex64
        """
        nx, ny, nz, nc = shape
        c, z, y, x = np.mgrid[:nc, :nz, :ny, :nx]
        coilx = r * np.cos(c * (2 * np.pi / nc))
        coily = r * np.sin(c * (2 * np.pi / nc))
        coilz = np.floor(c / nc) - 0.25  # * nc
        coil_phs = -(c + np.floor(c / nc)) * (2 * np.pi / nc)

        x_co = (x - nx / 2.0) / (nx / 2.0) - coilx
        y_co = (y - ny / 2.0) / (ny / 2.0) - coily
        z_co = (z - nz / 2.0) / (nz / 2.0) - coilz
        rr = (x_co ** 2 + y_co ** 2 + z_co ** 2) ** 0.5
        phi = np.arctan2(x_co, -y_co) + coil_phs
        out = (1 / rr) * np.exp(1j * phi)

        rss = sum(abs(out) ** 2, 0) ** 0.5
        out /= rss
        return tf.constant(out.transpose(3, 2, 1, 0), dtype=tf.complex64)
