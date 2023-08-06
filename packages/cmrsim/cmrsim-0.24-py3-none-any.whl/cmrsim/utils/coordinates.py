""" Module that contains functions to get required in the format """

__all__ = ['get_static_2d_centered_coordinates']


from typing import Tuple, Optional

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