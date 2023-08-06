""" This module contains the base implementation of a Dataset containing a digital phantom defined
 as a dictionary of numpy arrays, fitting into RAM at once"""

__all__ = ["BaseDataset"]

from abc import abstractmethod

from typing import Optional, Tuple
from collections import OrderedDict

import tensorflow as tf


class BaseDataset(tf.Module):
    """ Basic implementation of a module that constructs a tf.data.Dataset from the dictionary
    of numpy arrays, describing the digital phantom. """

    #: Names of simulation quantities passed as dictionary keys on construction
    map_names: Tuple = None
    #: Number of anatomies (0th - axis) of the passed simulation quantities
    set_size: int = None
    _array_dict: dict

    def __init__(self, filter_inputs, array_dictionary):
        """
        :param array_dictionary: (OrderedDict) containing the required quantities as numpy arrays
        :param filter_inputs: If set to true, trivial material points are filtered (M0=0),
                                on instantiation
        """
        super().__init__()
        if filter_inputs:
            self._array_dict = self._filter_inputs(array_dictionary)
        else:
            self._array_dict = array_dictionary

    def __call__(self, batchsize: int = 1000, prefetch: int = 5) -> (int, tf.data.Dataset):
        """ Returns a nested tf.data.Dataset, where the inner dataset represents the digital
         phantom per image. These datasets are batch and prefetch, and the batch yielded is a
         dictionary like : {'M0', tf.Tensor(...), ...}. The keys of the dict are strings, while the
         values each are Tensors representing a batch of iso-chromates/grid-positions of
         the flattened datasets.

        The return dataset is supposed to be iterated as:
        .. code::

                for batch in dataset(batchsize=500):
                    # batch = {magnetization:( ), trajectories: ( ), T1: (-1), ....}
                    ...

        :param batchsize: (int) batch size
        :param prefetch: (int) prefetched batches
        :return: tf.data.Dataset
        """
        datasets = tf.data.Dataset.from_tensor_slices(self._array_dict)
        return datasets.batch(batchsize).prefetch(prefetch)

    @staticmethod
    def _filter_inputs(array_dict):
        """ Per-image filter function, to select only grid-points that have an initial
        magnetization > 0.

        :return:
        """
        m0 = array_dict["M0"]
        indices = tf.where(tf.abs(m0) > 0.)[:, 0]
        new_dict = OrderedDict([(k, tf.gather(v, indices, axis=0)) for k, v in array_dict.items()])
        return new_dict
