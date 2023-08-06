__all__ = ["SimulationProgressBarI", "SimulationProgressBarII"]
from typing import Tuple, Optional, TYPE_CHECKING
from abc import abstractmethod
import sys
import os
from collections import OrderedDict

import tensorflow as tf


class SimulationProgressBarI(tf.Module):
    """ Graph-execution compatible command line progress-bar for running simulations"""
    # pylint: disable=too-many-instance-attributes
    target: tf.Variable
    current: tf.Variable

    # pylint: disable=too-many-arguments
    def __init__(self, total: int, prefix: str = '', suffix: str = '', bar_width=40,
                 print_step = 20):
        """ Construct a progress-bar instance  """
        super().__init__(name='progress_bar')
        with self.name_scope:
            self.target = tf.Variable(total, dtype=tf.int32, trainable=False, name='total_voxels')
            self.current = tf.Variable(0, dtype=tf.int32, trainable=False, name="current_voxel")
            self.bar_length = tf.constant(bar_width, dtype=tf.int32)
            self.prefix = prefix
            self.suffix = suffix
            self.print_step = print_step

    def update(self, current: int):
        """ Upates the value  """
        self.current.assign(tf.cast(current, tf.int32))
        if tf.math.mod(self.current, self.print_step) == 0:
            self.print()

    def add(self, n_add:  int):
        self.current.assign_add(tf.cast(n_add, tf.int32))
        if tf.math.mod(self.current, self.print_step) == 0:
            self.print()

    def finalize(self):
        """Sets all counters to their total max and prints the progress bar"""
        self.update(self.target.read_value())
        self.print()

    def reset(self):
        self.current.assign(0)

    @tf.function()
    def print(self):
        """ Graph-compatible definition of printing the current state of the progress bar """
        def bar_string(iteration, total, length):
            filled_length = tf.cast(tf.math.divide_no_nan(
                tf.cast(length * iteration, tf.float32), tf.cast(total, tf.float32)),
                tf.int32)
            prog_bar = tf.concat((tf.repeat('X', filled_length),
                                  tf.repeat('-', length - filled_length)), 0)
            ret_list = tf.concat((('|',), prog_bar,
                                  ('|', tf.strings.format('{}/{}', [iteration, total]))), 0)
            ret = tf.strings.reduce_join(ret_list)
            return ret
        bar = bar_string(self.current.read_value(), self.target.read_value(), self.bar_length)
        full_string = tf.strings.reduce_join(('\r', self.prefix, '\t', bar, self.suffix))
        tf.print(full_string, end=' ', output_stream=sys.stdout)


class SimulationProgressBarII(tf.Module):
    """ Graph-execution compatible command line progress-bar for running simulations"""
    # pylint: disable=too-many-instance-attributes
    total_voxels: tf.Variable
    total_segments: tf.Variable
    current_image: tf.Variable
    current_voxel: tf.Variable
    current_segment: tf.Variable

    # pylint: disable=too-many-arguments
    def __init__(self, total_voxels: int = 0, total_segments: int = None,
                 prefix: str = '', suffix: str = ''):
        """ Construct a progress-bar instance with three sub-progress-bars. The totals of each
        sub-bar are given by the arguments.
        """
        super().__init__(name='progress_bar')
        with self.name_scope:
            self.total_voxels = tf.Variable(total_voxels, dtype=tf.int32, trainable=False,
                                            name='total_voxels')
            self.total_segments = tf.Variable(total_segments, dtype=tf.int32, trainable=False,
                                              name='total_segments')
            self.current_voxel = tf.Variable(0, dtype=tf.int32, trainable=False,
                                             name="current_voxel")
            self.current_segment = tf.Variable(0, dtype=tf.int32, trainable=False,
                                               name="current_segment")
            self.bar_lengths = (20, 15)
            self.prefix = prefix
            self.suffix = suffix

    def update(self, add_voxels: int = None, add_segment: int = None,
               set_voxel: int = None, set_segment: int = None):
        """ Function to update the state of the progress bar either by setting the absolute value
        or adding a number to the sub-bars.

        """
        if add_voxels is not None:
            self.current_voxel.assign_add(tf.cast(add_voxels, tf.int32))
        if add_segment is not None:
            self.current_segment.assign_add(tf.cast(add_segment, tf.int32))
        if set_voxel is not None:
            self.current_voxel.assign(tf.cast(set_voxel, tf.int32))
        if set_segment is not None:
            self.current_segment.assign(tf.cast(set_segment, tf.int32))

    def reset_voxel(self):
        """ Resets counter of the point-sub-bar to 0 """
        self.current_voxel.assign(0)

    def reset_segments(self):
        """ Resets counter of the segment-sub-bar to 0 """
        self.current_segment.assign(0)

    def print_final(self):
        """Sets all counters to their total max and prints the progress bar"""
        self.update(set_voxel=self.total_voxels.read_value(),
                    set_segment=self.total_segments.read_value())
        self.print()

    @tf.function
    def print(self):
        """ Graph-compatible definition of printing the current state of the progress bar """
        def bar_string(iteration, total, length):
            filled_length = tf.cast(tf.math.divide_no_nan(
                tf.cast(length * iteration, tf.float32), tf.cast(total, tf.float32)),
                tf.int32)
            prog_bar = tf.concat((tf.repeat('X', filled_length),
                                  tf.repeat('-', length - filled_length)), 0)
            ret_list = tf.concat((('|',), prog_bar,
                                  ('|', tf.strings.format('{}/{}', [iteration, total]))), 0)
            ret = tf.strings.reduce_join(ret_list)
            return ret

        voxel_bar = bar_string(self.current_voxel.read_value(), self.total_voxels.read_value(),
                               self.bar_lengths[1])
        segment_bar = bar_string(self.current_segment.read_value(),
                                 self.total_segments.read_value(),
                                 self.bar_lengths[1])
        full_string = tf.strings.reduce_join(('\r', self.prefix, '\t', voxel_bar,
                                              '\t', segment_bar, self.suffix))
        tf.print(full_string, end=' ', output_stream=sys.stdout)
