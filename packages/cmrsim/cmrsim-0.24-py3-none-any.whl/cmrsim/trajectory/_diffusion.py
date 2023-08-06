"""Contains trajectory modules that model diffusional motion"""

__all__ = ["DiffusionTaylor"]

from typing import List

import numpy as np
import tensorflow as tf
from pint import Quantity
from tqdm import tqdm

from cmrsim.trajectory._taylor import TaylorTrajectoryN


# pylint: disable=abstract-method
class DiffusionTaylor(TaylorTrajectoryN):
    """Combines gaussian diffusional motion with bulk-motion defined as reference-particle
    trajectories. The diffusion motion is implemented by sampling random-walk steps from a gaussian
    distribution and adding them to the reference particle motions, where the number of diffusion
    particles per reference position can be specified on instantiation.
    The random-walk displacements are translated and rotated in space according to a temporal
    evolution of a local basis per reference particle, which must be specified on instantiation.

    .. dropdown:: Example Usage

        .. code::

            t, r = ...   # (steps, )  (particles, steps, 3)
            diff_eigenbasis = ...  # (particles, steps, 9)
            diffusivity = Quantity(np.repeat([[0.18, 0.12, 0.07],], r.shape[0], axis=0), "mm^2/s")

            mod = cmrsim.trajectory.DiffusionTaylor(order=5, time_grid=t,
                                                    particle_trajectories=r,
                                                    local_basis_over_time=diff_eigenbasis,
                                                    diffusivity=diffusivity,
                                                    particles_per_node=100)

    :param time_grid: (T, ) time-points corresponding to the snapshots of motion states
    :param particle_trajectories: (N, T, 3) trajectory snapshots describing the motion state of the
                                  reference nodes
    :param local_basis_over_time: (N, T, 9) Eigen-basis of diffusion tensors per snapshot of
                                  reference particle motion state
    :param diffusivity: (N, 3)  diffusion constant in the direction of the eigen-basis of
                        diffusion tensors per reference node
    :param particles_per_node: Number of additional particles per reference node used as
                               random walkers
    """
    #: Diffusion constants per
    diffusivity_per_particle: tf.Variable

    def __init__(self, order: int, time_grid: Quantity, particle_trajectories: Quantity,
                 local_basis_over_time: np.ndarray, diffusivity: Quantity,
                 particles_per_node: int, batch_size: int = None):
        _array_to_fit = np.concatenate([particle_trajectories,
                                        Quantity(local_basis_over_time, "m")], axis=-1)
        super().__init__(order, time_grid.m_as("ms"), _array_to_fit, batch_size, fit_on_init=True)
        self.diffusivity_per_particle = tf.Variable(
            diffusivity.m_as("m^2/ms").astype(np.float32),
            dtype=tf.float32, shape=(None, 3), trainable=False
        )

        self._particle_offsets = tf.Variable(
            tf.zeros((particles_per_node, *particle_trajectories[:, 0].shape), dtype=tf.float32),
            dtype=tf.float32, shape=(particles_per_node, None, 3), trainable=False
        )
        self.parts_per_node = tf.Variable(particles_per_node, dtype=tf.int32,
                                          shape=(), trainable=False)

    @tf.function(jit_compile=False, reduce_retracing=True)
    def increment_particles(self, particle_positions: tf.Tensor, dt: tf.Tensor,
                            return_eigenbasis: bool = False, **kwargs) -> (tf.Tensor, dict):
        """Evaluates the internally stored taylor-series to obtain the deterministic reference
        positions and diffusion tensor eigen-basis. Additionally, a new random-walk step according
        to the stored diffusivity is sampled and then transformed (rotated) according to the
        orientation change of the eigen-basis.

        **Note**: increments the variable self.current_time

        :param dt:
        :param return_eigenbasis: if True, the eigen-basis at the new position is returned as
                                  entries off the additional_fields dictionary
        :return: (#ref, #subparts, 3), additional_fields
        """
        self.current_time_ms.assign_add(dt)
        temp = self._evaluate_trajectory(tf.reshape(self.current_time_ms, [1, ]))[:, 0]
        deterministic_position = temp[..., :3]
        fiber_dir = temp[..., 3:6]
        sheet_dir = temp[..., 6:9]
        ev3_dir = temp[..., 9:12]
        # Sample random step in 3 Dimensions and scale with diffusivities
        # Shape: (#parts_per_node, #nodes, 3) where the last dimension indexes the
        # directions (fibers, sheet, ev3)
        random_step = tf.random.normal(shape=tf.shape(self._particle_offsets))
        random_step = random_step * self.diffusivity_per_particle[tf.newaxis]
        self._particle_offsets.assign_add(random_step)

        # Stack local basis
        # Shape: (#nodes, len(fibers, sheets, ev3)=3, len(x,y,z)=3)
        eigen_basis = tf.stack([fiber_dir, sheet_dir, ev3_dir], axis=-1)

        # Scale local basis vectors with the random steps
        # Shapes: (#parts_per_node, #nodes, 3) (1, #nodes, 3, 3)
        offset_per_dir = self._particle_offsets[..., tf.newaxis, :] * eigen_basis

        # Evaluate the total 3D displacement as vector sum over local directions
        offset_position = tf.reduce_sum(offset_per_dir, axis=-1)

        additional_fields = {}
        if return_eigenbasis:
            additional_fields["fibers"] = fiber_dir
            additional_fields["sheets"] = sheet_dir
            additional_fields["ev3"] = ev3_dir

        return deterministic_position + offset_position, additional_fields

    def __call__(self, timing: tf.Tensor, dt_max: tf.Tensor, return_eigenbasis: bool = False,
                 **kwargs) -> (tf.Tensor, List[dict]):
        """Repeatedly evaluates the increment_particle method to obtain positions at specified
        times. The resulting trajectories consist of the deterministic part and a random-walk
        according to local diffusion tensor definitions:

        :param timing: Sequence of time-points at which the particle positions shall be return.
        :param dt_max: maximal temporal step-length used to evaluated the increment particles method
        :param return_eigenbasis: if true the rotated eigen-basis is returned as entry in the
                additional field dictionary
        :return: particle trajectory (#steps, #ref_pos, #subparts, #3), additional-field dictionary
        """
        # Define time-definition with maximal step width and including the time points
        time_grid = np.arange(0., timing[-1], dt_max)
        insertion_index = np.searchsorted(time_grid, timing)
        time_grid = np.unique(np.insert(time_grid, insertion_index, timing))
        saving_indices = iter(enumerate(np.concatenate([np.searchsorted(time_grid, timing), [-1]])))

        # Allocate array for result
        positions = np.empty([timing.shape[0], *self._particle_offsets.read_value().shape[0:2], 3],
                             dtype=np.float32)

        # Loop over steps to increment particle positions
        self.current_time_ms.assign(0.)
        temp = self._evaluate_trajectory(tf.reshape(self.current_time_ms, [1, ]))
        particle_positions = temp[:, 0, 0:3]

        additional_fields = []
        result_idx, current_save_index = next(saving_indices)
        if current_save_index == 0:
            positions[result_idx] = particle_positions.numpy()
            result_idx, current_save_index = next(saving_indices)
            if return_eigenbasis:
                additional_fields.append(dict(fibers=temp[:, 0, 3:6], sheets=temp[:, 0, 6:9],
                                              ev3=temp[:, 0, 9:12]))

        for step_idx, dt in tqdm(enumerate(np.diff(time_grid).astype(np.float32)),
                                 total=time_grid.shape[0] - 1):
            particle_positions, fields = self.increment_particles(None, dt, return_eigenbasis)
            if step_idx + 1 == current_save_index:
                positions[result_idx] = particle_positions
                result_idx, current_save_index = next(saving_indices)
                if return_eigenbasis:
                    additional_fields.append(fields)

        trajectories = np.transpose(positions, [0, 1, 2, 3])
        return trajectories, additional_fields
