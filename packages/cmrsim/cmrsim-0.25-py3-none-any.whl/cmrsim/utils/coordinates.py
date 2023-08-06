""" Module that contains functions to get required in the format """

__all__ = ['get_static_2d_centered_coordinates', "compute_orientation_matrix"]


from typing import Tuple, Optional

import numpy as np
from pint import Quantity
import tensorflow as tf


def get_static_2d_centered_coordinates(
                    map_size: Tuple[int, int],
                    object_dimensions: Optional[Tuple[float, float]] = None,
                    return_2d: bool = True
                    )-> tf.Tensor:
    """ Calculates relative coordinates for a dense map with coordinate origin in the center of the
    map. If the dimension in map_size is even, the origin is shifted 1/2 with respect to grid
    indices, if they are uneven, the origin coincides with a grid point.
    Reshapes the output to a shape, used in cmrsim simulations. The singleton-axis is reserved
    for repetitions contrasts.

    :param map_size: Tuple[int, int], 2D grid dimensions used to calculate coordinates relative
                                to mid-point
    :param object_dimensions: Optional Tuple[float, float] used to scale relative coordinates.
                                Defaults to (1., 1.)
    :return: (X, Y, 1, 1, 3)
    """
    if object_dimensions is None:
        object_dimensions = (1., 1.)

    map_size = tf.constant(map_size, dtype=tf.float32)
    x, y = tf.meshgrid(tf.range(0., map_size[0]), tf.range(0., map_size[1]), indexing='xy')
    grid_coordinates = tf.cast(tf.stack([x, y], 2), tf.float32)
    offsets = (1 - tf.math.mod(map_size, 2)) / 2
    cell_mid_shift_coords = grid_coordinates - (map_size - 1) / 2 - offsets
    object_scaling_dr = tf.constant(object_dimensions) / map_size
    voxel_center_coords = cell_mid_shift_coords * object_scaling_dr

    # Append zero z coordinate
    voxel_center_coords = tf.concat((voxel_center_coords, tf.zeros_like(x)[..., tf.newaxis]), -1)

    # Reshape to desired shape
    if return_2d:
        voxel_center_coords = tf.reshape(voxel_center_coords, [map_size[0], map_size[1], 1, 1, 3])
    else:
        voxel_center_coords = tf.reshape(voxel_center_coords, [-1, 1, 1, 3])
    return voxel_center_coords

def compute_orientation_matrix(slice_normal: np.array, slice_position: Quantity,
                               readout_direction: np.array = None):
    """Computes the 4x4 transformation matrix :math:`A` that transform a positional vector
    :math:`r_{s}` defined in slice-coordinates into the gobal coordinate system :math:`r_{g}`.
    To apply the transformation, compute the matrix-vector product:

    .. math::

        (x_{g}, y_{g}, x_{g}, 1) = A \cdot (x_{s}, y_{s}, x_{s}, 1)

    To apply the inverse transformation, transpose the rotation-part of the matrix:

    .. code::

        A_inv =  A.copy()
        A_inv[:3, :3] = A[:3, :3].T

    :param slice_normal:
    :param slice_position:
    :param readout_direction:
    :return: transformation matrix - A (4, 4)
    """
    from scipy.spatial.transform import Rotation
    slice_normal /= np.linalg.norm(slice_normal)

    if readout_direction is None:
        if np.allclose(slice_normal, np.array([1., 0., 0.]), atol=1e-3):
            readout_direction = np.array([0., 1., 0.])
        else:
            readout_direction = np.array([1., 0., 0.])
    else:

        if np.isclose(
                np.dot(slice_normal, readout_direction / np.linalg.norm(readout_direction)),
                1., atol=1e-3):
            raise ValueError("Slice normal and readout-direction are parallel")

    readout_direction = readout_direction - np.dot(slice_normal,
                                                   readout_direction) * slice_normal
    readout_direction /= np.linalg.norm(readout_direction)
    pe_direction = np.cross(readout_direction, slice_normal)
    pe_direction /= np.linalg.norm(pe_direction)
    original_basis = np.eye(3, 3)
    new_basis = np.stack([readout_direction, pe_direction, slice_normal])

    rot, _ = Rotation.align_vectors(original_basis, new_basis)

    total_transform = np.eye(4, 4)
    total_transform[:3, :3] = rot.as_matrix()
    total_transform[:3, 3] = slice_position.m_as("m")
    return total_transform