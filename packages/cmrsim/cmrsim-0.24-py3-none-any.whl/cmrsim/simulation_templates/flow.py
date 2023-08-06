"""Contains templates for running special-case flow-simulations"""

__all__ = ["FlowSimulation", "FlowSimulationMultiVenc"]


from typing import TYPE_CHECKING, List

import tensorflow as tf
import numpy as np
from time import perf_counter
from tqdm.notebook import tqdm

from cmrsim.datasets import RefillingFlowDataset
from cmrsim.trajectory import FlowTrajectory, TurbulentTrajectory

if TYPE_CHECKING:
    import cmrsim


# pylint: disable=abtract-method
class FlowSimulation(tf.Module):
    """Performs simulation of a refilling flow over multiple TRs.

    :param flow_dataset:
    :param prep_modules:
    :param readout_module:
    :param contrast_modules:
    :param trajectory_module:
    """
    def __init__(self, flow_dataset: 'RefillingFlowDataset',
                 prep_modules: List['cmrsim.bloch.BaseBlochOperator'],
                 readout_module: 'cmrsim.bloch.BlochReadout',
                 contrast_modules: List['cmrsim.bloch.BaseBlochOperator'] = (),
                 trajectory_module: 'FlowTrajectory' = None):
        super().__init__(name="flow_simulation")
        self.prep_modules = prep_modules
        self.readout_module = readout_module
        self._refilling_dataset = flow_dataset
        self.contrast_modules = contrast_modules

        # Instantiate lookup-module according to the mesh data dataset content
        if trajectory_module is None:
            lookup_table_3d, map_dimensions = self._refilling_dataset.get_lookup_table()
            self.trajectory_module = FlowTrajectory(
                            velocity_field=lookup_table_3d.astype(np.float32),
                            map_dimensions=map_dimensions.astype(np.float32),
                            additional_dimension_mapping=self._refilling_dataset.field_list[1:],
                            device=self.readout_module.device)

        self._index_list = self._check_initializiaton_input()

    def _check_initializiaton_input(self):
        """

        :raises: ValueError if some required properties are not contained in the given dataset
        :raises: ValueError if repetition numbers of specified simulation modules are inconsistent

        :return: List[Iterable[int], ...] for each simulation module specify which repetition index
                 corresponds to which k-space-line
        """
        # Check if all required properties are provided by the dataset:
        required_properties = ["magnetization, M0, T1, T2"]
        for cm in self.contrast_modules + self.prep_modules + [self.readout_module, ]:
            for sm in cm.submodules:
                required_properties.extend(sm.required_quantities)
        required_properties = set(required_properties)

        provided_properties = [v[0] for v in self._refilling_dataset.field_list[1:]]
        provided_properties += self._refilling_dataset.particle_properties

        is_provided = [rq in provided_properties for rq in required_properties]
        if not all(is_provided):
            ValueError(f"Not all required particle properties / lookups are provided by the given"
                       f"Dataset: \n\treq = {required_properties}\n\tprov={provided_properties}")

        # Check if repetition indices of modules are consistent:
        all_rep_indices = [cm.n_repetitions for cm in self.contrast_modules]
        all_rep_indices.append(self.readout_module.n_repetitions)
        indices_one_or_max = [i == 1 or i == max(all_rep_indices) for i in all_rep_indices]
        if not all(indices_one_or_max):
            raise ValueError("Repetitions of specified modules are not consistent: "
                             f"Constraint matched: {indices_one_or_max} for given"
                             f" repetitions: {all_rep_indices}")
        repetition_indices = [range(i) if i == max(all_rep_indices)
                              else [0, ] * max(all_rep_indices) for i in all_rep_indices]
        return repetition_indices

    def __call__(self, particle_density: float = 0.1, dropping_distance: float = 0.05,
                 averages: int = 1, reseed_threshold: float = 0.25, 
                 use_inital_filling: bool = True, initial_filling_dict: dict = None,
                 return_final_magnetization: bool = False):
        """

        :param particle_density:
        :param dropping_distance:
        :param averages:
        :param reseed_threshold:
        :param use_inital_filling:
        :param initial_filling_dict:
        :param return_final_magnetization:
        :return:
        """

        for av in tqdm(range(averages), desc="Loop over averages"):
            if use_inital_filling:
                r, properties = self._refilling_dataset.initial_filling(
                                                            particle_density=particle_density,
                                                            slice_dictionary=initial_filling_dict)
                m = properties.pop("magnetization")
            else:
                r, properties, _ = self._refilling_dataset(particle_density)
                m = properties.pop("magnetization")

            for prep in tqdm(range(len(self.prep_modules)),
                             desc="Looping Over Prep Modules", leave=False):
                prep_module = self.prep_modules[prep]

                pbar = tqdm(range(prep_module.n_repetitions),
                            desc="Running Simulation - Prep Modules", leave=False)

                for k_line_index in pbar:
                    start = perf_counter()

                    m, r_new = prep_module(magnetization=m,
                                           trajectory_module=self.trajectory_module,
                                           initial_position=r, repetition_index=k_line_index,
                                           **properties)

                    displacements = np.linalg.norm(r - r_new, axis=-1) * 1000

                    properties["magnetization"] = m.numpy()

                    mid = perf_counter()

                    r, properties, _ = self._refilling_dataset(particle_density=particle_density,
                                                               residual_particle_pos=r_new.numpy(),
                                                               particle_properties=properties,
                                                               distance_tolerance=dropping_distance,
                                                               reseed_threshold=reseed_threshold)
                    m = properties.pop("magnetization")
                    end = perf_counter()

                    n_reused_particles = _[0].shape[0] if _ is not None else 0
                    pbar.set_postfix_str(
                        f"Particles Reused: {n_reused_particles}/{r.shape[0]}  // "
                        f" New vs. Drop: {self._refilling_dataset.n_new}/"
                        f"{self._refilling_dataset.n_drop}  // "
                        f" Density: {self._refilling_dataset.mean_density: 1.3f}/mm^3 // "
                        f" Durations: {mid - start:1.3f} | {end - mid:1.3f} // "
                        f" Displacements: {np.mean(displacements):1.1f}"
                        f"+-{np.std(displacements):1.2f} mm"
                    )

            pbar = tqdm(range(len(self.readout_module.time_signal_acc)),
                        desc="Running Simulation - Readout", leave=False)

            for k_line_index in pbar:
                start = perf_counter()
                m, r_new = self._call_core(m, r, properties, k_line_index)
                displacements = np.linalg.norm(r - r_new, axis=-1) * 1000

                properties["magnetization"] = m.numpy()

                mid = perf_counter()

                r, properties, _ = self._refilling_dataset(particle_density=particle_density,
                                                           residual_particle_pos=r_new.numpy(),
                                                           particle_properties=properties,
                                                           distance_tolerance=dropping_distance,
                                                           reseed_threshold=reseed_threshold)
                m = properties.pop("magnetization")
                end = perf_counter()

                n_reused_particles = _[0].shape[0] if _ is not None else 0
                pbar.set_postfix_str(
                    f"Particles Reused: {n_reused_particles}/{r.shape[0]}  // "
                    f" New vs. Drop: {self._refilling_dataset.n_new}/"
                    f"{self._refilling_dataset.n_drop}  // "
                    f" Density: {self._refilling_dataset.mean_density: 1.3f}/mm^3 // "
                    f" Durations: {mid - start:1.3f} | {end - mid:1.3f} // "
                    f" Displacements: {np.mean(displacements):1.1f}+-{np.std(displacements):1.2f}mm"
                )
        if return_final_magnetization:
            return r, m

    def _call_core(self, magnetization_init, r_init, batch, k_line_index):
        m, r = magnetization_init, r_init
        
        # contrast Modules
        for mod_idx, c_module in enumerate(self.contrast_modules):
            m, r = c_module(magnetization=m,
                            trajectory_module=self.trajectory_module,
                            initial_position=r,
                            repetition_index=self._index_list[mod_idx][k_line_index],
                            **batch)
        # Readout Module
        m, r = self.readout_module(magnetization=m, trajectory_module=self.trajectory_module,
                                   initial_position=r, repetition_index=k_line_index,
                                   **batch)
        return m, r


# pylint: disable=abtract-method
class FlowSimulationMultiVenc(tf.Module):
    """Performs simulation of a refilling flow over multiple TRs while using multiple waveforms
    in parallel.

    :param flow_dataset:
    :param prep_modules:
    :param readout_modules:
    :param trajectory_module:
    """
    def __init__(self, flow_dataset: 'RefillingFlowDataset',
                 prep_modules: List['cmrsim.bloch.BaseBlochOperator'],
                 readout_modules: List['cmrsim.bloch.BlochReadout'],
                 trajectory_module: 'FlowTrajectory' = None):

        super(FlowSimulationMultiVenc, self).__init__(name="flow_simulation")
        self.prep_modules = prep_modules
        self.readout_modules = readout_modules
        self._refilling_dataset = flow_dataset

        # Instantiate lookup-module according to the mesh data dataset content
        if trajectory_module is None:
            lookup_table_3d, map_dimensions = self._refilling_dataset.get_lookup_table()
            self.trajectory_module = FlowTrajectory(
                velocity_field=lookup_table_3d.astype(np.float32),
                map_dimensions=map_dimensions.astype(np.float32),
                additional_dimension_mapping=self._refilling_dataset.field_list[1:],
                device=self.readout_modules[0].device)
        else:
            self.trajectory_module = trajectory_module

        self._index_list = self._check_initializiaton_input()

    def _check_initializiaton_input(self):
        """
        :raises: ValueError if some required properties are not contained in the given dataset
        :raises: ValueError if repetition numbers of specified simulation modules are inconsistent
        :return: List[Iterable[int], ...] for each simulation module specify which repition index
                 corresponds to which k-space-line
        """
        # Check if all required properties are provided by the dataset:
        required_properties = ["magnetization, M0, T1, T2"]
        for cm in self.prep_modules + self.readout_modules:
            for sm in cm.submodules:
                required_properties.extend(sm.required_quantities)
        required_properties = set(required_properties)

        provided_properties = [v[0] for v in self._refilling_dataset.field_list[1:]]
        provided_properties += self._refilling_dataset.particle_properties

        is_provided = [rq in provided_properties for rq in required_properties]
        if not all(is_provided):
            ValueError(f"Not all required particle properties / lookups are provided by the given"
                       f"Dataset: \n\treq = {required_properties}\n\tprov={provided_properties}")

        # Check if repetition indices of modules are consistent:
        all_rep_indices = [rm.n_repetitions for rm in self.readout_modules]
        indices_one_or_max = [i == 1 or i == max(all_rep_indices) for i in all_rep_indices]
        if not all(indices_one_or_max):
            raise ValueError("Repetitions of specified modules are not consistent: "
                             f"Constraint matched: {indices_one_or_max} for given"
                             f" repetitions: {all_rep_indices}")
        repetition_indices = [range(i) if i == max(all_rep_indices)
                              else [0, ] * max(all_rep_indices) for i in all_rep_indices]
        return repetition_indices

    def __call__(self, particle_density: float = 0.1, dropping_distance: float = 0.05,
                 averages: int = 1, reseed_threshold: float = 0.25,
                 use_inital_filling: bool = True, initial_filling_dict: dict = None,
                 return_final_magnetization: bool = False):
        """ Evals

        :param particle_density:
        :param dropping_distance:
        :param averages:
        :param reseed_threshold:
        :param use_inital_filling:
        :param initial_filling_dict:
        :param return_final_magnetization:
        :return:
        """

        for av in tqdm(range(averages), desc="Loop over averages"):
            if use_inital_filling:
                r, properties = self._refilling_dataset.initial_filling(
                                                            particle_density=particle_density,
                                                            slice_dictionary=initial_filling_dict)
                m = properties.pop("magnetization")
            else:
                r, properties, _ = self._refilling_dataset(particle_density)
                m = properties.pop("magnetization")

            # initialize turbulence velocities for new particles if turbulence trajectory is used
            if isinstance(self.trajectory_module, TurbulentTrajectory):
                self.trajectory_module.warmup_step(particle_positions=r)

            for prep in tqdm(range(len(self.prep_modules)),
                             desc="Looping Over Prep Modules", leave=False):
                prep_module = self.prep_modules[prep]

                pbar = tqdm(range(prep_module.n_repetitions),
                            desc="Running Simulation - Prep Modules", leave=False)

                for k_line_index in pbar:
                    start = perf_counter()

                    m, r_new = prep_module(magnetization=m,
                                           trajectory_module=self.trajectory_module,
                                           initial_position=r, repetition_index=k_line_index,
                                           **properties)

                    displacements = np.linalg.norm(r - r_new, axis=-1) * 1000

                    properties["magnetization"] = m.numpy()

                    mid = perf_counter()

                    r, properties, in_tol = self._refilling_dataset(
                                                            particle_density=particle_density,
                                                            residual_particle_pos=r_new.numpy(),
                                                            particle_properties=properties,
                                                            distance_tolerance=dropping_distance,
                                                            reseed_threshold=reseed_threshold)

                    if isinstance(self.trajectory_module, TurbulentTrajectory):
                        n_new = self._refilling_dataset.n_new0
                        self.trajectory_module.turbulence_reseed_update(
                                            in_tol, new_particle_positions=r[-n_new:, :])
                        
                    m = properties.pop("magnetization")
                    end = perf_counter()

                    n_reused_particles = _[0].shape[0] if _ is not None else 0
                    pbar.set_postfix_str(
                        f"Particles Reused: {n_reused_particles}/{r.shape[0]}  // "
                        f" New vs. Drop: {self._refilling_dataset.n_new}/"
                        f"{self._refilling_dataset.n_drop}  // "
                        f" Density: {self._refilling_dataset.mean_density: 1.3f}/mm^3 // "
                        f" Durations: {mid - start:1.3f} | {end - mid:1.3f} // "
                        f" Displacements: {np.median(displacements):1.1f},"
                        f"({np.percentile(displacements,97):1.2f},"
                        f"{np.percentile(displacements,3):1.2f}) mm"
                    )

            pbar = tqdm(range(len(self.readout_modules)),
                        desc="Running Simulation - Readout", leave=False)

            m = tf.repeat(m[tf.newaxis, ...], self.readout_modules[0].n_repetitions, axis=0)

            for bloch_mod_index in pbar:
                start = perf_counter()

                bloch_module = self.readout_modules[bloch_mod_index]

                m_all, r_new = bloch_module(magnetization=m,
                                            trajectory_module=self.trajectory_module,
                                            initial_position=r,
                                            run_parallel=True, **properties)

                displacements = np.linalg.norm(r - r_new, axis=-1) * 1000

                properties["magnetization"] = m_all[0].numpy()

                mid = perf_counter()

                r, properties, in_tol = self._refilling_dataset(
                                                            particle_density=particle_density,
                                                            residual_particle_pos=r_new.numpy(),
                                                            particle_properties=properties,
                                                            distance_tolerance=dropping_distance,
                                                            reseed_threshold=reseed_threshold)
                n_new = self._refilling_dataset.n_new
                m_new = properties.pop("magnetization")[-n_new:]
                m = np.concatenate((np.take(m_all, in_tol[0], axis=1),
                                    np.repeat(m_new[np.newaxis, ...], np.shape(m_all)[0], axis=0)),
                                    axis=1)

                if isinstance(self.trajectory_module, TurbulentTrajectory):
                    self.trajectory_module.turbulence_reseed_update(
                                                in_tol, new_particle_positions=r[-n_new:, :])

                end = perf_counter()

                n_reused_particles = in_tol[0].shape[0] if in_tol is not None else 0
                pbar.set_postfix_str(
                    f"Particles Reused: {n_reused_particles}/{r.shape[0]}  // "
                    f" New vs. Drop: {self._refilling_dataset.n_new}/"
                    f"{self._refilling_dataset.n_drop}  // "
                    f" Density: {self._refilling_dataset.mean_density: 1.3f}/mm^3 // "
                    f" Durations: {mid - start:1.3f} | {end - mid:1.3f} // "
                    f" Displacements: {np.median(displacements):1.1f},"
                    f"({np.percentile(displacements,97):1.2f},"
                    f"{np.percentile(displacements,3):1.2f}) mm"
                )
        if return_final_magnetization:
            return r, m

    def _call_core(self, magnetization_init, r_init, batch, k_line_index):
        m, r = magnetization_init, r_init

        # Readout Module
        m, r = self.readout_module(magnetization=m, trajectory_module=self.trajectory_module,
                                   initial_position=r, repetition_index=k_line_index,
                                   **batch)
        return m, r
