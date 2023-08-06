""" This module contains the base implementation for all signal-process building blocks. """
__all__ = ["BaseSignalModel", "LookUpTableModule"]

from abc import abstractmethod
from typing import Tuple, Optional
import itertools

import tensorflow as tf

import numpy as np


class BaseSignalModel(tf.Module):
    # pylint: disable=anomalous-backslash-in-string

    """ All concrete implementations of modules that modify the transverse magnetization need to be
    sub-classed from this abstract class. All sub-classes must implement the `__call__` method

    Class to inherit every module from, that multiplies a term \Psi to the integrand in
    the fourier transform:

        .. math::

            s(\mathbf{k}(t)) = \int_V \mathrm{d}V m( \mathbf{r} , 0)
            \Psi(\mathbf{r}, t) e^{-2\pi j \mathbf{k}(t) \cdot \mathbf{r}}


    The purpose of this parent class is to ensure the attributes '' required quantities field
    is set and the \_\_call\_\_ method is implemented

    :param expand_repetitions: Sets the self.expand_repetitions attribute
    :param name: Module name
    :param device: Device on which the graph of this module is executed.
                Defaults to GPU:0 (CPU:0 if no GPU is available)
    """
    #: Tuple of names specifying the input quantities that must be passed as keyword-arguments to
    # the __call__ method of the operator instance.
    required_quantities: Tuple[str] = ()
    #: Name of the device that the module is executed on (defaults to: GPU:0 - CPU:0)
    device: str = None
    #: Corresponds to the number of different parameter sets, for which this operator is evaluated.
    # Dtype = tf.int32
    expansion_factor: tf.Variable
    #: Is used to determine wether the repetitions-axis of the signal tensor is expanded by a factor
    # of self.expansion_factor or not. Expanding the axis means that for every handed in repetition
    # all parameter-sets (corresponding to the expansion factor) of are evaluated in __call__.
    # If set to False, the __call__ function assumes that self.expansion factor is equal to the
    # dimension of the signal_tensor given to the __call__ method. Dtype = tf.bool
    expand_repetitions: tf.Variable

    def __init__(self, expand_repetitions: bool, name: str = None, device: str = None):
        # pylint: disable=anomalous-backslash-in-string
        """
        :param expand_repetitions: Sets the self.expand_repetitions attribute
        :param name: Module name
        :param device: Device on which the graph of this module is executed.
                        Defaults to GPU:0 (CPU:0 if no GPU is available)
        """
        if device is None:
            if tf.config.get_visible_devices('GPU'):
                self.device = 'GPU:0'
            else:
                self.device = 'CPU:0'
        else:
            self.device = device

        self.expansion_factor = tf.Variable(1, shape=(), dtype=tf.int32)
        self.expand_repetitions = tf.Variable(expand_repetitions, shape=(), dtype=tf.bool)
        super().__init__(name=name)

    @abstractmethod
    def __call__(self, signal_tensor, **kwargs):
        """Defines the calculation which represent the factor multiplied to the integrand in the
        signal equation. Tensors and arguments that are listed in the self._required_quantities
        field are automatically passed via **kwargs** if the module is inserted into a
        :code:`CompositeSignalModel`.

        :param signal_tensor: tf.complex64 - Tensor of points representing local magnetization
            multiplied with factors of previously executed modules
        :param kwargs: all available tensors representing quantities at given points
        :return: signal_tensor * (defined_factor)
        """
        # with tf.device(self.device):
        #   Calculate factor.....
        #   factor = ....
        #   pass
        # return  # signal_tensor * factor

    @abstractmethod
    def update(self):
        """ Can be left empty if changing the Variables in the signal module does not affect the
         shape of the tensors processed by it. In other cases, e.g. when the expansion factor
         changes on Variable change, this needs to be mirrored here.

         Function is called before every simulation execute.
         """
        return

    def check_inputs(self, **kwargs):
        # pylint: disable=anomalous-backslash-in-string
        """ This method is meant to be called by CompositeSignalModel and asserts that all
        required_quantities are passed in kwargs during graph construction.

        :raises: ValueError if \*\*kwargs is missing a specified required quantity
        """
        key_check = [key in kwargs for key in self.required_quantities]
        if not all(key_check):
            raise ValueError(f"For calling the Signal model {self.name} following keyword arguments"
                             f" are necessary: {self.required_quantities} while these were "
                             f"given: {key_check}")


# pylint: disable=W0223,R0902
class LookUpTableModule(BaseSignalModel):
    """Base implementation of a signal process that involves a spatial look-up in
    a T + 3D + channel map.

    :param look_up_map3d: (X, Y, Z, #channels,) where X, Y, Z are the number of bins of the
                           3D map.
                           Or if temporal information is present: (t, X, Y, Z, #channels,)
    :param map_dimensions: (3, 2) -> [(xlow, xhigh), (ylow, yhigh), (zlow, zhigh)]
                           Extend of the map in scanner coordinate system. Used to sort
                           iso-chromat positions into bins. This is assumed to be the 'length'
                           in meter in each spatial direction of
    :param name: defines Module name-scope
    :param expand_repetitions: See BaseSignalModel for explanation
    :param kwargs: - device: str defaults to CPU:0
    """
    required_quantities = ('r_vectors',)
    #: Data type of the lookup map
    map_dtype: tf.DType
    #: Spatial extend of the look up as: (3, 2) -> [(xlow, xhigh), (ylow, yhigh), (zlow, zhigh)]
    map_dimensions: tf.Variable  # float32
    #: Three dimensional look-up-table assuming a regular spacing derived from self.map-dimension
    look_up_map3d: tf.Variable  # float32

    _bins: tf.Tensor  # float32
    _n_channels: tf.Tensor  # int32

    def __init__(self, look_up_map3d: np.ndarray, map_dimensions: np.ndarray,
                 name: Optional[str] = None, expand_repetitions: bool = True,
                 **kwargs):
        """
        :param look_up_map3d: (X, Y, Z, #channels,) where X, Y, Z are the number of bins of the
                               3D map.
                               Or if temporal information is present: (t, X, Y, Z, #channels,)
        :param map_dimensions: (3, 2) -> [(xlow, xhigh), (ylow, yhigh), (zlow, zhigh)]
                               Extend of the map in scanner coordinate system. Used to sort
                               iso-chromat positions into bins. This is assumed to be the 'length'
                               in meter in each spatial direction of
        :param name: defines Module name-scope
        :param expand_repetitions: See BaseSignalModel for explanation
        :param kwargs: - device: str defaults to CPU:0
        """
        super().__init__(expand_repetitions=expand_repetitions, name=name,
                         device=kwargs.get('device', 'CPU:0'))

        with tf.device(self.device):

            self.map_dimensions = tf.Variable(tf.constant(map_dimensions), shape=(3, 2),
                                              dtype=tf.float32, trainable=False,
                                              name='map_dimension')
            if len(look_up_map3d.shape) == 4:
                look_up_map3d = look_up_map3d[np.newaxis]

            self.look_up_map3d = tf.Variable(look_up_map3d, dtype=look_up_map3d.dtype,
                                             shape=(None, None, None, None, None), trainable=False,
                                             name='look_up_map3d')
            self.index_additions = tf.constant(list(itertools.product((0, 1), (0, 1), (0, 1)))
                                               )[tf.newaxis]
            self.update()

            self._r_min = tf.cast(self.map_dimensions[tf.newaxis, :, 0], tf.float32)
            self._r_extend = tf.cast(self.map_dimensions[tf.newaxis, :, 1]
                                     - self.map_dimensions[tf.newaxis, :, 0], tf.float32)

    def update(self):
        """ If the look-up map is changed, the look-up parameters have to be updated as well """
        super().update()
        new_lookup_map = self.look_up_map3d.read_value()
        self._bins = tf.cast(tf.shape(new_lookup_map)[1:-1]-1, tf.float32)
        self._n_channels = tf.shape(new_lookup_map)[-1]
        self.map_dtype = tf.as_dtype(self.look_up_map3d.dtype)

    def __call__(self, r_vectors, method: str = "nearest", **kwargs):
        """ Evaluates look up of stored values for given positional vectors.

        :param r_vectors: (#batch, 3)
        :param method: one of ["nearest", "trilinear"] determines which interpolation strategy
                    is used for look-up
        :param kwargs: placeholder to allow arbitrary keyword arguments
        :return:
        """
        if method.lower() == "nearest":
            values = self.nearest_neighbour(r_vectors)
        elif method.lower() == "trilinear":
            values = self.linear_interpolation(r_vectors)
        else:
            raise ValueError(f"Unknown look-up method '{method.lower()}' not "
                             f"in implemented methods ['nearest', 'trilinear']")
        return values

    def get_indices(self, r_vectors):
        """ Rounds r_vectors to map-resolution to get look-up indices that can be used to gather
        the corresponding values
        :param r_vectors: ()
        :return:
        """
        relative_r_vectors = (r_vectors - self._r_min) / self._r_extend * self._bins
        r_as_bin_indices = tf.cast(tf.math.floor(relative_r_vectors), tf.int32)
        r_as_bin_indices = tf.minimum(r_as_bin_indices, tf.shape(self.look_up_map3d)[1:-1] - 1)
        r_as_bin_indices = tf.maximum(r_as_bin_indices, tf.zeros((3,), dtype=tf.int32))
        return r_as_bin_indices

    @tf.function(jit_compile=False, reduce_retracing=True)
    # pylint: disable=unused-argument
    def nearest_neighbour(self, r_vectors: tf.Tensor,
                          batch_index: tf.Tensor = tf.constant([0, ], dtype=tf.int32),
                          **kwargs) -> tf.Tensor:
        # pylint: disable=anomalous-backslash-in-string
        """Rounds r\_vectors to map-resolution to get look-up indices and gathers the required
        values from the stored 3D table.

        :param r_vectors: (-1, 3) in meter
        :param batch_index: (#batch) indices of the first dimension (T) used for spatial lookup
        :return: (-1, self._n_channels) map values at nearest neighbour locations
        """
        with tf.name_scope("nearest_neighbour_lookup") as scope:
            with tf.device(self.device):
                r_as_bin_indices = self.get_indices(r_vectors)
                _padded_lookup = tf.pad(self.look_up_map3d,
                                        [[0, 0], [0, 1], [0, 1], [0, 1], [0, 0]],
                                        "SYMMETRIC", name="padded_lookup_map")
                lookup_temp = tf.gather(_padded_lookup, batch_index)
                indices_temp = tf.repeat(r_as_bin_indices[tf.newaxis], tf.shape(batch_index)[0],
                                         axis=0)
                look_up_values = tf.gather_nd(lookup_temp, indices_temp, batch_dims=1,
                                              name="lookup")
                look_up_values = tf.squeeze(look_up_values, axis=0)
                return tf.identity(look_up_values, name=scope)

    @tf.function(jit_compile=True, reduce_retracing=True)
    # pylint: disable=unused-argument
    def linear_interpolation(self, r_vectors: tf.Tensor,
                             batch_index: tf.Tensor = tf.constant([0, ], dtype=tf.int32),
                             **kwargs) -> tf.Tensor:
        # pylint: disable=anomalous-backslash-in-string
        """Rounds r\_vectors to map-resolution to get look-up indices and gathers the required
        values from the stored 3D table.

        :param r_vectors: (-1, 3) in meter
        :param batch_index: (#batch) indices of the first dimension (T) used for spatial lookup
        :return: (#batch_idx, -1, self._n_channels) trilinear interpolated map values for specified
                    locations
        """
        with tf.name_scope("linear_interpolation_lookup") as scope:
            with tf.device(self.device):
                relative_r_vectors = (r_vectors - self._r_min) / self._r_extend * self._bins
                r_as_bin_indices = self.get_indices(r_vectors)
                indices_all_cell_corners = r_as_bin_indices[:, tf.newaxis] + self.index_additions

                _padded_lookup = tf.pad(self.look_up_map3d,
                                        [[0, 0], [0, 1], [0, 1], [0, 1], [0, 0]],
                                        "SYMMETRIC", name="padded_lookup_map")
                lookup_temp = tf.gather(_padded_lookup, batch_index)
                tf.Assert(batch_index[0] <= tf.shape(_padded_lookup)[0],
                          ["Trying to lookup zeroth dimension index higher than provided",
                           batch_index, "not in", tf.shape(_padded_lookup)])
                indices_temp = tf.repeat(indices_all_cell_corners[tf.newaxis],
                                         tf.shape(batch_index)[0], axis=0)
                look_up_values = tf.gather_nd(lookup_temp, indices_temp,
                                              batch_dims=1, name="lookup")
                rel_distance_to_cell_origin = relative_r_vectors - tf.cast(r_as_bin_indices,
                                                                           tf.float32)
                result = self._calculate_trilinear(rel_distance_to_cell_origin[tf.newaxis],
                                                   look_up_values)
                if result.shape[0] == 1:
                    result = tf.squeeze(result, axis=0)
                return tf.identity(result, name=scope)

    @staticmethod
    # pylint: disable=C0103
    def _calculate_trilinear(r_d, r_vals):
        """ Interpolation according to
            https://en.wikipedia.org/wiki/Trilinear_interpolation

        :param r_d: (#batch, -1, 3) distance to cell corners in order [000, 001, 010, 011,
                                                                       100, 101, 110, 111]
        :param r_vals: (#batch, -1, 8, #channels) value of cell corners
        """
        with tf.name_scope("trilinear_evaluation") as scope:
            r_d = tf.round(r_d * 1e5) / 1e5
            c00 = (1. - r_d[..., 0:1]) * r_vals[..., 0, :] + r_d[..., 0:1] * r_vals[..., 4, :]
            c01 = (1. - r_d[..., 0:1]) * r_vals[..., 1, :] + r_d[..., 0:1] * r_vals[..., 5, :]
            c10 = (1. - r_d[..., 0:1]) * r_vals[..., 2, :] + r_d[..., 0:1] * r_vals[..., 6, :]
            c11 = (1. - r_d[..., 0:1]) * r_vals[..., 3, :] + r_d[..., 0:1] * r_vals[..., 7, :]

            c0 = (1. - r_d[..., 1:2]) * c00 + r_d[..., 1:2] * c10
            c1 = (1. - r_d[..., 1:2]) * c01 + r_d[..., 1:2] * c11
            result = (1. - r_d[..., 2:3]) * c0 + r_d[..., 2:3] * c1
            return tf.identity(result, name=scope)
