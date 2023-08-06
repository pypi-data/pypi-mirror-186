""" This module contains the base implementation of the encoding mechanism of the simulation"""
__all__ = ["BaseSampling", "InternalAccumulator", "BlochOperatorInput"]

from typing import Union, Iterable, Tuple
import abc
import math

import tensorflow as tf


# pylint: disable=abstract-method
class BaseSampling(tf.Module):
    """Base Module for implementing a time-dependent sampling in k-space. Is meant to be inherited
    from when specifying standard trajectories.

    :param absolute_noise_std: if < 0, add_noise() will leave signal unchanged
    :param name: (str) defining the module name-scope
    :param k_space_segments: int
    :param device: str e.g. 'GPU:0'
     """
    # pylint: disable=too-many-instance-attributes
    #: Flat and unsegmented tensor of all sampling-event times.  Is set by a call of
    # abstract function self._calculate_trajectory. Expected shape: (-1, )
    sampling_times: tf.Variable
    #: Flat and unsegmented tensor of 3D k-space vectors corresponding to sampling-events.
    # Is set by a call of abstract function self._calculate_trajectory. Expected shape: (-1, 3)
    k_space_vectors: tf.Variable
    #: absolute values for the standard deviation of the sampled noise distributions added
    # to the k-space signal
    absolute_noise_std: tf.Variable
    #: Number of segments used to subdivide the simulation memory load
    k_space_segments: tf.Variable
    #: Number of k-space samples that are defined by the _calculate trajectory method
    number_of_samples: tf.Tensor
    #: Name of the device that the module is executed on (defaults to: GPU:0 - CPU:0)
    device: str
    #: Spatial acquisition offset (corresponds to frequency offset)
    acq_position: tf.Variable = tf.Variable(tf.zeros(3), dtype=tf.float32)

    _segmented_sampling_times = None  # set in update
    _segmented_k_vectors = None  # set in update

    def __init__(self, absolute_noise_std: Union[float, Iterable[float]], name: str = None,
                 k_space_segments: int = 1, device: str = None):
        """

        :param absolute_noise_std: if < 0, add_noise() will leave signal unchanged
        :param name: (str) defining the module name-scope
        :param k_space_segments: int
        :param device: str e.g. 'GPU:0'
        """

        if device is None:
            if tf.config.get_visible_devices('GPU'):
                self.device = 'GPU:0'
            else:
                self.device = 'CPU:0'
        else:
            self.device = device

        super().__init__(name=name)
        if isinstance(absolute_noise_std, float):
            absolute_noise_std = [absolute_noise_std, ]

        self.absolute_noise_std = tf.Variable(tf.constant(absolute_noise_std), dtype=tf.float32,
                                              trainable=False, shape=[None, ],
                                              name='absolute_noise_std')
        self.k_space_segments = tf.Variable(tf.constant(k_space_segments), dtype=tf.int32,
                                            trainable=False)
        self.k_space_vectors = tf.Variable(tf.zeros((1, 3), tf.float32), shape=[None, 3],
                                           dtype=tf.float32, trainable=False,
                                           name='k_space_vectors')
        self.sampling_times = tf.Variable(tf.zeros((1,), tf.float32), shape=[None, ],
                                          dtype=tf.float32, trainable=False, name='sampling_times')
        self.update()

    def update(self):
        """ Assigns values to trajectory vectors. Should be used after modifying the parameters of
        the encoding module.
        :return:
        """
        k_space_vectors, sampling_times = self._calculate_trajectory()
        self.k_space_vectors.assign(k_space_vectors)
        self.sampling_times.assign(sampling_times)
        self.number_of_samples = tf.size(self.sampling_times.read_value())

        # Define segmented k-space trajectory for lower GPU memory requirements
        segment_size = tf.cast(tf.math.ceil(self.number_of_samples /
                                            self.k_space_segments.read_value()), tf.int32)
        total_element_count = self.k_space_segments.read_value() * segment_size
        difference = total_element_count - self.number_of_samples
        row_lengths = tf.constant([int(segment_size) for _ in
                                   tf.range(self.k_space_segments.read_value() - 1)] +
                                  [int(segment_size - difference), ], dtype=tf.int32)

        self._segmented_sampling_times = tf.RaggedTensor.from_row_lengths(
            self.sampling_times.read_value(), row_lengths)
        self._segmented_k_vectors = tf.RaggedTensor.from_row_lengths(
            self.k_space_vectors.read_value(), row_lengths)

    def __call__(self, transverse_magnetization: tf.Tensor, r_vectors: tf.Tensor,
                 segment_index: Union[int, tf.Tensor] = 0, **kwargs):
        """Calculates fourier phases for given object-representation at r-vectors. For multiple
        different contrasts #repetitions is the representing axis.

        Motion during encoding is captured in the r_vectors input axis #k-space-samples. If
        this axis has size=1, this position is reused for all sampling ADC events.
        If #repetitions = 1 in r_vectors, the same trajectory/constant position is reused
        for all contrasts.

        :param transverse_magnetization: (#voxel, #repetitions, #k-space-samples) of
                                         type tf.complex; #repetitions, #k-space-samples can be 1
        :param r_vectors: (#voxel, #repetitions, #k-space-samples, 3), axis #repetitions
                            and #k-space-samples can be 1 to broadcast for coordinate reuse.
        :param segment_index: int
        :param kwargs: - noise_seed: if not None, sets seed for sampling the noise vector.
        :return: tf.Tensor
        """
        with tf.device(self.device):
            n_repetitions = tf.shape(transverse_magnetization)[1]
            fourier_factors = self._calculate_fourier_phases(r_vectors=r_vectors,
                                                             segment_index=segment_index)

            with tf.name_scope('shape_handling'):
                if tf.shape(fourier_factors)[1] < n_repetitions:
                    multiples = n_repetitions // tf.shape(fourier_factors)[1]
                    fourier_factors = tf.tile(fourier_factors, [1, multiples, 1])

                if tf.shape(transverse_magnetization)[2] == 1:
                    n_samples = tf.size(self._segmented_sampling_times[segment_index])
                    transverse_magnetization = tf.tile(transverse_magnetization,
                                                       [1, 1, n_samples])
            fourier_transform_batch = tf.einsum('vrk, vrk -> rk',
                                                transverse_magnetization, fourier_factors)
            return fourier_transform_batch

    def _calculate_fourier_phases(self, r_vectors: tf.Tensor, segment_index: tf.Tensor):
        # pylint: disable=anomalous-backslash-in-string
        """ Calculates the phase factor for encoding a static (during read-out) object for the
         k-space-trajectory defined by self.k_space_vectors

        .. math::

            f = e^{2 \pi j\ k_r(t) \cdot r(t) }

        :param r_vectors: (#batch, #repetition, #kspace, 3)
        :param segment_index: int
        :return:
        """
        with tf.name_scope('calculate_fourier_phase'):
            segment_batch_size = tf.size(self._segmented_sampling_times[segment_index])
            if tf.shape(r_vectors)[2] == 1:  # tile if #kspace-samples is 1
                r_vectors = tf.tile(r_vectors, [1, 1, segment_batch_size, 1])
            elif tf.shape(r_vectors)[2] != segment_batch_size:
                start = segment_batch_size * segment_index
                r_vectors = r_vectors[..., start:start + segment_batch_size, :]

            r_vectors = r_vectors - tf.reshape(self.acq_position, [1, 1, 1, 3])
            fourier_phases = tf.einsum('vrkj, kj -> vrk', r_vectors,
                                       self._segmented_k_vectors[segment_index])
            fourier_phases = 1j * tf.cast(
                tf.scalar_mul(tf.constant(2. * math.pi, tf.float32), fourier_phases), tf.complex64)
            fourier_factors = tf.exp(-fourier_phases)
            return fourier_factors

    def add_noise(self, s_of_k: tf.Tensor, **kwargs):
        """ Adds noise to k-space-samples, expands the number of axis by one and appends the
        different noise instantiations as second last axis.

        :param s_of_k: Tensor containing all encoded k-space samples
        :return: tf.Tensor
        """
        with tf.name_scope('add_noise'):
            old_shape = tf.shape(s_of_k)
            s_of_k = tf.expand_dims(s_of_k, axis=-2)
            if tf.reduce_any(tf.math.greater(self.absolute_noise_std, tf.constant(0.))):
                seed = kwargs.get("seed", None)

                # Set values less that 0 to exactly zero to scales sampled noise vector correctly
                clean_noise_std = tf.where(
                    tf.math.greater(self.absolute_noise_std, tf.constant(0.)),
                    self.absolute_noise_std, tf.zeros_like(self.absolute_noise_std))
                noise_vector_shape = tf.concat(
                    ((2,), old_shape, (tf.size(self.absolute_noise_std),)), 0)
                noise_vector = tf.random.normal(noise_vector_shape, mean=0., stddev=1., seed=seed)

                # Transposition of last two axis on purpose for subsequent addition
                # Einsum indices: real/imag channel, image_batch, ...
                # ... repetitions, pixels,noise_instantiations
                n_half = tf.cast(tf.size(self.sampling_times), tf.float32) / 2.
                noise_vector = tf.einsum('crpn, n -> crnp', noise_vector,
                                         clean_noise_std * tf.sqrt(n_half))
                complex_noise_vector = tf.complex(noise_vector[0], noise_vector[1])
                s_of_k = s_of_k + complex_noise_vector
            return s_of_k

    @abc.abstractmethod
    def _calculate_trajectory(self):
        """ Calculates the k_space_trajectory with the given variables of the module. The
        trajectory is given as tensor of shape (#samples, 3). Additionally it should return a
        tensor of times corresponding to the samples
        (#samples, 1) in ms

        :return: k_space_vectors, sampling_times
        """
        raise NotImplementedError

    def get_sampling_times(self):
        """Getter for sampling times. Defines format that should be used for all Signal modules
        that need the timing of the sampling events.

        :return: - tf.RaggedTensor or numpy.ndarray
                 - sampling times as numpy.ndarray in case the trajectory is not segmented.
        """
        if int(self.k_space_segments) > 1:  # noqa
            return self._segmented_sampling_times

        return self.sampling_times.read_value()


# pylint: disable=abstract-method
class InternalAccumulator(tf.Module):
    """Wraps a BaseSampling object to enable internal k-space accumulation"""
    #: Encoding module that is wrapped
    wrapped_module: BaseSampling
    _kspace_acc: Tuple[tf.Variable]

    def __init__(self, encoding_module: BaseSampling, n_repetitions: int):
        """
        :param encoding_module: Instance of an encoding module
        :param n_repetitions: number of repetitions to be expected for
                given transversal magnetization
        """
        self.wrapped_module = encoding_module
        super().__init__(name=encoding_module.name)
        self.update(n_repetitions)

    def update(self, n_repetitions: int):
        self.wrapped_module.update()
        # pylint: disable=protected-access
        samples_per_segment = [tf.shape(_)[0] for _ in
                               self.wrapped_module._segmented_sampling_times]

        with tf.device("CPU:0"):
            # pylint: disable=consider-using-generator
            self._kspace_acc = tuple([tf.Variable(tf.zeros((n_repetitions, s),
                                                           dtype=tf.complex64),
                                                  dtype=tf.complex64, shape=(None, s))
                                      for s in samples_per_segment])

    def __getattr__(self, attr):
        """ This is only called if attr is not in self.__dict__"""
        if attr != "wrapped_module":
            return getattr(self.wrapped_module, attr)

    def __call__(self, transverse_magnetization: tf.Tensor, r_vectors: tf.Tensor,
                 segment_index: Union[int, tf.Tensor] = 0, **kwargs):
        samples_batch = self.wrapped_module(transverse_magnetization, r_vectors,
                                            segment_index, **kwargs)
        with tf.device("CPU:0"):
            self._kspace_acc[segment_index].assign_add(samples_batch)
        return transverse_magnetization

    def reset(self):
        """ Sets all k-space-line accumulators to zero """
        for i, accumulator in enumerate(self._kspace_acc):
            self._kspace_acc[i].assign(tf.zeros_like(accumulator))

    def get_kspace(self):
        """ Returns k-space data in shape (1, -1, #samples)"""
        return tf.concat(self._kspace_acc, -1)


# pylint: disable=abstract-method
class BlochOperatorInput(tf.Module):
    """Wraps a BaseSampling object to deal with the difference in input shape for bloch operators
    and solution operators """

    def __init__(self, encoding_module: Union[BaseSampling, InternalAccumulator]):
        """
        :param encoding_module: Instance of an encoding module
        """
        super().__init__(name=encoding_module.name)
        self.wrapped_module = encoding_module

    def __getattr__(self, attr):
        """ This is only called if attr is not in self.__dict__"""
        if attr != "wrapped_module":
            return getattr(self.wrapped_module, attr)

    def __call__(self, magnetization: tf.Tensor, trajectories: tf.Tensor,
                 segment_index: Union[int, tf.Tensor] = 0, **kwargs):
        """

        :param magnetization: (#batch, 3)
        :param trajectories: (#batch, #k-space-points, 3)
        """
        m_transverse = tf.reshape(magnetization[:, 0], [-1, 1, 1])
        rvec = tf.reshape(trajectories, [magnetization.shape[0], 1, -1, 3])
        return self.wrapped_module(transverse_magnetization=m_transverse, r_vectors=rvec,
                                   segment_index=segment_index, **kwargs)
