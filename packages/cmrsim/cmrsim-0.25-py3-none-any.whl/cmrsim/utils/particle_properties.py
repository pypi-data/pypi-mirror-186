""" Module containing factory functions to define particle properties used"""

__all__ = ["uniform", "norm_magnetization", "t2star_lorentzian"]

import tensorflow as tf
import numpy as np

from typing import Tuple


def uniform(default_value: float, additional_shape: Tuple[int, ...] = (),
            dtype: np.dtype = np.float32):
    """ Factory function to create an array containing the property of n_new particles """
    def ret_func(n_new):
        return np.ones([n_new, *additional_shape], dtype=dtype) * default_value
    return ret_func


def norm_magnetization(dtype: np.dtype = np.complex64):
    """    """
    def ret_func(n_new):
        single_mag = np.array([[0 + 0j, 0 + 0j, 1 + 0j], ], dtype=np.complex64)
        return np.tile(single_mag, [n_new, 1])
    return ret_func


def t2star_lorentzian(T2p: float, prctile_cutoff: float = 0.01, dtype: np.dtype = np.float32):
    def ret_func(n_new: int):
        pos_on_distribution_support = tf.random.uniform([n_new], minval=0 + prctile_cutoff,
                                                        maxval=1 - prctile_cutoff) - 0.5
        omega_t2s = 1. / T2p * tf.tan(np.pi * pos_on_distribution_support)
        return np.array(omega_t2s).astype(dtype)
    return ret_func
