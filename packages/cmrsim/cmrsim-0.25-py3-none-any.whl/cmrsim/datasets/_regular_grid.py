__all__ = ["RegularGridDataset", ]

from typing import Dict, Tuple, Union, Sequence

import tensorflow as tf
import numpy as np
import pyvista
from pint import Quantity

import cmrsim.utils.coordinates


class RegularGridDataset:
    """Dataset class containing functionality, that requires a regular-grid representation of the
    data. Multiple class-methods define inputs from which an instance of this class can be
    created.

    :param mesh: Instance of a pyvista.UniformGrid which is copied on instantiation
    """
    #: Instance of a pyvista.UniformGrid used as basis for all contained computations
    mesh: pyvista.UniformGrid

    def __init__(self, mesh: pyvista.UniformGrid):
        self.mesh = mesh.copy()

    def get_phantom_def(self, filter_by: str = None, keys: Sequence[str] = None,
                        perturb_positions_std: float = None) -> Dict[str, np.ndarray]:
        """Extracts points and their corresponding physical properties from the contained mesh
        and returns them as dictionary of flattened array

        :param filter_by: used to determine which points to extract from the mesh by using the
                            indices = np.where(self.mesh[filter_by])
        :param keys: sequence of strings defining the field arrays returned as dictionary keys
        :param perturb_positions_std: if specified the positions of the extracted mesh-points are
                    perturbed by sampling a normal distribution with zero mean and given standard
                    deviation to reduce descretization artifacts in simulation
        :return:
        """

        if filter_by is not None:
            indices = np.where(self.mesh[filter_by])
        else:
            indices = np.where(np.ones_like(self.mesh.points[:, 0]))

        if keys is None:
            keys = self.mesh.array_names

        r_vectors = np.array(self.mesh.points[indices], dtype=np.float32).reshape(-1, 3)
        if perturb_positions_std is not None:
            r_vectors += np.random.normal(0, perturb_positions_std, size=r_vectors.shape)

        phantom = dict(r_vectors=r_vectors)
        phantom.update({k: np.squeeze(self.mesh[k][indices].reshape(r_vectors.shape[0], -1))
                        for k in keys})
        return phantom

    def add_field(self, key: str, data: np.ndarray):
        """Adds field to self.mesh from a numpy array (takes care of correct ordering from
        default numpy C-order to F-order used in pyvista).

        :param key: name of the new field
        :param data: (x, y, z, N) dimensional array containing arbitrary data
        """
        n_channels = np.prod(data.shape) // np.prod(self.mesh.dimensions)
        flat_data = data.reshape([-1, n_channels], order="F")
        self.mesh[key] = flat_data

    def resample_spacing(self, spacing: Quantity):
        """Resamples the contained self.mesh to a new spacing, which might be necessary to reduce
        discretization artifacts on simulation.

        :param spacing: New target spacing (3, )
        """
        r_max = np.max(self.mesh.points, axis=0)
        r_min = np.min(self.mesh.points, axis=0)
        nbins = (Quantity(r_max - r_min, "m") / spacing.to("m")).m.astype(int)
        new_mesh = pyvista.UniformGrid(dimensions=nbins, spacing=spacing.m_as("m"), origin=r_min)
        self.mesh = new_mesh.sample(self.mesh)

    def select_slice(self, slice_normal: np.array, spacing: Quantity,
                     slice_position: Quantity, field_of_view: Quantity,
                     readout_direction: np.array = None,
                     in_mps: bool = False) -> pyvista.UniformGrid:
        """Creates a uniform grid (slice) according to the specified parameters, and uses it to
        probe the self.mesh (see example). Slice (coordinates) can either be returned in mps
        or in global coordinates.

        .. Dropdown:: Example Visualization

            .. image:: ../../_static/api/dataset_regular_grid_select_slice.png

        :param slice_normal: (3, ) normal vector of the extracted slice
        :param spacing: (3, ) dimension of voxels in all directions
        :param slice_position: (3, ) vector pointing to the slice-center
        :param field_of_view: (3, ) total extent of the extracted slice in 3 dimensions
        :param readout_direction: (3, ) if not provided, is assumed to be x (part orthogonal to
                specified slice normal). Used to rotate the extracted slice about the slice-normal
        :param in_mps: if true the slice is returned in MPS coordinates
        :return:
        """
        from cmrsim.utils.coordinates import compute_orientation_matrix
        total_transform = compute_orientation_matrix(slice_normal, slice_position,
                                                     readout_direction)
        nbins = (field_of_view / spacing).m_as("dimensionless").astype(int)
        new_slice = pyvista.UniformGrid(dimensions=nbins, spacing=spacing.m_as("m"),
                                        origin=-field_of_view.m_as("m") / 2)
        new_slice = new_slice.transform(total_transform, inplace=False)
        new_slice = self.mesh.probe(new_slice)

        if in_mps:
            inv_transform = np.eye(4, 4)
            inv_transform[:3, :3] = total_transform[:3, :3].T
            inv_transform[:3, 3] = -np.einsum('ij, j', inv_transform[:3, :3], slice_position.m_as("m"))
            new_slice = new_slice.transform(inv_transform, inplace=False,
                                            transform_all_input_vectors=True)
        return new_slice

    def compute_offresonance(self, b0: Quantity, susceptibility_key: str) -> Quantity:
        """Approximates the magnetic field variations in z-direction due to interfaces with varying
        susceptibilities by applying a convolution (Fourier Product) with a dipole kernel to the
        susceptibility field contained in self.mesh. The name of the mesh array is specified by
        argument.

        Assumes that the main magnetic field is pointing in z-direction of the contained mesh.
        The susceptibility os assumed to be specified as parts per million
        (e.g. :math:`\chi_{air} = 0.36ppm`).

        The result is store in self.mesh["offres"] and is also returned as Quantity.

        .. Dropdown:: Literature Reference

            This function is based on the work of Frank-Zijlstra, published on Mathworks:

            Frank Zijlstra (2022). MRI simulation using FORECAST: Fourier-based Off-REsonanCe
            Artifact simulation in the STeady-state
            (https://www.mathworks.com/matlabcentral/fileexchange/56680-mri-simulation-using-
            forecast-fourier-based-off-resonance-artifact-simulation-in-the-steady-state),

            MATLAB Central File Exchange. Retrieved December 8, 2022.

        :param b0: Field strength of main magnetic field pointing in z-direction in Tesla
        :param susceptibility_key: name of the array contained in self.mesh, used as susceptibility
        :return: (X, Y, Z) array wrapped as Quantity with dimension ("T")
        """
        chi_3d = self.mesh[susceptibility_key].reshape(self.mesh.dimensions, order="F")
        # Pad the chi-map to a multiple of four:
        residual_per_dim = np.mod(self.mesh.dimensions, 4)
        chi_3d = np.pad(chi_3d,
                        np.stack([np.zeros_like(residual_per_dim), residual_per_dim], axis=1),
                        mode="constant", constant_values=0.)
        voxel_size = Quantity(self.mesh.spacing, "m")
        field_of_view = voxel_size * Quantity(chi_3d.shape, "dimensionless")

        # The fourier based convolution (from original implementation):
        # 1) The forward Fourier Transform (FT): Instead of doing an extra convolution to calculate
        # the effect of aliasing (as proposed in the article), here we use the 'imaginary channel'
        # to do this. This is done by downscaling the artificial environment, and adding this as
        # an imaginary component to the original (unpadded) susceptibility distribution.
        # Together this is referred to as the "DUAL" distribution:
        # down_sampled_chi = tf.nn.avg_pool3d(chi_3d[np.newaxis, ..., np.newaxis], ksize=(2, 2, 2),
        #                                     strides=(2, 2, 2), padding="VALID")
        # imaginary_channel = self._zc(down_sampled_chi[0, ..., 0])
        # ft_chi_3d_dual = tf.signal.fft3d(chi_3d + 1j * imaginary_channel)
        ft_chi_3d_dual = tf.signal.fft3d(chi_3d)
        # 2) multiplication with the dipole function
        dipole_kernel = self._compute_fourier_dipole_kernel(field_of_view,
                                                       np.array(ft_chi_3d_dual.shape))
        ft_field_3d = ft_chi_3d_dual * dipole_kernel
        # 3) inverse FT to spatial domain
        field_3d_dual = tf.signal.ifft3d(ft_field_3d)
        # 4) Subtract the up-scaled cropped center of the aliasing
        # field_3d = tf.math.real(field_3d_dual) - UC(tf.math.imag(field_3d_dual))
        field_3d = tf.math.real(field_3d_dual)
        i, j, k = [_ if _ != 0 else None for _ in -residual_per_dim]
        field_3d = field_3d.numpy()[:i, :j, :k]
        self.mesh["offres"] = b0.to("mT") * field_3d.reshape(-1, order="f")
        return field_3d * b0.to("mT")

    @staticmethod
    def _compute_fourier_dipole_kernel(fov: Quantity, n_samples: np.ndarray):
        """ Computes the dipole kernel for a given FOV and 3D array
        :param fov: (3, ) length - quantity
        :param n_samples: (3, ) integer number of regular points per dimension
        :return:
        """
        k_squared = [np.arange(-n/2, n/2, 1) / fov[i].m_as("m") for i, n in enumerate(n_samples)]
        k_squared = [np.fft.ifftshift(k)**2 for k in k_squared]
        [kx2, ky2, kz2] = np.meshgrid(*k_squared, indexing="ij")
        kernel = 1/3 - kz2 / (kx2 + ky2 + kz2)
        kernel[0, 0, 0] = 0
        return kernel

    @classmethod
    def from_unstructured_grid(cls, input_mesh: pyvista.DataSet, pixel_spacing: Quantity,
                               padding: Quantity = None) -> 'RegularGridDataset':
        """Resamples a given unstructured mesh onto a regular grid and instantiates a
        RegularGridDataset from it.

        :param input_mesh: pyvista.Dataset
        :param pixel_spacing: Quantity (3,) specifying the 3D spacing of the uniform grid
        :param padding: Space added symmetrically around the bounding box of the input_mesh,
                        defaults to (0, 0, 0) "meter"
        """
        if padding is None:
            padding = Quantity([0., 0., 0.], "m")
        r_max = np.max(input_mesh.points, axis=0) + padding.m_as("m") / 2
        r_min = np.min(input_mesh.points, axis=0) - padding.m_as("m") / 2
        nbins = (Quantity(r_max - r_min, "m") / pixel_spacing.to("m")).m.astype(int)
        mesh = pyvista.UniformGrid(dimensions=nbins, spacing=pixel_spacing.m_as("m"), origin=r_min)
        mesh = input_mesh.probe(mesh)
        return cls(mesh)

    @classmethod
    def from_numpy(cls, data: Union[np.ndarray, Dict[str, np.ndarray]],
                   origin_offset: Quantity = Quantity([0, 0, 0], "m"), extent: Quantity = None,
                   pixel_spacing: Quantity = None) -> 'RegularGridDataset':
        """Constructs a uniform regular 3D grid of the same shape as the data provided as argument.

        Assumes that the origin is at the center of the provided array.

        :raises: ValueError:
                    - if neither extent nor pixel_spacing is specified
                    - data-argument is a dictionary containing arrays with non-identical shapes

        :param data: (X, Y, Z, ...)
        :param origin_offset: (3, ) If not provided, the grid is positioned symmetrically around the
                                point (0., 0., 0.). Otherwise this is vector is added onto the
                                center-point.
        :param extent: (3, ) Length-Quantity defining the extend of the provided data in 3 dimen
        :param pixel_spacing: (3, )
        """

        if (all(v is None for v in [pixel_spacing, extent]) or
                all(v is not None for v in [pixel_spacing, extent])):
            raise ValueError("Either 'extent'/'pixel-spacing' keyword argument must be specified")

        if isinstance(data, dict):
            shapes = [v.shape for v in data.values()]
            if not all(shapes[0][0:3] == x[0:3] for x in shapes):
                raise ValueError("Data arrays specified in argument 'data' are not identical:\n"
                                 + "\n".join([str(s) for s in shapes]))
        else:
            shapes = [data.shape, ]

        if extent is not None:
            pixel_spacing = extent.to("m") / np.array(shapes[0])

        shape = np.array(shapes[0][0:3])
        origin = - pixel_spacing * shape / 2 + origin_offset

        mesh = pyvista.UniformGrid(dimensions=shape, spacing=pixel_spacing.m_as("m"),
                                   origin=origin.m_as("m"))

        for name, arr in data.items():
            mesh[name] = arr.reshape([shape.prod(), *arr.shape[3:]], order="F")

        return cls(mesh)

    @classmethod
    def from_shepp_logan(cls, map_size: Tuple[int, int, int], extent: Quantity) \
            -> 'RegularGridDataset':
        """Creates a 3D Shepp-Logan phantom and stores it in a RegularGridDataset.

        :param map_size: Target number of voxels per dimension
        :param extent: Target spatial extent of the resulting shepp-logan phantom.
        """
        try:
            import phantominator
        except ImportError:
            raise ImportError("The python-package phantominator is necessary to create a shepp-"
                              "logan phantom. To install it, type:\n pip install phantominator")

        M0, T1, T2 = phantominator.shepp_logan(map_size, MR=True)
        M0, T1, T2 = [t.transpose(2, 1, 0) for t in [M0, T1, T2]]
        data = dict(rho=M0, T1=T1 * 1000, T2=T2*1000)
        return cls.from_numpy(data=data, extent=extent)
