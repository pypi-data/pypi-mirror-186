"""  """
import abc
from typing import List, Optional, Tuple

import tensorflow as tf

from cmrsim.analytic import AnalyticSimulation


class SimulationOptimizer(tf.Module):
    """ Module that implements the set-up to optimized the experimental parameters by back -
     propagating gradients from a given loss function to the variables defined in the Simulation
     class. The simulation is defined as a Subclass of 'SimulationBase', which is assigned as
     member of the Simulation Optimizer.

     Conceptually this Module is meant to be subclassed, where the abstract member-function
     `loss_function` needs to be implemented (or monkey-patched). By call
    """
    # Instance of SimulationBase-subclass defining the forward model
    simulator: 'AnalyticSimulation' = None

    def __init__(self, simulator: 'AnalyticSimulation', optimizer: 'tf.keras.optimizers.Optimizer'):
        super(SimulationOptimizer, self).__init__(name="simulation_optimizer")
        self.simulator = simulator
        self._optimizer = optimizer

    # @abc.abstractmethod
    def loss_function(self, prediction: tf.Tensor, label: tf.Tensor) -> tf.Tensor:
        return tf.reduce_mean(tf.abs(prediction))

    @tf.function
    def optimization_step(self, dataset: 'tf.data.Dataset',
                          vars_to_watch_forward: List[tf.Variable],
                          vars_to_watch_recon: List[tf.Variable],
                          points_in_dataset: Optional[int] = -1):
        """

        """
        # Calculate forward simulation and keep track of the jacobians
        ksp, jc_ksp = self._forward_model_with_gradients(dataset, vars_to_watch_forward,
                                                         points_in_dataset)
        jc_ksp = tf.cast(jc_ksp, tf.complex64)
        jc_shape1 = tf.shape(jc_ksp)
        # Flatten all repetitions for jacobian combination
        flat_jc_ksp = tf.reshape(jc_ksp, [jc_shape1[0], -1])

        # Calculate the reconstruction
        with tf.device("CPU:0"):
            recon_image, jc_recon, _ = self._reconstruct_with_gradients(ksp, vars_to_watch_recon)
        flat_jc_recon = tf.reshape(jc_recon, [-1, tf.shape(flat_jc_ksp)[1]])

        loss, jc_loss = self._loss_wrapper(recon_image, 0.)

        total_gradients = jc_loss * tf.reshape(tf.einsum('ij,vj->vi', flat_jc_recon, flat_jc_ksp),
                                               tf.concat([jc_shape1[0:1], tf.shape(jc_loss)], 0))

        reduced_grad_per_var = tf.reduce_mean(total_gradients, axis=(1, -2, -1))
        reduced_grad_per_var = tf.math.real(reduced_grad_per_var) +\
                               tf.math.imag(reduced_grad_per_var)

        # This step will only work if it is inside a tf.function in the case, that a variable
        # to optimize has a partially unknown shape in eager mode
        tf.debugging.assert_equal(tf.shape(reduced_grad_per_var)[0], len(vars_to_watch_forward))
        self._optimizer.apply_gradients(zip(tf.unstack(reduced_grad_per_var),
                                            vars_to_watch_forward))
        return recon_image, loss, total_gradients

    @tf.function
    def _loss_wrapper(self, prediction, label):
        with tf.GradientTape(watch_accessed_variables=False) as loss_tape:
            loss_tape.watch(prediction)
            loss_value = self.loss_function(prediction, label)
        jacobian = loss_tape.jacobian(loss_value, prediction)
        return loss_value, jacobian

    @tf.function
    def _forward_model_with_gradients(self, dataset: tf.data.Dataset,
                                      variables_to_watch: List[tf.Variable],
                                      set_size: Optional[int] = -1) -> Tuple[tf.Tensor, tf.Tensor]:
        """ Calls simulation forward-model similar to implementation as in SimualtionBase but uses
        tf.GradientTape to calculate the jacobian matrix for all variables specified in the
        input arguments.

        :param dataset:
        :param variables_to_watch:
        :param set_size:
        :returns:
        """
        self.simulator.progress_bar.print()
        self.simulator.progress_bar.total_voxels.assign(set_size)
        self.simulator.progress_bar.reset_voxel()

        # Initialize simulation result and jacobian matrix with zeros
        s_of_k_accumulator = tf.zeros(self.simulator.get_k_space_shape(), tf.complex64)
        kspace_jacobians_acc = tf.zeros(tf.concat(([len(variables_to_watch), ],
                                                   self.simulator.get_k_space_shape()),
                                                  0), tf.float32)

        # Summation over all material points of the Fourier-transform
        for batch in dataset:
            self.simulator.progress_bar.reset_segments()

            # Initialize TensorArrays to gather all entries of simulation results and jacobians
            # for all segments. These are stacked after the segment loop
            n_segments = self.simulator.encoding_module.k_space_segments.read_value()
            s_of_k_segments = tf.TensorArray(dtype=tf.complex64, size=n_segments,
                                             dynamic_size=False)
            segment_jacobians = tf.TensorArray(dtype=tf.float32, size=n_segments,
                                               dynamic_size=False)

            # Loop over k-space segments for the given batch of material points
            for segment_index in tf.range(n_segments):
                with tf.GradientTape(watch_accessed_variables=False) as segment_tape:
                    segment_tape.watch(variables_to_watch)
                    m_transverse = self.simulator.forward_model(batch["M0"], **batch,
                                                                segment_index=segment_index)
                    k_space_segment_data = self.simulator.encoding_module(
                                                                    m_transverse,
                                                                    batch['r_vectors'],
                                                                    segment_index=segment_index)

                # Write simulation result and gradients into TensorArrays
                jacobians = segment_tape.jacobian(k_space_segment_data,
                                                  segment_tape.watched_variables())
                # NOTE: this step REQUIRES the forward model variables jacobian to be diagonal,
                # meaning that every entry of the variable ONLY changes the result at #repetition
                # corresponding to it.
                jacobians = tf.reduce_sum(jacobians, axis=-1)

                segment_jacobians = segment_jacobians.write(segment_index, jacobians)
                s_of_k_segments = s_of_k_segments.write(segment_index, k_space_segment_data)

                self.simulator.progress_bar.update(add_segment=1)
                if tf.math.floormod(segment_index, 5) == 0:
                    self.simulator.progress_bar.print()

            # Stack segments data / gradients and add the results to accumulating tensors
            s_of_k_segments = s_of_k_segments.stack()
            segment_jacobians = segment_jacobians.stack()

            s_of_k_segments = tf.reshape(tf.transpose(s_of_k_segments, [0, 1, 2]),
                                         tf.shape(s_of_k_accumulator))
            s_of_k_accumulator += s_of_k_segments

            segment_jacobians = tf.reshape(tf.transpose(segment_jacobians, [0, 1, 2, 3]),
                                           tf.shape(kspace_jacobians_acc))
            kspace_jacobians_acc += segment_jacobians
            self.simulator.progress_bar.update(
                add_voxels=tf.shape(batch["M0"])[0]), self.simulator.progress_bar.print()
        self.simulator.progress_bar.print_final()
        return s_of_k_accumulator, kspace_jacobians_acc

    @tf.function
    def _reconstruct_with_gradients(self, k_space: tf.Tensor,
                                    recon_variables_to_watch: List[tf.Variable]) \
            -> Tuple[tf.Tensor, tf.Tensor, tf.Tensor]:
        """

        :param k_space:
        :param recon_variables_to_watch:
        :returns: (reconstructed image, jacobian wrt kspace, jacobian wrt recon_variables)
        """
        # TODO: Take care of the case were the recon_variables_to_watch is an empty list
        # TODO: as this causes the calculation to crash
        k_space = self.simulator.encoding_module.add_noise(k_space)
        with tf.GradientTape(watch_accessed_variables=False) as recon_tape, \
                tf.GradientTape(watch_accessed_variables=False) as addition_tape:
            recon_tape.watch(k_space), addition_tape.watch(recon_variables_to_watch)
            recon_result = self.simulator.recon_module(k_space)
        jacobian_ksp = recon_tape.jacobian(recon_result, k_space, experimental_use_pfor=False)
        # jacobian_vars = addition_tape.jacobian(recon_result, recon_variables_to_watch,
        #                                        experimental_use_pfor=False)
        # return recon_result, jacobian_ksp, jacobian_vars
        return recon_result, jacobian_ksp, None
