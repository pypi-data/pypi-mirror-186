"""Contains convenience implementations to handle meshes for flow-simulations including
refilling and pruning """

__all__ = ["RefillingFlowDataset"]

import math
from typing import List, Tuple, Dict

import tensorflow as tf
import numpy as np
import pyvista

from scipy.ndimage import gaussian_filter


# pylint: disable=too-many-instance-attributes
class RefillingFlowDataset(tf.Module):
    """ Wraps a vtk-mesh of containing a velocity field. Functionality tackles the problem of in-/
    out-flow of particles for a given imaging slice.
    """
    #: Reference to the original mesh, given as input
    original_mesh: 'pyvista.UnstructuredGrid'
    #: Spacing of the uniform grid used for defining the lookup-maps taken from original mesh
    lookup_map_spacing: np.ndarray
    #: Reference to the uniformly gridded input mesh
    gridded_mesh: 'pyvista.UniformGrid'
    #: Property storing the mean particle density in the specified seeding volume
    mean_density: float
    #:
    n_new: int
    #:
    n_drop: int
    #: Positional offset of the re-seeding volume in meter
    seeding_slice_position: np.ndarray
    #: Normal vector of the re-seeding volume (formulated as plane +/ slice thickness/2)
    seeding_slice_normal: np.ndarray
    #: Slice thickness the re-seeding volume in meter
    seeding_slice_thickness: float
    #: Maximal extend of the cartesian bounding box for the re-seeding slice. If not specified,
    #: the seeding volume includes the union of an infinite slice & the original mesh
    slice_bounding_box: np.ndarray
    #: Spacing of the uniform grid used for defining the seeding volume
    seeding_vol_spacing: np.ndarray
    #: Reference to the seeding volume represented as an uniform grid
    gridded_seeding_volume: 'pyvista.UniformGrid'
    #: Cell indices for the union of self.gridded_seeding_volume & original mesh.
    #: (Note: self.gridded_seeding_volume implements a uniform grid corresponding to the bounding
    # box for a part of the original mesh)
    _active_cells_indices: np.ndarray
    #: Coordinates of cells indexed by _active_cells_indices, this is used for uniformly seeding
    #: Particles
    _active_cell_centers: np.ndarray

    # pylint: disable=too-many-arguments
    def __init__(self, mesh: 'pyvista.UnstructuredGrid', slice_position: np.ndarray,
                 slice_normal: np.ndarray, slice_thickness: float,
                 lookup_map_spacing: np.ndarray,
                 seeding_vol_spacing: np.ndarray,
                 field_list: List[Tuple[str, int]],
                 particle_creation_callables: Dict[str, callable] = None,
                 slice_bounding_box: np.ndarray = None):
        """

        :param mesh: 'pyvista.UnstructuredGrid' 3D mesh of flow-field
        :param slice_position: (3, ) in meter
        :param slice_normal: (3, ) unit normal vector of the selected slice
        :param slice_thickness: float in meter
        :param lookup_map_spacing: (3, ) in meter - determines the pixel size of the uniformly
                                        gridded mesh representing the lookup maps
        :param seeding_vol_spacing: (3, ) in meter - determines the pixel size of the seeding
                                        volume, should be at least 4 times smaller that Voxel-size
                                        of the simulated image
        :param field_list: list of tuples for fields in mesh.
                            tuples should be ("label", num elements)
        :param slice_bounding_box: (3, ) in meter - user defined bounding box for slicing mesh.
                                         Uses whichever is smaller between mesh limits
                                         and user defined box
        """
        super().__init__(name="refilling_flow_field")
        if not all(f in mesh.array_names for f, _ in field_list):
            raise ValueError(f"Specified field_list {field_list} contains names that are not "
                             f"contained in given mesh-arrays {mesh.array_names}")
        self.particle_properties = list(particle_creation_callables.keys())
        self._particle_creators = [particle_creation_callables[k] for k in self.particle_properties]
        self.field_list = field_list
        self.update_mesh(mesh, lookup_map_spacing)

        self.slice_bounding_box = slice_bounding_box
        self.update_seeding_volume(seeding_vol_spacing, slice_position, slice_normal,
                                   slice_thickness, slice_bounding_box)

        # initialize mean density, which is correctly evaluated on __call__
        self.mean_density = 0.
        self.n_new = 0
        self.n_drop = 0

    def update_mesh(self, mesh: 'pyvista.UnstructuredGrid',
                    lookup_map_spacing: np.ndarray):
        """ Processes the mesh handed in as argument, and saves the nessecary information
        into class attributes.

        Sets the module attributes:
            - self.original_mesh
            - self.lookup_map_spacing
            - self.gridded_mesh

        :param mesh: 'pyvista.UnstructuredGrid' 3D mesh of flow-field
        :param lookup_map_spacing: (3, ) in meter - determines the pixel size of the
                             uniformly gridded mesh
        :return: None
        """
        image_box = np.max(mesh.points, axis=0) - np.min(mesh.points, axis=0)
        dims = (image_box / lookup_map_spacing).astype(int)
        resolution = image_box / dims
        origin = np.min(mesh.points, axis=0)

        uniform_grid = pyvista.UniformGrid(dims=dims,
                                           spacing=resolution,
                                           origin=origin)
        self.lookup_map_spacing = lookup_map_spacing

        uniform_grid = uniform_grid.sample(mesh)
        uniform_grid["in_mesh"] = np.array(uniform_grid["vtkValidPointMask"], dtype=np.float64)
        self.gridded_mesh = uniform_grid
        self.original_mesh = mesh
        print("Updated Mesh")

    # pylint: disable=multiple-statements
    # pylint: disable=too-many-arguments
    def update_seeding_volume(self,
                              seeding_vol_spacing: np.ndarray = None,
                              slice_position: np.ndarray = None,
                              slice_normal: np.ndarray = None,
                              slice_thickness: float = None,
                              slice_bounding_box: np.array = None):
        """ Creates a uniform grid which represents the surrounding cuboid of the selected slice
        from self.gridded_mesh. The pv.UniformGrid contains the arrays 'in_slice' and 'in_mesh'.
        Using logical_and on those, yields the condition for positions being inside the sliced
        flow field.

        Sets the module attributes:
            - self.gridded_seeding_volume
            - self.seeding_slice_position
            - self.seeding_slice_normal
            - self.seeding_slice_thickness
            - self.slice_bounding_box

        :param seeding_vol_spacing:  (3, ) in meter - determines the pixel size of the seeding
                                        volume, should be at least 4 times smaller that Voxel-size
                                        of the simulated image
        :param slice_position:  (3, ) in meter
        :param slice_normal: (3, )
        :param slice_thickness: float in meter
        :param slice_bounding_box: (3, ) in meter - user defined bounding box for slicing mesh.
        """

        if seeding_vol_spacing is not None: self.seeding_vol_spacing = seeding_vol_spacing
        if slice_position is not None: self.seeding_slice_position = slice_position
        if slice_normal is not None: self.seeding_slice_normal = slice_normal
        if slice_thickness is not None: self.seeding_slice_thickness = slice_thickness
        if slice_bounding_box is not None: self.slice_bounding_box = slice_bounding_box

        r_slice, _ = RefillingFlowDataset._select_slice(self.gridded_mesh.points,
                                                        self.seeding_slice_normal,
                                                        self.seeding_slice_position,
                                                        self.seeding_slice_thickness,
                                                        self.slice_bounding_box)

        # Create uniform grid with specified seeding slice boundaries
        image_box = np.max(r_slice, axis=0) - np.min(r_slice, axis=0)
        dims = (image_box / self.seeding_vol_spacing).astype(int)
        resolution = image_box / dims
        origin = np.min(r_slice, axis=0)
        gridded_seeding_volume = pyvista.UniformGrid(dims=dims + 1,
                                                     spacing=resolution,
                                                     origin=origin)
        self.gridded_seeding_volume = self.gridded_mesh.probe(gridded_seeding_volume)

        active_indx = np.where(self.gridded_seeding_volume.ptc().cell_data["in_mesh"] > 0.7)
        active_cell_centers = self.gridded_seeding_volume.cell_centers().ptc().points[active_indx]

        self._active_cell_centers, in_slice = self._select_slice(active_cell_centers,
                                                                 self.seeding_slice_normal,
                                                                 self.seeding_slice_position,
                                                                 self.seeding_slice_thickness,
                                                                 self.slice_bounding_box)
        self._active_cells_indices = np.where(in_slice)
        print("Updated Slice Position")

    @staticmethod
    def _select_slice(all_points: np.ndarray, slice_normal: np.ndarray,
                      slice_position: np.ndarray, slice_thickness: float,
                      slice_bounding_box: Tuple[float, float, float] = None):
        """ For given
        :param all_points: [-1, 3]
        :param slice_normal: (x, y, z)
        :param slice_position: (x, y, z)
        :param slice_thickness: float
        :param slice_bounding box: ()
        """
        slice_normal = slice_normal / np.linalg.norm(slice_normal)
        distance = np.einsum("ni, i", all_points - slice_position[np.newaxis, :], slice_normal)
        in_slice = np.abs(distance) <= slice_thickness / 2

        if slice_bounding_box is not None:
            masked_lower = np.prod(all_points >
                                   (slice_position - slice_bounding_box / 2)[np.newaxis], axis=-1)
            masked_upper = np.prod(all_points <
                                   (slice_position + slice_bounding_box / 2)[np.newaxis], axis=-1)
            in_bb = np.logical_and(masked_lower, masked_upper)
            in_slice = np.logical_and(in_slice, in_bb)

        r_slice = all_points[np.where(in_slice)]
        return r_slice, in_slice

    # pylint: disable=too-many-arguments
    def __call__(self, particle_density, residual_particle_pos=None, particle_properties=None,
                 distance_tolerance: float = 5e-3, reseed_threshold: float = 1):
        """ Checks given particle positions and drops all that are out of bounds and sufficiently
        far away from the reseeding box.

        :param particle_density: target values for particle per 1/mm^3 cell of the grid
        :param residual_particle_pos: np.ndarray - Shape (-1, 3)
        :param particle_properties: dictionary of arrays (magnetization, T1, T2)
        :param distance_tolerance: float maximal distance to slice of particles that are reused
        :param reseed_threshold: [0,1], threshold as a fraction of particle density below which
                                 reseeding will occur. Positions with higher density than
                                 reseed_threshold*particle_density will not reseed
        :return: If no residual particles are handed in the returned tuple of properties is set to
                 default values only.
                 otherwise it contains the properties of the particles selected to keep
                 Tuple[np.ndarray, (np.ndarray)] - Shape[(-1, 3), (-1, 3)]
                 (particle_positions, (particle_properties), in_tolerance)
        """
        sampled_particle_pos = self._uniformly_sample_slice(particle_density)

        # No particles are kept --> only new particles
        if residual_particle_pos is None:
            n_new = len(sampled_particle_pos)
            return_pos = sampled_particle_pos
            in_tolerance = None
            self.mean_density = particle_density
            return_properties = [fnc(n_new) for fnc in self._particle_creators]
        # Suitable particles are kept --> new particles according to target density
        else:
            # Check for particles within defined distance of original slice
            in_tolerance = self._filter_positions_by_distance_to_slice(residual_particle_pos,
                                                                       distance_tolerance)
            self.n_drop = residual_particle_pos.shape[0] - in_tolerance[0].shape[0]

            # Re-seed particles in un-populated areas with Monte-Carlo rejection:
            # 1. Estimate current particle density within slice
            self._estimate_particle_density(residual_particle_pos[in_tolerance])
            sampled_particle_pos = self.gridded_seeding_volume.probe(sampled_particle_pos)
            density = np.array(sampled_particle_pos["density"])
            decision_boundaries = density / particle_density
            # 2. To prevent unintentionally increasing particle density, set the decision boundary
            # to 1 where it is larger than the defined threshold
            decision_boundaries[decision_boundaries > reseed_threshold] = 1
            # 3. MC-rejection step based on density
            mc_samples = np.random.uniform(0., 1., size=len(sampled_particle_pos.points))
            is_accepted = np.where(np.array(mc_samples > decision_boundaries, dtype=bool))
            n_new = len(is_accepted[0])

            # Keep properties of particles in tolerance and concatenate new particles
            return_pos = np.concatenate([residual_particle_pos[in_tolerance],
                                         sampled_particle_pos.points[is_accepted]])
            return_properties = [np.concatenate([particle_properties[k][in_tolerance], fnc(n_new)])
                                 for k, fnc in zip(self.particle_properties, self._particle_creators)]

            # Update mean density after reseeding (to check for density increase)
            density_pre = self.gridded_seeding_volume["density"][self._active_cells_indices]
            self.mean_density = np.mean(density_pre)

        self.n_new = n_new
        return (return_pos.astype(np.float32),
                {k: v for k, v in zip(self.particle_properties, return_properties)}, in_tolerance)

    def _uniformly_sample_slice(self, particle_density: float) -> np.ndarray:
        """ Uniformly samples positions in each cell of gridded_seeding_volume that is inside
        the original mesh. The density of particles per mm^3 will be an  integer multiple of
        rasterized cells within a cubic mm (defined by self.seeding_vol_spacing on
        object initialization).

        :param particle_density: float - particle positions per cubic mm to be sampled
        :return: np.ndarray
        """
        n_active_cells = self._active_cell_centers.shape[0]
        cell_spacing = np.array(self.gridded_seeding_volume.spacing).reshape(3, 1)
        sampling_volume_mm3 = np.prod(cell_spacing * 1e3)
        n_particles_per_cell = max([math.ceil(particle_density * sampling_volume_mm3), 1])
        sampling_boundaries = cell_spacing * np.array([-0.5, 0.5]).reshape(1, 2)
        rnd_r = np.stack([np.random.uniform(lower, upper, size=n_active_cells * n_particles_per_cell)
                          for lower, upper in sampling_boundaries], axis=-1)
        rnd_r = (self._active_cell_centers.reshape((-1, 1, 3)) +
                 rnd_r.reshape((-1, n_particles_per_cell, 3)))

        # Density adjustment
        actual_density = n_particles_per_cell / sampling_volume_mm3
        density_ratio = particle_density / actual_density
        n_keep = math.ceil(rnd_r.shape[0] * density_ratio)
        keep_idx = np.random.choice(np.arange(0, rnd_r.shape[0]), n_keep, replace=False)
        rnd_r = rnd_r[keep_idx, :]
        return rnd_r.reshape(-1, 3)

    def _filter_positions_by_distance_to_slice(self, particle_positions: np.ndarray,
                                               max_distance: float):
        """ For given particle positions computes the distance to slice surface and evaluates
        following boolean:
            - particles are within specified maximal distance to slice
            - particles are inside bounding box of original mesh
        :param particle_positions: (#batch, 3)
        :param max_distance:
        :return: in_tolerance (#batch, )
        """
        relative_positions = particle_positions - self.seeding_slice_position[np.newaxis, :]
        distance_to_slice = np.einsum("ni, i", relative_positions, self.seeding_slice_normal)
        within_distance = (np.abs(distance_to_slice) <
                           max_distance + self.seeding_slice_thickness / 2)

        bounds = np.array(self.original_mesh.bounds).reshape(3, 2)
        above_min = np.prod(particle_positions > bounds[np.newaxis, :, 0], axis=-1)
        under_max = np.prod(particle_positions < bounds[np.newaxis, :, 1], axis=-1)
        in_bounds = np.logical_and(above_min, under_max)
        accepted_particles = np.logical_and(within_distance, in_bounds)
        return np.where(accepted_particles)

    def _estimate_particle_density(self, particles: np.ndarray):
        """ Creates 3D histogram of positions inside the gridded slice and applies the gaussian
        smoothing filter to estimate the current particle density at grid locations

        After calling the method, the pyvista.UniformGrid self.gridded_seeding_volume contains the
        data arrays 'histogram' and 'density'
        """
        sampling_volume = np.prod(np.array(self.gridded_seeding_volume.spacing) * 1e3)  # in mm^3
        bin_edges = [np.arange(0., self.gridded_seeding_volume.extent[2 * i + 1] + 1) *
                     self.gridded_seeding_volume.spacing[i] + self.gridded_seeding_volume.origin[i]
                     for i in range(3)]
        residual_histogram, _ = np.histogramdd(particles, bins=bin_edges)
        sigma = self.lookup_map_spacing / self.seeding_vol_spacing * 0.75
        smoothed_histogram = gaussian_filter(residual_histogram / sampling_volume,
                                             sigma=sigma, truncate=2.5)
        self.gridded_seeding_volume.cell_data["density"] = smoothed_histogram.reshape(-1, order="F")

    def get_lookup_table(self):
        """ Returns a C-ordered gridded 3D velocity-field and the corresponding physical extends
        of the grid. Assumes that the internally stored mesh/UniformGrid is stored in Fortran order.

        :return: Array of shape [X, Y, Z, 3+N] containing the lookup-tables for velocity and N
                    additional entries
        """
        fields = []
        for entry in self.field_list:
            fields.append(
                self.gridded_mesh[entry[0]].reshape((*self.gridded_mesh.dimensions, entry[1]),
                                                    order="F").astype(np.float32))
        map_dimensions = np.array(self.gridded_mesh.bounds, dtype=np.float32).reshape(3, 2)
        return np.concatenate(fields, axis=3), map_dimensions

    def initial_filling(self, particle_density: float, slice_dictionary: dict = None):
        """ Randomly uniform seeds particle into the rasterized version of the input mesh
        with the specified particle density. The density of particles per mm^3 will be an
        integer multiple of rasterized cells within a cubic mm (defined by lookup_map_spacing
        on object initialization). Along with the positions, particle properties
        are returned (defined by the factory functions passed on object initialization)

        :param particle_density: approximate density; will be rounded according to
                    n_particles_per_cell = max([int(particle_density * sampling_volume_mm3), 1])
        :param slice_dictionary: keys: (slice_normal, slice_position, slice_thickness,
                                        slice_bounding_box)
        :return: (-1, 3) particle positions, dict("T1": (-1), ...) particle properties
        """
        active_indx = np.where(self.gridded_mesh.ptc().cell_data["in_mesh"] > 0.7)
        active_cell_centers = self.gridded_mesh.cell_centers().ptc().points[active_indx]

        if slice_dictionary is not None:
            active_cell_centers, _ = self._select_slice(active_cell_centers, **slice_dictionary)

        n_active_cells = active_cell_centers.shape[0]
        cell_spacing = np.array(self.gridded_mesh.spacing).reshape(3, 1)
        sampling_volume_mm3 = np.prod(cell_spacing * 1e3)
        n_particles_per_cell = max([math.ceil(particle_density * sampling_volume_mm3), 1])
        sampling_boundaries = cell_spacing * np.array([-0.5, 0.5]).reshape(1, 2)
        rnd_r = np.stack([np.random.uniform(lower, upper, size=n_active_cells * n_particles_per_cell)
                          for lower, upper in sampling_boundaries], axis=-1)
        rnd_r = active_cell_centers.reshape(-1, 1, 3) + rnd_r.reshape((-1, n_particles_per_cell, 3))
        rnd_r = rnd_r.reshape(-1, 3).astype(np.float32)

        # Adjust density which is >= target due to ceiling operation
        actual_density = n_particles_per_cell / sampling_volume_mm3
        density_ratio = particle_density / actual_density
        n_keep = math.ceil(rnd_r.shape[0] * density_ratio)
        keep_idx = np.random.choice(np.arange(0, rnd_r.shape[0]), n_keep, replace=False)
        rnd_r = rnd_r[keep_idx, :]

        return_properties = {k: fnc(rnd_r.shape[0]) for k, fnc
                             in zip(self.particle_properties, self._particle_creators)}

        return rnd_r, return_properties

    def project_density_to_mesh(self, particles: np.ndarray) -> pyvista.UnstructuredGrid:
        """ Evaluates the density of given particle positions and projects it onto the geometry
        of the original mesh

        :param particles: (-1, 3)
        """
        sampling_volume = np.prod(np.array(self.gridded_mesh.spacing) * 1e3)  # in mm^3
        bin_edges = [np.arange(0., self.gridded_mesh.extent[2 * i + 1] + 1)
                     * self.gridded_mesh.spacing[i] + self.gridded_mesh.origin[i]
                     for i in range(3)]
        residual_histogram, _ = np.histogramdd(particles, bins=bin_edges)
        sigma = self.lookup_map_spacing / self.seeding_vol_spacing * 0.75
        smoothed_histogram = gaussian_filter(residual_histogram / sampling_volume,
                                             sigma=sigma, truncate=2.5)
        self.gridded_mesh.cell_data["density"] = smoothed_histogram.reshape(-1, order="F")
        return self.gridded_mesh.probe(self.original_mesh)