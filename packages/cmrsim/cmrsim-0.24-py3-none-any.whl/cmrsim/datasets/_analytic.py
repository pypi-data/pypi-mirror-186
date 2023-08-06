__all__ = ["AnalyticDataset"]

from collections import OrderedDict

import numpy as np
from cmrsim.datasets._base import BaseDataset


class AnalyticDataset(BaseDataset):

    def __init__(self, array_dictionary: OrderedDict, filter_inputs: bool = True,
                 expand_dimension: bool = False):
        """ Initializes a callable module, that yields an iterable tf.Dataset on call. The target
        shape of the yielded batches is (#batch, #repetitions, #kspace-samples, ...)


        :raises: InvalidArgument - if shape of M0 and r_vector entry of the dictionary do not match
                                  (#MaterialPoints, #Repetitions, #k-space-samples)
                                  (#MaterialPoints, #Repetitions, 3, #k-space-samples)
                                  InvalidArgumentError is raised

        :param array_dictionary: (OrderedDict) containing the required quantities as numpy arrays
        :param filter_inputs: If set to true, trivial material points are filtered (M0=0),
                                on instantiation
        """
        if expand_dimension:
            if len(array_dictionary["M0"].shape) > 1:
                dtype_list = [f"{k}: {v.shape}" for k, v in array_dictionary.items()]
                raise ValueError("Arrays appear to have repetition/sample axis already. Please"
                                 "disable the expand-dims argument. Shapes" +
                                 "\n\t".join(dtype_list))
            array_dictionary = {k: v[:, np.newaxis, np.newaxis]
                                for k, v in array_dictionary.items()}

        if array_dictionary["M0"].dtype != np.dtype(np.complex64):
            raise ValueError("M0 is not of required type complex64")

        if not all([v.dtype == np.dtype(np.float32) for k, v
                    in array_dictionary.items() if k != "M0"]):
            dtype_list = [f"{k}: {v.dtype}" for k, v in array_dictionary.items() if k != "M0"]
            raise ValueError("Not all arrays are of required type np.float32: \n" +
                             "\n\t".join(dtype_list))

        if len(array_dictionary["M0"].shape) != 3:
            raise ValueError("Shape of input array M0 invalid")
        if len(array_dictionary["r_vectors"].shape) != 4:
            raise ValueError("Shape of input array r_vectors invalid")
        if array_dictionary["r_vectors"].shape[-1] != 3:
            raise ValueError(f"Last dimension of r-vectors is not 3, it is likely that the array"
                             f"axes are wrongly ordered. Refer to doc-string.\n"
                             f"Given shape: {array_dictionary['r_vectors'].shape}")

        super().__init__(filter_inputs=filter_inputs, array_dictionary=array_dictionary)

        self.set_size = self._array_dict["M0"].shape[0]
        self.map_names = tuple(self._array_dict.keys())
