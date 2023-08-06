"""Contains base-implementation / definition for trajectory modules"""

__all__ = ["BaseTrajectoryModule", "StaticParticlesTrajectory"]

from abc import abstractmethod

import tensorflow as tf


class BaseTrajectoryModule(tf.Module):
    """ Base implementation for Trajectory modules compatible with the Bloch simulation module
    as well as containing a guaranteed method for position pre-calculation on call.

    All derived classes must implement the abstract method "increment_particles" which must be
    compatible with a tf.function decoration. The __call__ function must also be implemented but
    is not meant to be called inside a tf.function
    """
    @abstractmethod
    def __call__(self, initial_position: tf.Tensor, timing: tf.Tensor, **kwargs)\
            -> (tf.Tensor, dict):
        """ Evaluates the positions for particles at given initial positions for all times specified
        in the timing argument. For implementations using the increment_particles function
        in a loop the maximal time-delta must be specified.

        :param initial_position: (N, 3)
        :param timing: (T, )
        :param kwargs: Can vary in concrete implementation
        :return:  - r_new [tf.Tensor, (T, N, 3)]
                  - additional_fields [dict] containing the lookup values for each step
        """
        return None

    @abstractmethod
    def increment_particles(self, particle_positions: tf.Tensor, dt: tf.Tensor,
                            **kwargs) -> (tf.Tensor, dict):
        """ Evaluates the new position of particles at given locations r for a temporal
        step width dt. If the concrete implementation involves a look up (e.g. velocity fields)
        the values at the old location is also returned as dictionary.

        .. note::

            concrete implementations must be compatible with tf.function decoration

        :param particle_positions: (N, 3) Current particle positions.
        :param dt: (,) Temporal step width in milliseconds to evaluate the next positions
        :param kwargs: Can vary in concrete implementation
        :return: r_new [tf.Tensor, (N, 3)], additional_fields [dict] containing the lookup values
        """
        return None


# pylint: disable=abstract-method
class StaticParticlesTrajectory(BaseTrajectoryModule):
    """ Trivial implementation for static particles to match the trajectory-module definition
    for Bloch simulations. When called (also increment_particles) just returns the identity
    operation for particle positions along with an empty dictionary usually containing the
    additional field look-ups.
    """
    def __int__(self):
        super().__init__(name="static_trajectory")

    def __call__(self, initial_positions: tf.Tensor, timing: tf.Tensor,
                 **kwargs) -> (tf.Tensor, dict):
        """ Returns a tiled tensor of the static positions

        :param initial_position: (N, 3)
        :param timing: (T, )
        :return: r_const - (T, N, 3)
        """
        n_steps = tf.shape(timing)[0]
        return tf.tile(initial_positions[tf.newaxis], [n_steps, 1, 1]), {}

    def increment_particles(self, particle_positions: tf.Tensor, dt: tf.Tensor,
                            **kwargs) -> (tf.Tensor, dict):
        return particle_positions, {}
