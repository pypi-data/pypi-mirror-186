"""Contains convenience implementations to handle mesh-inputs"""

__all__ = ["MeshDataset", "CardiacMeshDataset"]

import os
from typing import List, Union, Tuple, Iterable

import pyvista
import numpy as np
from tqdm.notebook import tqdm
from pint import Quantity
import vtk
from scipy import interpolate


class MeshDataset:
    """This class bundles basic functionality to handles dynamic meshes and implements convenience
    functionality like rendering or slice selection.

    :param mesh: pyvista mesh containing the field-array 'displacement_{time}ms' for each
                    time specified in timing_ms
    :param timing_ms: array containing the times corresponding to the stored displacements
    """
    #: Mesh containing the displacements for each time-point
    mesh: Union[pyvista.UnstructuredGrid, pyvista.DataSet]
    #: Time points corresponding to the mesh states given by the list of files in ms
    timing: np.ndarray

    def __init__(self, mesh: Union[pyvista.UnstructuredGrid, pyvista.DataSet],
                 timing_ms: np.ndarray):
        self.mesh = mesh
        self.timing = timing_ms

    def add_data_per_time(self, scalars: np.array, name: str):
        """ Adds a scalar field array for each time-stamp

        :param scalars: (t, #p, ...)
        :param name: name of the scalar
        """
        for timing, value in zip(self.timing, scalars):
            self.mesh[f"{name}_{timing}ms"] = value

    def transform_vectors(self, time_stamps: np.ndarray, vector_names: List[str],
                          reference_time: Quantity = None, rotation_only: bool = True):
        """Evalutes the deformation matrix for ref-timing -> time_stamps and applies the
        transformation to the vector arrays of specified names in the mesh. Results are stored
        as vector field in self.mesh.

        :param time_stamps:
        :param vector_names: Names of properties that are transformed
        :param reference_time: Time that correspond to the definition of the vectors
        :param rotation_only: If true the transformation includes a normalization, thus results in a
                rotation only.
        """
        reference_positions = self.get_positions_at_time(reference_time)

        # pylint: disable=E1101
        deformation_mesh = pyvista.UnstructuredGrid(
            {vtk.VTK_TETRA: self.mesh.cell_connectivity.reshape(-1, 4)},
            reference_positions)

        # Apply transformation for all time steps
        for tstamp in tqdm(time_stamps, desc="Computing deformation matrices", leave=False):

            # Compute the deformation matrix on the mesh serving as transformation
            disps_at_timestamp = self.mesh[f"displacements_{tstamp}ms"]
            for idx, direction in enumerate("xyz"):
                deformation_mesh[f"disp{direction}"] = disps_at_timestamp[:, idx]
                deformation_mesh = deformation_mesh.compute_derivative(
                    scalars=f"disp{direction}",
                    gradient=f"d{direction}_dxyz")
                deformation_mesh[f"d{direction}_dxyz"][
                    np.logical_not(np.isfinite(deformation_mesh[f"d{direction}_dxyz"]))] = 0

            nabla_u = np.stack([deformation_mesh["dx_dxyz"], deformation_mesh["dy_dxyz"],
                                deformation_mesh["dz_dxyz"]], axis=1)
            deformation_matrix = nabla_u + np.eye(3, 3).reshape(1, 3, 3)

            # Apply all transformations and store result in self.mesh
            for vec_name in vector_names:
                self.mesh[f"{vec_name}_{tstamp}ms"] = np.einsum("nji, nj -> ni",
                                                                deformation_matrix,
                                                                self.mesh[vec_name])
                if rotation_only:
                    norm = np.linalg.norm(self.mesh[f"{vec_name}_{tstamp}ms"], axis=-1,
                                          keepdims=True)
                    self.mesh[f"{vec_name}_{tstamp}ms"] /= norm

    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-locals
    def render_input_animation(self, filename: str, plotter: pyvista.Plotter = None,
                               scalar: str = None, vector: str = None,
                               start: Quantity = Quantity(0., "ms"),
                               end: Quantity = None, mesh_kwargs: dict = None,
                               vector_kwargs: dict = None,
                               text_kwargs: dict = None) -> None:
        """ Renders an animation of the contained mesh using the displacements. Depending
        on specified arguments, renders vectors/scalars stored as '{name}_{t}ms' in the mesh.

        :param filename: Filename/path where the result is stored
        :param plotter: Optional - if specified, this pyvista.Plotter is used to render the
                            animation
        :param scalar: Optional - if specified, the mesh is plotted using this scalar as color,
                        assuming that for all time-stamps a scalar quantity is stored as field_data
                        as '{name}_{t}ms'
        :param vector: Optional - if specified, additional vectors starting at mesh nodes are
                        rendered, assuming that for all time-stamps a vector quantity is stored
                        as field_data as '{name}_{t}ms'
        :param start: Defines the start time for animation.
        :param end: Defines the end time for animation.
        :param mesh_kwargs: keyword arguments forwarded to plotter.add_mesh(..., **mesh_kwargs).
                        See pyvista reference for more detail
        :param vector_kwargs: defaults to {"mag": 1e-3}. Keyword arguments forwarded to
                        plotter.add_arrows(..., **vector_kwargs). See reference for more detail.
        :param text_kwargs: defaults to dict(position='upper_right', color='white', shadow=False,
                        font_size=26). Keyword arguments forwarded to plotter.add_text(...).
        """
        plotting_mesh = self.mesh.copy()

        index_start = np.searchsorted(self.timing, start.m_as("ms"))
        reference_position = np.array(plotting_mesh.points)
        initial_position = (reference_position +
                            plotting_mesh[f"displacements_{self.timing[index_start]}ms"])

        if scalar is not None:
            plotting_mesh.set_active_scalars(f"{scalar}_{self.timing[index_start]}ms")

        if mesh_kwargs is None:
            mesh_kwargs = {}
        if vector_kwargs is None:
            vector_kwargs = dict(mag=1e-3)
        if text_kwargs is None:
            text_kwargs = dict(position='upper_right', color='white', shadow=False, font_size=26)

        if end is None:
            index_end = -1
        else:
            index_end = np.searchsorted(self.timing, end.m_as("ms"), side="right")

        if plotter is None:
            plotter = pyvista.Plotter(off_screen=True)

        plotting_mesh.points = initial_position
        plotter.add_mesh(plotting_mesh, **mesh_kwargs)

        plotter.open_gif(f"{filename}.gif")
        pbar = tqdm(self.timing[index_start:index_end],
                    desc=f"Rendering Mesh-Animation from {self.timing[index_start]:1.3f}"
                         f" ms to {self.timing[index_end]:1.3f} ms")
        for timing in pbar:
            text_actor = plotter.add_text(f"{timing: 1.2f} ms", **text_kwargs)
            plotter.update_coordinates(reference_position +
                                       plotting_mesh[f"displacements_{timing}ms"],
                                       mesh=plotting_mesh, render=False)
            if scalar is not None:
                pbar.set_postfix_str(f"Update scalar with: {scalar}_{self.timing[index_start]}ms")
                plotter.update_scalars(plotting_mesh[f"{scalar}_{timing}ms"],
                                       mesh=plotting_mesh,
                                       render=False)
            if vector is not None:
                arrow_actor = plotter.add_arrows(
                    cent=reference_position + plotting_mesh[f"displacements_{timing}ms"],
                    direction=plotting_mesh[f"{vector}_{timing}ms"],
                    **vector_kwargs
                )

            plotter.render()
            plotter.write_frame()
            plotter.remove_actor(text_actor)
            if vector is not None:
                plotter.remove_actor(arrow_actor)

        plotter.close()

    def get_positions_at_time(self, time: Quantity) -> np.ndarray:
        """ Returns mesh nodes at the closest match to time argument

        :param time: Quantity
        :return: positions at given time
        """
        if time is not None:
            index_start = np.searchsorted(self.timing, time.m_as("ms"))
            reference_position = (self.mesh.points +
                                  self.mesh[f"displacements_{self.timing[index_start]}ms"])
        else:
            reference_position = np.array(self.mesh.points)
        return reference_position

    def probe_reference(self, reference_mesh: pyvista.UnstructuredGrid,
                        field_names: List[str], reference_time: Quantity = None):
        """ Probes the reference mesh with the points of self.mesh at reference time and stores
        the probed fields matching the given names into self.mesh.

        :param reference_mesh:
        :param field_names:
        :param reference_time:
        :return:
        """
        reference_positions = self.get_positions_at_time(reference_time)

        # pylint: disable=E1101
        probing_mesh = pyvista.UnstructuredGrid(
            {vtk.VTK_TETRA: self.mesh.cell_connectivity.reshape(-1, 4)},
            reference_positions)
        probing_mesh = reference_mesh.probe(probing_mesh)
        for name in field_names:
            self.mesh[name] = probing_mesh[name]

    def get_field(self, field_name: str, timing_indices: Iterable[int] = None) \
            -> (Quantity, np.ndarray):
        """ Gets the specified field at all given time-indices and returns a stacked array.
        Assumes the field to be stored as '{field_name}_{t}ms'.

        :param field_name: str
        :param timing_indices: integers indexing self.timing
        :return:
        """
        if timing_indices is not None:
            times = Quantity([self.timing[t] for t in timing_indices], "ms")
        else:
            times = Quantity(self.timing, "ms")
        field_arr = np.stack([self.mesh[f"{field_name}_{t}ms"] for t in times.m], axis=0)
        return times, field_arr

    def select_slice(self, slice_position: Quantity, slice_normal: np.ndarray,
                     slice_thickness: Quantity, reference_time: Quantity) \
            -> pyvista.UnstructuredGrid:
        """Filters all mesh nodes by position and returns an unstructured grid that contains
         only the nodes within the specified slice definition at the reference.

        :param slice_position: (3, ) vector denoting the slice position
        :param slice_normal: (3, ) vector denoting the normal vector of the slice
                    (is normalized internally)
        :param slice_thickness: Thickness of the selected slice (along the slice_normal)
        :param reference_time:
        :return: mesh containing only the cell being inside the specified slice
        """
        time_idx = np.searchsorted(self.timing, reference_time.m_as("ms"), side="right")
        all_points = (self.mesh.cell_centers().points
                      + self.mesh.ptc()[f"displacements_{self.timing[time_idx]}ms"])
        slice_normal = slice_normal / np.linalg.norm(slice_normal)
        slice_position = slice_position.m_as("m")
        distance = np.einsum("ni, i", all_points - slice_position[np.newaxis, :], slice_normal)
        in_slice = np.abs(distance) < slice_thickness.m_as("m") / 2
        mesh_copy = self.mesh.copy()
        current_slice = mesh_copy.remove_cells(np.where(np.logical_not(in_slice)),
                                               inplace=True)
        current_slice.reference_time = reference_time
        return current_slice

    def get_trajectories(self, start: Quantity, end: Quantity) -> Tuple[Quantity, Quantity]:
        """ Returns available times and positions between specified start-end

        :param start: Quantity
        :param end: Quantity
        :return: time (t, ), positions (N, t, 3)
        """
        time_idx_start = np.searchsorted(self.timing, start.m_as("ms"), side="right")
        time_idx_end = np.searchsorted(self.timing, end.m_as("ms"), side="right")
        time = Quantity(self.timing[time_idx_start:time_idx_end], "ms")
        positions = Quantity(np.stack([self.mesh.points + self.mesh[f"displacements_{t}ms"]
                                       for t in time.m], axis=1), "m")
        return time, positions


class CardiacMeshDataset(MeshDataset):
    """ Cardiac mesh model assuming the continuous node-ordering:

            [apex, n_points_per_ring(1st slice, 1st shell), n_points_per_ring(2st slice, 1st shell),
            ..., n_points_per_ring(1st slice, 2nd shell)]

        shell --> radial
        slice --> longitudinal


    :param mesh: pyvista mesh containing the field-array 'displacement_{time}ms' for each
                time specified in timing_ms
    :param mesh_numbers: (shells, circ, long)
    :param timing_ms: array containing the times corresponding to the stored displacements
    """
    #: (n_shells, n_points_per_ring, n_slices)
    mesh_numbers: Tuple[int, int, int]

    def __init__(self, mesh: Union[pyvista.UnstructuredGrid, pyvista.DataSet],
                 mesh_numbers: (int, int, int),
                 timing_ms: np.ndarray):
        super().__init__(mesh, timing_ms)
        self.mesh_numbers = mesh_numbers

    # pylint: disable=too-many-arguments
    @classmethod
    def from_list_of_arrays(cls, initial_mesh: pyvista.DataSet, mesh_numbers: (int, int, int),
                            list_of_files: List, timing: Quantity, time_precision_ms: int = 1):
        """ Loads a mesh and its displacements from a list of numpy files each containing the
        positional vectors for all points in initial_mesh.

        :raises: FileNotFoundError - if not all files in given list of files exist

        :param initial_mesh: Initial mesh configuration
        :param mesh_numbers: (shells, circ, long)
        :param list_of_files: List of .npy containing the position of all mesh nodes per time
        :param timing:
        :param time_precision_ms: number of decimals used in the field name and timepoints
                                        (e.g. displacements_0.01ms)
        """
        # Make sure all file exist before starting to load all of them
        files_exist = [os.path.exists(f) for f in list_of_files]
        if not all(files_exist):
            n_not_found = len(list_of_files) - sum(files_exist)
            non_existent_files = "\n\t".join([f for f, exists in zip(list_of_files, files_exist)
                                              if not exists])
            raise FileNotFoundError(f"Could not find {n_not_found} files:\n\t {non_existent_files}")

        timing_ms = np.around(timing.m_as("ms"), decimals=time_precision_ms)
        initial_mesh[f"displacements_{timing_ms[0]}ms"] = np.zeros_like(initial_mesh.points)
        for file, time in tqdm(zip(list_of_files[1:], timing_ms[1:]), desc="Loading Files... ",
                               total=len(list_of_files)):
            temp_rvecs = np.load(file)
            initial_mesh[f"displacements_{time}ms"] = temp_rvecs - initial_mesh.points
        return cls(initial_mesh, timing_ms=timing_ms, mesh_numbers=mesh_numbers)

    # pylint: disable=too-many-arguments
    @classmethod
    def from_list_of_meshes(cls, list_of_files: List, timing: Quantity,
                            mesh_numbers: (int, int, int), field_key: str = "displacement",
                            time_precision_ms: int = 1) -> 'CardiacMeshDataset':
        """ Loads vti/vtk files that contain the motion states of the same mesh, calculates
        the displacements from positional differences and returns a CardicMeshDataset instance
        containing the displacements

        :raises: FileNotFoundError - if not all files in given list of files exist

        :param list_of_files: List of .vtk or .vti files each containing a mesh in which the
                              displacement vectors for each node is stored under the name of
                              specified by the argument field_key
        :param timing:
        :param mesh_numbers: (shells, circ, long)
        :param field_key: key to extract
        :param time_precision_ms: number of decimals used in the field name and timepoints
                                        (e.g. displacements_0.01ms)
        """

        # Make sure all file exist before starting to load all of them
        files_exist = [os.path.exists(f) for f in list_of_files]
        if not all(files_exist):
            n_not_found = len(list_of_files) - sum(files_exist)
            non_existent_files = "\n\t".join([f for f, exists in zip(list_of_files, files_exist)
                                              if not exists])
            raise FileNotFoundError(f"Could not find {n_not_found} files:\n\t {non_existent_files}")

        # Load initial vtk file and add all displacements to the mesh as field array
        mesh = pyvista.read(list_of_files[0])
        timing_ms = np.around(timing.m_as("ms"), decimals=time_precision_ms)
        mesh[f"displacements_{timing_ms[0]}ms"] = np.zeros_like(mesh.points)
        for file, time in tqdm(zip(list_of_files[1:], timing_ms[1:]), desc="Loading Files... ",
                               total=len(list_of_files) - 1):
            temp_mesh = pyvista.read(file)
            mesh[f"displacements_{time}ms"] = temp_mesh[field_key]
        return cls(mesh, timing_ms=timing_ms, mesh_numbers=mesh_numbers)

    @classmethod
    def from_single_vtk(cls, file_name: str, mesh_numbers: (int, int, int),
                        time_precision_ms: int = 3):
        """ Loads a vtk-file that contains the displacements

        :param file_name:
        :param mesh_numbers: (shells, circ, long)
        :param time_precision_ms: number of decimals used in the field name and timepoints
                                        (e.g. displacements_0.01ms)
        :return:
        """
        mesh = pyvista.read(file_name)
        timings = [float(t.replace("displacements_", "").replace("ms", "")) for t
                   in mesh.array_names if "displacements" in t]
        timings.sort()
        timings = np.around(np.array(timings), decimals=time_precision_ms)
        return cls(mesh, timing_ms=timings, mesh_numbers=mesh_numbers)

    def compute_local_basis(self, time_stamp: Quantity,
                            keys: Tuple[str, str, str] = ("e_t", "e_c", "e_l")):
        """ Computes the local coordinate system (radial, circumferential, longitudinal) for
        a left ventricle mesh. The local basis vectors per point are stored with specified keys

        :param time_stamp: time Quantity used to determine reference mesh configuration
        :param keys: array names used to store (radial, circumferential, longitudinal) basis vectors
        """
        positions = self.get_positions_at_time(time_stamp)
        local_basis = self._compute_local_basis(positions,
                                                [self.mesh_numbers[i] for i in (0, 2, 1)])
        local_basis = [local_basis[k] for k in ("e_r", "e_c", "e_l")]
        for key, value in zip(keys, local_basis):
            self.mesh[key] = value

    def compute_cylinder_coords(self, time_stamp: Quantity):
        """ Computes cylinder coordinates (transmural_depth, polar_angle, z-pos) for all mesh nodes.

        :param time_stamp: time Quantity used to determine reference mesh configuration
        """
        positions = self.get_positions_at_time(time_stamp)
        cyl_coords = self.evaluate_cylinder_coordinates(
            positions,
            n_shells=self.mesh_numbers[0],
            points_per_shell=1 + self.mesh_numbers[1] * self.mesh_numbers[2])

        self.mesh["transmural_depth"] = cyl_coords[..., 0]
        self.mesh["polar_angle"] = cyl_coords[..., 1]
        self.mesh["z-pos"] = cyl_coords[..., 2]

    # pylint: disable=too-many-locals
    def refine(self, longitudinal_factor: int, circumferential_factor: int, radial_factor: int) \
            -> 'CardiacMeshDataset':
        """ Refines the cardiac mesh model assuming the continuous node-ordering:

            [apex, n_points_per_ring(1st slice, 1st shell), n_points_per_ring(2st slice, 1st shell),
            ..., n_points_per_ring(1st slice, 2nd shell)]

        shell --> radial
        slice --> longitudinal

        :param longitudinal_factor: nl_new = f * nl_old
        :param circumferential_factor: nc_new = n
        :param radial_factor:
        :return: New CardiacMeshDataset instance with refined mesh and new in
        """
        n_shells, n_points_per_ring, n_slices = self.mesh_numbers
        original_ref_points = self.mesh.points + self.mesh[f"displacements_{self.timing[0]}ms"]
        refined_ref_positions, new_dimensions = self.interpolate_mesh(
            original_ref_points,
            points_per_ring=n_points_per_ring,
            n_shells=n_shells, n_slices=n_slices,
            interp_factor_c=circumferential_factor,
            interp_factor_l=longitudinal_factor,
            interp_factor_r=radial_factor)

        connectivity = self.evaluate_connectivity(*new_dimensions)

        # pylint: disable=E1101
        new_mesh = pyvista.UnstructuredGrid({vtk.VTK_TETRA: connectivity}, refined_ref_positions)
        refined_ref_positions = np.array(new_mesh.points)

        for idx, timing in tqdm(enumerate(self.timing), total=len(self.timing),
                                desc=f"Refining mesh by factors: l={longitudinal_factor}, "
                                     f"c={circumferential_factor}, r={radial_factor}"):
            original_points = self.mesh.points + self.mesh[f"displacements_{self.timing[idx]}ms"]
            refined_positions, new_mesh_numbers = self.interpolate_mesh(
                original_points, points_per_ring=n_points_per_ring,
                n_shells=n_shells, n_slices=n_slices,
                interp_factor_c=circumferential_factor,
                interp_factor_l=longitudinal_factor,
                interp_factor_r=radial_factor)
            new_mesh[f"displacements_{timing}ms"] = refined_positions - refined_ref_positions
        new_dataset = CardiacMeshDataset(new_mesh, new_mesh_numbers, self.timing)
        return new_dataset

    @staticmethod
    def interpolate_mesh(mesh_points: np.ndarray, points_per_ring: int = 40, n_shells: int = 4,
                         n_slices: int = 30, interp_factor_c: int = 1, interp_factor_l: int = 1,
                         interp_factor_r: int = 1) -> (np.ndarray, Tuple[int, int, int]):
        """ Function to linear interpolate points of LV meshes in circular, longitudinal and
         radial direction. Indexing of the points is assumed to adhere to the following structure:
                 0th element -> Apex
                 1:points_per_ring+1 -> inner most shell most apical slice.
                 Repeated for n_slices.
                 Repeated for n_shells.

        :param mesh_points: np.ndarray - (-1, 3) Flattened array of 3D positional vectors of
                            mesh points.
        :param points_per_ring: (int) number of points per ring (circumferential direction)
        :param n_shells: (int) number of shells (radial direction)
        :param n_slices: (int) number of slices (longitudinal direction)
        :param interp_factor_c: (int) interpolation multiplier for circumferential direction
        :param interp_factor_l: (int) interpolation multiplier for longitudinal direction
        :param interp_factor_r: (int) interpolation multiplier for radial direction
        :returns: np.ndarray - (n_shell_new, 1 + (n_theta_new*n_slices_new), 3),
                    (n_theta_new, n_slices_new, n_shells_new)
        """

        points_per_shell = 1 + points_per_ring * n_slices
        all_points_per_shell = np.stack(
            [mesh_points[i * points_per_shell:(i + 1) * points_per_shell] for i in range(n_shells)])

        points_per_shell_interp_c, new_n_theta = CardiacMeshDataset._interp_circ(
            all_points_per_shell, interp_factor_c,
            points_per_ring, n_slices)

        points_per_shell_interp_cl, new_n_slices = CardiacMeshDataset._interp_long(
            points_per_shell_interp_c,
            interp_factor_l, new_n_theta)

        points_per_shell_interp_clr, new_n_shells = CardiacMeshDataset._interp_radial(
            np.stack(points_per_shell_interp_cl, axis=0),
            interp_factor_r)

        return points_per_shell_interp_clr.reshape(-1, 3), (new_n_theta, new_n_slices, new_n_shells)

    @staticmethod
    def _interp_circ(mesh_layers: np.ndarray, factor: int = 4, points_per_ring: int = 40,
                     n_slices: int = 30) -> (np.ndarray, int):
        """ Interpolates mesh in circumferential direction. As the last interval on a ring in larger
        than the rest, an additional point is inserted there, even if the interpolation factor is 1.
        This results in new_points_per_ring = points_per_ring * factor + 1.

        :param mesh_layers: (n_shells, points_per_ring * n_slices + 1, 3)
        :param factor: (int) interpolation multiplier
        :param points_per_ring: (int) number of points per ring for input argument mesh_layers
        :param n_slices: (int) number of slices for input argument mesh_layers
        :returns: (n_shells, new_points_per_ring * n_slices + 1, 3), new_points_per_ring
        """
        factor_last = factor + 1
        new_points_per_ring = points_per_ring * factor + 1
        result = []
        for points_of_shell in mesh_layers:
            # Apex point is saved at location 0 -> no interpolation
            points_per_slice = np.stack(
                [points_of_shell[1 + i * points_per_ring:1 + (i + 1) * points_per_ring] for i in
                 range(n_slices)])

            c_points_interp = np.stack([(points_per_slice[:, 1:] - points_per_slice[:, :-1])
                                        * i / factor + points_per_slice[:, :-1] for i in
                                        range(factor)],
                                       axis=-2)
            c_points_interp = c_points_interp.reshape((n_slices, -1, 3))

            last_interval = np.stack([(points_per_slice[:, 0:1] - points_per_slice[:, -1:])
                                      * i / factor_last + points_per_slice[:, -1:] for i in
                                      range(factor_last)], axis=-2)
            last_interval = last_interval.reshape((n_slices, -1, 3))

            c_points_interp = np.concatenate([c_points_interp, last_interval],
                                             axis=1).reshape(-1, 3)
            result.append(np.concatenate([points_of_shell[0:1],
                                          c_points_interp.reshape(-1, 3)], axis=0))

        return np.stack(result, axis=0), new_points_per_ring

    @staticmethod
    def _interp_long(mesh_layers: np.ndarray, factor: int = 4, points_per_ring: int = 40,
                     n_slices: int = 30) -> (np.ndarray, int):
        """ Interpolates mesh along longitudinal direction. The number of slices excludes the apex.
        The interpolation includes the interval between the apex and the first slice, therefore the
        resulting number of slices after interpolation evaluates to
        n_slices_new = n_slices * factor.

        :param mesh_layers: (n_shells, points_per_ring * n_slices + 1, 3)
        :param factor: (int) interpolation multiplier
        :param points_per_ring: (int) number of points per ring for input argument mesh_layers
        :param n_slices: (int) number of slices for input argument mesh_layers
        :returns: (n_shells, points_per_ring * n_slices_new + 1, 3)
        """
        new_n_slices = n_slices * factor
        result = []
        if factor == 1:
            return mesh_layers, n_slices

        for points_of_shell in mesh_layers:
            # Unstack longitudinal slices (each having points_per_ring elements)
            points_per_slice = points_of_shell[1:].reshape(n_slices, points_per_ring, 3)

            # Concatenate broadcasted singularity (apex) to insert slices there as well
            apex_to_first_interp = np.stack([(points_per_slice[0] - points_per_slice[1:2]) *
                                             i / factor + points_per_slice[1:2] for i in
                                             range(1, factor)], axis=1)
            apex_to_first_interp = apex_to_first_interp[:, ::-1].reshape(-1, points_per_ring, 3)

            # interpolate, most basal layer is dropped
            points_interp = np.stack([(points_per_slice[1:] - points_per_slice[:-1]) *
                                      i / factor + points_per_slice[:-1] for i in range(factor)],
                                     axis=1)
            points_interp = points_interp.reshape((-1, points_per_ring, 3))

            points_interp = np.concatenate([apex_to_first_interp, points_interp], axis=0).reshape(
                -1, 3)

            # strip apex and append basal
            points_interp = np.concatenate(
                [points_of_shell[0:1], points_interp, points_per_slice[-1]],
                axis=0)
            result.append(points_interp)

        return np.stack(result, axis=0), new_n_slices

    @staticmethod
    def _interp_radial(mesh_layers: np.ndarray, factor: int = 4) -> (np.ndarray, int):
        """Interpolates mesh along radial direction. Interpolation is performed in the n_shells-1
        intervals, therefore the resulting number of shells is
        n_shells_new = (n_shells - 1) * factor + 1

        Interpolation includes the interval between the apex and the first slice, therefore
        the resulting number of slices after interpolation evaluates
        to n_slices_new = n_slices * factor.

        :param mesh_layers: (n_shells, points_per_ring * n_slices + 1, 3)
        :param factor: (int) interpolation multiplier
        :returns: (n_shells, points_per_ring * n_slices_new + 1, 3)
        """
        n_shells, points_per_shell = mesh_layers.shape[0:2]
        new_n_shells = (n_shells - 1) * factor + 1
        shells_without_apex = mesh_layers[:, 1:, :]
        x_ref = np.arange(0., n_shells, 1.)
        x_new = np.concatenate([np.arange(i, i + 1, 1 / factor) for i in range(n_shells - 1)])
        x_new = np.concatenate([x_new, [n_shells - 1, ]], axis=0)
        shells_interp = np.zeros((new_n_shells, points_per_shell - 1, 3))
        for cl_idx in range(points_per_shell - 1):
            r_pos = shells_without_apex[:, cl_idx]
            func_x = interpolate.InterpolatedUnivariateSpline(x_ref, r_pos[..., 0], k=3)
            func_y = interpolate.InterpolatedUnivariateSpline(x_ref, r_pos[..., 1], k=3)
            func_z = interpolate.InterpolatedUnivariateSpline(x_ref, r_pos[..., 2], k=3)
            shells_interp[:, cl_idx] = np.stack([func_x(x_new), func_y(x_new), func_z(x_new)],
                                                axis=-1)

        shells_interp_with_apex = np.concatenate(
            [np.tile(mesh_layers[0:1, 0:1, :], [shells_interp.shape[0], 1, 1]),
             shells_interp], axis=1)

        return shells_interp_with_apex, new_n_shells

    @staticmethod
    def evaluate_connectivity(n_theta: int, n_radial: int, n_layers: int):
        """Generates connectivity for tetrahedral UnstructuredGrid in vtk format
        Inputs:
            - n_theta  : number of points along circumferential contour (n points for each ring)
            - n_radial : number of points along longitudinal direction
            - n_layers : number of points along radial direction

        Outputs:
            - connectivity : connectivity array where row i contains the vertex id of points
            defining tetrahedron with index i

        Dr. Buoso Stefano (2020)
        email: buoso@biomed.ee.ethz
        """
        offset_layer0 = n_radial * n_theta + 1

        connectivity = []
        offset = 0

        for k in range(n_layers - 1):
            for j in range(n_theta - 1):
                connectivity.append(
                    [offset, j + 1 + offset, j + 2 + offset, j + 2 + offset + offset_layer0])
                connectivity.append([offset, j + 1 + offset, j + 2 + offset + offset_layer0,
                                     j + 1 + offset + offset_layer0])
                connectivity.append(
                    [offset, j + 1 + offset + offset_layer0, j + 2 + offset + offset_layer0,
                     offset + offset_layer0])
            connectivity.append([offset, j + 2 + offset, 1 + offset, 1 + offset + offset_layer0])
            connectivity.append(
                [offset, j + 2 + offset, 1 + offset + offset_layer0,
                 j + 2 + offset + offset_layer0])
            connectivity.append([offset, j + 2 + offset + offset_layer0, 1 + offset + offset_layer0,
                                 offset + offset_layer0])

            for i in range(0, n_radial - 1):
                for j in range(n_theta - 1):
                    connectivity.append([j + 1 + offset, j + 2 + offset + n_theta, j + 2 + offset,
                                         j + 2 + offset + n_theta + offset_layer0])
                    connectivity.append(
                        [j + 1 + offset, j + 2 + offset + n_theta + offset_layer0, j + 2 + offset,
                         j + 2 + offset + offset_layer0])
                    connectivity.append([j + 1 + offset, j + 2 + offset + n_theta + offset_layer0,
                                         j + 2 + offset + offset_layer0,
                                         j + 1 + offset + offset_layer0])

                    connectivity.append(
                        [j + 1 + offset, j + 1 + offset + n_theta, j + 2 + offset + n_theta,
                         j + 2 + offset + n_theta + offset_layer0])
                    connectivity.append([j + 1 + offset, j + 1 + offset + n_theta,
                                         j + 2 + offset + n_theta + offset_layer0,
                                         j + 1 + offset + n_theta + offset_layer0])
                    connectivity.append([j + 1 + offset, j + 1 + offset + n_theta + offset_layer0,
                                         j + 2 + offset + n_theta + offset_layer0,
                                         j + 1 + offset + offset_layer0])
                connectivity.append([j + 2 + offset, j + 3 + offset, j + 3 + offset - n_theta,
                                     j + 3 + offset + offset_layer0])
                connectivity.append(
                    [j + 2 + offset, j + 3 + offset + offset_layer0, j + 3 + offset - n_theta,
                     j + 3 + offset - n_theta + offset_layer0])
                connectivity.append([j + 2 + offset, j + 3 + offset + offset_layer0,
                                     j + 3 + offset - n_theta + offset_layer0,
                                     j + 2 + offset + offset_layer0])
                connectivity.append([j + 2 + offset, j + 2 + offset + n_theta, j + 3 + offset,
                                     j + 3 + offset + offset_layer0])
                connectivity.append(
                    [j + 2 + offset, j + 2 + offset + n_theta, j + 3 + offset + offset_layer0,
                     j + 2 + offset + n_theta + offset_layer0])
                connectivity.append([j + 2 + offset, j + 2 + offset + n_theta + offset_layer0,
                                     j + 3 + offset + offset_layer0,
                                     j + 2 + offset + offset_layer0])

                offset += n_theta
            offset = (k + 1) * offset_layer0

        return np.array(connectivity)

    @staticmethod
    def evaluate_cellsize(points: np.ndarray, connectivity: np.ndarray) \
            -> (np.ndarray, np.ndarray, np.ndarray):
        """ Evaluates cell centers and cell volumes for the tetra-mesh given as
        points and connectivity.

        :param points: (#points, 3)
        :param connectivity: (#cells, 4)
        :returns: cell_center (#cells, 3), cell_volumes (#cells), point_weights (#points)
        """
        coordinates = points[connectivity]
        cell_centers = np.mean(coordinates, axis=1)
        tetra_edge_vectors = coordinates[:, 1:] - coordinates[:, 0:1]
        cell_volumes = np.abs(
            np.einsum("ni,ni->n", np.cross(tetra_edge_vectors[:, 0], tetra_edge_vectors[:, 1]),
                      tetra_edge_vectors[:, 2])) / 6
        point_weights = np.zeros(points.shape[0])
        point_weights[connectivity.reshape(-1)] += np.tile(cell_volumes[:, np.newaxis],
                                                           [1, 4]).reshape(-1) / 4

        point_weights = (np.abs(point_weights)) / np.mean(np.abs(point_weights))
        cell_volumes = (np.abs(cell_volumes)) / np.mean(np.abs(cell_volumes))

        return cell_centers, cell_volumes, point_weights

    @staticmethod
    def evaluate_cylinder_coordinates(positional_vectors: np.ndarray, n_shells: int,
                                      points_per_shell: int):
        """
        :param positional_vectors: (-1, 3)
        :param n_shells: (int)
        :param points_per_shell: (int)
        :return: np.ndarray (-1, 3) [radial, angle, relative z]
        """
        outer_shell = positional_vectors[1:points_per_shell, 0:2]
        inner_shell = positional_vectors[1 + (n_shells - 1) * points_per_shell:, 0:2]

        r_vec = positional_vectors.reshape((n_shells, points_per_shell, 3))
        transmural_position = np.linalg.norm(r_vec[:, 1:, 0:2] - inner_shell, axis=-1)
        transmural_position /= np.linalg.norm(outer_shell - inner_shell, axis=-1)

        angle = np.angle(r_vec[:, 1:, 0] + 1j * r_vec[:, 1:, 1])

        normalized_z_pos = r_vec[..., 2] / np.abs(r_vec[..., 2]).max()

        cylinder_coordinates = np.stack([transmural_position, angle,
                                         normalized_z_pos[:, 1:]], axis=-1)
        apex = np.concatenate([np.zeros_like(r_vec[:, 0:1, 0:2]),
                               normalized_z_pos[:, 0:1, np.newaxis]], axis=-1)
        cylinder_coordinates = np.concatenate([apex, cylinder_coordinates], axis=1)
        return cylinder_coordinates.reshape(-1, 3)

    @staticmethod
    def _compute_local_basis(positional_vectors: np.ndarray,
                             mesh_numbers: Union[Tuple[int, int, int], List[int]]) -> dict:
        """ Computes the local coordinate system (radial, circumferential, longitudinal) for
        a left ventricle mesh.

        Assumes the mesh indexing to correspond to:
             without apex: (#n_shells, #n_slices, #n_theta, 3).reshape(#n_shells, -1, 3)
             concat apex: (#n_shells, 1+(#n_slices * #n_theta), 3).reshape(-1, 3)

        :param positional_vectors: (-1, 3)
        :param mesh_numbers: (#shells, #slices, #points_per_ring)
        :return: dict containing the local basis vectors per point with keys (e_r, e_c, e_l)
        """
        points_per_shell = 1 + mesh_numbers[1] * mesh_numbers[2]

        # Compute circ basis vector as difference
        mesh_vecs = positional_vectors.reshape((mesh_numbers[0], points_per_shell, 3),
                                               order="C")[:, 1:]
        mesh_vecs = mesh_vecs.reshape((mesh_numbers[0], mesh_numbers[1], mesh_numbers[2], 3),
                                      order="C")
        mesh_vecs_aug = np.concatenate([mesh_vecs, mesh_vecs[:, :, 0:1]], axis=2)

        e_c = np.diff(mesh_vecs_aug, axis=2).reshape((mesh_numbers[0], -1, 3))
        e_c = np.concatenate([e_c, np.tile(np.array([[[0., 1., 0.]]]), [mesh_numbers[0], 1, 1])],
                             axis=1).reshape(-1, 3)
        e_c /= np.linalg.norm(e_c, axis=-1, keepdims=True)

        # Compute longitudinal as difference vector between slices
        mesh_vecs = positional_vectors.reshape((mesh_numbers[0], points_per_shell, 3),
                                               order="C")[:, 1:]
        mesh_vecs = mesh_vecs.reshape(mesh_numbers[0], mesh_numbers[1], mesh_numbers[2],
                                      3, order="C")
        mesh_vecs = np.concatenate([mesh_vecs,
                                    np.tile(positional_vectors[0:1, :].reshape(1, 1, 1, 3),
                                            [mesh_numbers[0], 1, mesh_numbers[2], 1])
                                    ], axis=1)
        e_l = np.gradient(mesh_vecs, axis=1)
        e_l = np.concatenate([e_l[:, 0:1, 0], e_l[:, 1:].reshape(mesh_numbers[0], -1, 3)], axis=1)
        e_l = e_l.reshape(-1, 3)
        norm_l = np.linalg.norm(e_l, axis=-1, keepdims=True)
        e_l = np.divide(e_l, norm_l, where=norm_l > 0)

        # Compute radial vector as cross product
        e_r = np.cross(e_c, e_l)
        norm_r = np.linalg.norm(e_r, axis=-1, keepdims=True)
        e_r = np.divide(e_r, norm_r, where=norm_r > 0)

        return dict(e_r=e_r, e_l=e_l, e_c=e_c)
