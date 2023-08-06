""" This module contains the base implementation of a Dataset containing a digital phantom defined
 as a dictionary of numpy arrays, fitting into RAM at once"""

__all__ = ["BlochDataset"]

from collections import OrderedDict
from cmrsim.datasets._base import BaseDataset


class BlochDataset(BaseDataset):
    def __init__(self, array_dictionary: OrderedDict, filter_inputs: bool = True):
        """ Initializes a callable module, that yields an iterable tf.Dataset on call. The target
        shape of the yielded batches is (#batch, ...)

        :raises: InvalidArgument - if shape of M0, magnetization entries of the dictionary do
                    not match (#MaterialPoints, ), (#MaterialPoints, 3)

        :param array_dictionary: (OrderedDict) containing the required quantities as numpy arrays
        :param filter_inputs: If set to true, trivial material points are filtered (M0=0),
                                on instantiation
        """
        if len(array_dictionary["M0"].shape) != 1:
            raise ValueError("Shape of input array M0 invalid")
        if len(array_dictionary["magnetization"].shape) != 2:
            raise ValueError("Shape of input array magnetization invalid")
        if len(array_dictionary["T1"].shape) != 1:
            raise ValueError("Shape of input array T1 invalid")
        if len(array_dictionary["T2"].shape) != 1:
            raise ValueError("Shape of input array T2 invalid")

        self.set_size = array_dictionary["magnetization"].shape[0]
        self.map_names = tuple(array_dictionary.keys())
        super().__init__(filter_inputs=filter_inputs, array_dictionary=array_dictionary)
