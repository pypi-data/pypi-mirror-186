""" This module contains the Entry-point for defining and running simulations """
__all__ = ['AnalyticSimulation', ]
from typing import Tuple, Optional, TYPE_CHECKING
from abc import abstractmethod
import os
from collections import OrderedDict

import tensorflow as tf

if TYPE_CHECKING:
    from cmrsim.datasets import AnalyticDataset
    from cmrsim.analytic.encoding.base import BaseSampling
    from cmrsim.reconstruction.base import BaseRecon
    from cmrsim.analytic._composite_signal import CompositeSignalModel

from cmrsim.utils.display import SimulationProgressBarII


class AnalyticSimulation(tf.Module):
    """ This module provides the entry point to build and call the simulations defined within the
    cmrsim framework. It is meant to be subclassed, where all subclasses need to implement the
    abstract method `_build` defining the building blocks of the simulation to run.

    Creates an instance of class either by using the given building Blocks or by calling
    the _build function to set up the simulation.

    :param name:
    :param building_blocks: Tuple containing one instance each of
                            'CompositeSignalModel', 'BaseSampling', 'BaseRecon'
                            defining the actual simulation configuration if it is None, the
                            memberfunction _build is called
    """
    forward_model: 'CompositeSignalModel' = None
    encoding_module: 'BaseSampling' = None
    recon_module: 'BaseRecon' = None

    def __init__(self, name: str = None,
                 building_blocks: Tuple['CompositeSignalModel', 'BaseSampling', 'BaseRecon'] = None,
                 build_kwargs: dict = None):
        """

        :param name:
        :param building_blocks: Tuple containing one instance each of
                                'CompositeSignalModel', 'BaseSampling', 'BaseRecon'
                                defining the actual simulation configuration if it is None, the
                                memberfunction _build is called
        """
        super().__init__(name=name)
        if building_blocks is None:
            if build_kwargs is None:
                raise ValueError("Neither building blocks nor build kwargs are specified")
            self.forward_model, self.encoding_module, self.recon_module = self.build(**build_kwargs)
        else:
            self.forward_model, self.encoding_module, self.recon_module = building_blocks

        # Initialize progress bar
        n_k_space_segments = self.encoding_module.k_space_segments.read_value()
        self.progress_bar = SimulationProgressBarII(total_voxels=1, prefix='Run Simulation: ',
                                                  total_segments=n_k_space_segments)

    @abstractmethod
    def build(self, **kwargs) -> ('CompositeSignalModel', 'BaseSampling', 'BaseRecon'):
        """ Abstract method that needs to be defined in subclasses to configure
         specific simulations
        """
        return -1

    def __call__(self, dataset: 'AnalyticDataset', voxel_batch_size: int = 1000,
                 unstack_repetitions: bool = True,
                 trajectory_module=None,
                 trajectory_signatures: dict = None,
                 additional_kwargs: dict = None) -> tf.Tensor:
        """ Wrapper for the decorated (@tf.function) call of the simulation loop.

        :param dataset:
        :param voxel_batch_size: (int) see documentation of _simulate_segmented_k_space.
        :param unstack_repetitions: If False the returned shape will be
                                    (#images, #Reps, #noise_levels, #samples).
                                    If True refer to 'return' in docstring.
        :return: **(tf.Tensor)** | Stack of images with shape
            (#images, ..., #noise_levels, #X, #Y, #Z), or k-spaces  with shape
            (#images, ..., #noise_levels, #samples)  where the ellipsis (...) depends on the
            specific forward model. The order in which the *CompositeSignalModel* calls the
            submodules determines the order of dimensions and number of axis in the ellipsis.
        """
        self._update()
        self._validate_dataset(dataset.map_names, trajectory_module is not None)

        # If wanted, disable graph construction with tf.function (designed for debugging)
        self.progress_bar.total_voxels.assign(dataset.set_size)

        # Run actual simulation
        k_space_shape = self.get_k_space_shape()
        batched_dataset = dataset(batchsize=voxel_batch_size)
        noise_less_k_space_stack = self._simulation_loop(batched_dataset, k_space_shape,
                                                         trajectory_module, trajectory_signatures,
                                                         additional_kwargs)

        # Act noise_instantiations
        k_space_stack = self.encoding_module.add_noise(noise_less_k_space_stack)

        if unstack_repetitions:
            k_space_stack = self.forward_model.unstack_repetitions(k_space_stack)

        if self.recon_module is not None:
            simulation_result = self._reconstruct(k_space_stack)
        else:
            simulation_result = k_space_stack

        return simulation_result

    def _validate_dataset(self, map_names: Tuple[str], tr_mod: bool):
        # Check dataset inputs for missing parameter maps
        if tr_mod:
            if not all((rq in map_names for rq in self.forward_model.required_quantities if rq != 'r_vectors')):
                raise AssertionError(
                    f'{map_names} does not contain all entries of'
                    f' {self.forward_model.required_quantities}')
        else:
            if not all((rq in map_names for rq in self.forward_model.required_quantities)):
                raise AssertionError(
                    f'{map_names} does not contain all entries of'
                    f' {self.forward_model.required_quantities}')

    def _simulation_loop(self, dataset: tf.data.Dataset, k_space_shape: tf.Tensor, 
                         trajectory_module=None, trajectory_signatures: dict = None,
                         additional_kwargs: dict = None):
        """ Consumes all object-configuration data (images) and simulates the MR images. The
        simulation configuration is
        exclusively defined by the given modules forward_model and encoding. If the optional
        reconstruction module is given, the returned tensor contains images otherwise it will
        return the k-space data.

        :param dataset: tf.Dataset that yields corresponding to the
                        `cmrsim.datasets.BaseDataset.__call__`
        :return: Stack of noise_less k-space-images as tensor with shape
                 (#repetitions, #samples). The returned images are only 3D if the
                  input data, encoding and recon module are 3D as well.
        """
        # Allocate tensor array to store the simulated images
        s_of_k_temp = tf.zeros(k_space_shape, tf.complex64)
        self.progress_bar.reset_voxel()

        s_of_k_temp *= (0. + 0.j)
        # Loop over material points in dataset
        for batch_idx, batch_dict in dataset.enumerate():
            if trajectory_module is not None:
                batch_dict = self._map_trajectories(batch_idx, batch_dict, trajectory_module,
                                                    trajectory_signatures, additional_kwargs)
                # print([f"{k}: {v.shape}" for k, v in batch_dict.items()])
            s_of_k_temp += self._segment_loop(batch_dict)
            self.progress_bar.update(add_voxels=tf.shape(batch_dict['M0'])[0])
            self.progress_bar.print()

        self.progress_bar.print_final()
        return s_of_k_temp

    @tf.function(jit_compile=False, reduce_retracing=True)
    def _segment_loop(self, batch_dict: dict):
        """ Fourier transforms the handed batch of object points / isochromates,

        :param batch_dict: dictionary of type {'property_name': tf.Tensor(...)}
                           e.g. {'M0': tf.Tensor{}}
        :return: tf.Tensor of shape (1, #repetitions, #k-space-samples)
        """
        # Allocate k-space-Tensor
        n_segments = self.encoding_module.k_space_segments.read_value()
        s_of_k_segments = tf.TensorArray(dtype=tf.complex64, size=n_segments, dynamic_size=False)
        self.progress_bar.reset_segments()
 
        # Loop over k-space segments, defined by k-space trajectory in self.encoding_module
        m_transverse = self.forward_model(batch_dict["M0"], segment_index=0, **batch_dict)
        for segment_index in tf.range(n_segments):
            k_space_segment = self.encoding_module(m_transverse, batch_dict['r_vectors'],
                                                   segment_index=segment_index)
            k_space_segment = tf.transpose(k_space_segment, [1, 0])
            s_of_k_segments = s_of_k_segments.write(segment_index, k_space_segment)

            self.progress_bar.update(add_segment=1)
            if tf.math.floormod(segment_index, 5) == 0:
                self.progress_bar.print()

        # Concat all segments and transpose axes to match needed format
        return tf.transpose(s_of_k_segments.concat(), [1, 0])
    
    @staticmethod
    def _map_trajectories(idx: int, batch: dict, trajectory_module,
                          trajectory_signatures: dict, additional_kwargs: dict):
        init_r = batch.pop("initial_positions")
        for k, t in trajectory_signatures.items():
            new_shape = tf.concat([tf.shape(init_r)[0:1], tf.shape(t), [3, ]], axis=0)
            # Iterate over repetitions as for some reason this might cause troubles if tried
            # using the flattened time-samples
            pos, add_lookups = [], []
            for t_ in t:
                p, alup = trajectory_module(initial_positions=tf.reshape(init_r, (-1, 3)), timing=t_, 
                                            **additional_kwargs, batch_index=tf.cast(idx, tf.int32))
                pos.append(p)
                add_lookups.append(alup)
            pos = tf.stack(pos, axis=1)
            pos = tf.reshape(pos, new_shape)
            add_lookups = {k:tf.reshape(tf.stack([alup[k] for alup in add_lookups]),
                                        tf.concat([new_shape[:-1], tf.shape(add_lookups[0][k])]))
                           for k in add_lookups[0].keys()}
            
            batch.update({k: pos})
            batch.update(add_lookups)
        return batch


    def get_k_space_shape(self):
        """ Calculates the expected result shape of the simulated k-space, given the configuration
         of encoding and forward-model modules

        :return: tf.Tensor specifying the shape (#repetitions, #k_space_samples)
        """
        n_reps = tf.cast(self.forward_model.expected_number_of_repetitions, tf.int32)
        n_samples = tf.cast(self.encoding_module.number_of_samples, tf.int32)
        expected_k_space_shape = tf.stack([n_reps, n_samples], axis=0)
        return expected_k_space_shape

    def _reconstruct(self, simulated_k_spaces):
        return self.recon_module(simulated_k_spaces)

    def _update(self):
        """ In case there are dependencies between the modules of the simulation, this function
        offers the entry point to adapt all Variables after changes
        """
        self.forward_model.update()
        self.encoding_module.update()

    def save(self, checkpoint_path: str):
        """ Saves a tf checkpoint of the current simulation configuration
        :param checkpoint_path: str
        """
        checkpoint = tf.train.Checkpoint(model=self)
        checkpoint.write(checkpoint_path)

    @classmethod
    def from_checkpoint(cls, checkpoint_path: str):
        """ Creates instance of the class and loads variables from the specified checkpoint
        :param checkpoint_path: str
        :return: Instance of class
        """
        new_model = cls(build_kwargs=dict())
        new_checkpoint = tf.train.Checkpoint(model=new_model)
        new_checkpoint.restore(checkpoint_path)
        return new_model

    @property
    def configuration_summary(self) -> OrderedDict:
        """ Creates a summary of the configured variables in the submodules as dictionaries
        :return: dict
        """
        summary = OrderedDict()

        temp = {'modules': []}
        for module in self.forward_model.submodules:
            temp['modules'].append(module.name)
            temp.update({module.name: {}})
            for variable in module.variables:
                temp[module.name].update(
                    {variable.name: {'name': variable.name, 'dtype': str(variable.dtype),
                                     'shape': str(variable.shape),
                                     'is_trainable': str(variable.trainable),
                                     'value': variable.numpy().tolist()}})
        summary.update({'forward model': temp})

        summary.update({'encoding': {'name': self.encoding_module.name}})
        for variable in self.encoding_module.variables:
            summary['encoding'].update(
                {variable.name: {'name': variable.name, 'dtype': str(variable.dtype),
                                 'shape': str(variable.shape),
                                 'is_trainable': str(variable.trainable),
                                 'value': variable.numpy().tolist()}})
        return summary

    def write_graph(self, dataset, graph_log_dir: str):
        """ Traces the graph of the simulation for one batch and saves it as graphdef to the
        specified folder

        """
        # If set to True log the graph with tf.summary
        os.makedirs(graph_log_dir, exist_ok=True)
        writer = tf.summary.create_file_writer(graph_log_dir)
        print("Graph Tracing activated...")
        tf.summary.trace_on(graph=True)
        batch_dict, = [_ for _ in dataset(100).take(1)]
        _ = self._segment_loop(batch_dict)

        with writer.as_default():   # pylint: disable not-context-manager
            tf.summary.trace_export(name='graph_def', step=0)
        print(f'\nSaved Graph-definition to {graph_log_dir}')
