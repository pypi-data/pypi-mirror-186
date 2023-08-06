""" Functionality to determine SNR for images """
__all__ = ["calculate_snr", "compute_noise_std"]


from typing import Union, Optional, Iterable
import warnings

import tensorflow as tf
import numpy as np


def calculate_snr(single_coil_images: Union[np.ndarray, tf.Tensor],
                  dynamic_noise_scan: Union[np.ndarray, tf.Tensor],
                  coil_sensitivities: Optional[Union[np.ndarray, tf.Tensor]] = None):
    """Calculates the SNR for a multicoil-acquisition according to doi:10.1002/mrm.21868.
     To guarantee correct scaling this assumes, non-zero-filled reconstruction.

    Previously implemented by Robbert van Gorkum in the MRXCAT project.

    :param single_coil_images: (#coils, X, Y, [Z]) of type complex64
    :param dynamic_noise_scan: (#coils, X, Y, [Z]) of type complex64
    :param coil_sensitivities: Optional: (#coils, X, Y, [Z]) of type complex64 defaults
                                    to ones(1, X, Y, [Z])
    :return: snr_map (X, Y, Z) of type float32
    """
    if coil_sensitivities is None:
        coil_sensitivities = tf.ones_like(single_coil_images)

    denominator = tf.reduce_sum(coil_sensitivities * tf.math.conj(coil_sensitivities), axis=0)

    numerator = tf.reduce_sum(single_coil_images * tf.math.conj(coil_sensitivities), axis=0)
    roemer_noisy_image = numerator / denominator

    numerator_noise = tf.reduce_sum(dynamic_noise_scan * tf.math.conj(coil_sensitivities), axis=0)
    roemer_noise = numerator_noise / denominator

    snr_map = tf.abs(roemer_noisy_image) / tf.math.reduce_std(tf.math.real(roemer_noise))
    return snr_map


def compute_noise_std(noiseless_single_coil_images: Union[np.ndarray, tf.Tensor],
                      target_snr: Iterable[float],
                      coil_sensitivities: Optional[Union[np.ndarray, tf.Tensor]] = None,
                      mask: Optional[Union[np.ndarray, tf.Tensor]] = None, **kwargs) -> np.ndarray:
    """Computes the standard deviation of the complex gaussian noise for a set of target snr given
     multiple single coil images, which are combined on reconstruction.

    :param noiseless_single_coil_images: (n_coils, X, Y, [Z]) of type complex64
    :param target_snr:
    :param coil_sensitivities: (n_coils, X, Y, [Z]) of type complex64, Optional: defaults to
                                    ones(1, X, Y, [Z]) Is used for iterative refinement.

    :param mask: (X, Y, [Z]) Optional: binary mask to specify ROI for SNR computation.
                            Defaults to entire image.
    :param kwargs: - iteratively_refine: (bool) default=True. If True and coil_sensitivities are given, uses iterative method to refine std estimation.


    :return: estimated_stds (np.array) of type np.float32 with shape like np.array(target_snr)
    """
    if mask is None:
        mask = np.ones(noiseless_single_coil_images.shape[1:], dtype=np.float32)

    n_coils = noiseless_single_coil_images.shape[0]

    flat_image = tf.reshape(noiseless_single_coil_images, [n_coils, -1])
    flat_mask = tf.cast(tf.reshape(mask, [-1]), tf.float32)
    number_of_pixels_in_mask = tf.reduce_sum(mask)

    roi_summed_signal_per_coil = tf.einsum('ci, i -> c', tf.abs(flat_image), flat_mask)
    roi_mean_signal_per_coil = roi_summed_signal_per_coil / tf.cast(number_of_pixels_in_mask,
                                                                    tf.float32)
    sum_of_squares_mean = tf.sqrt(tf.reduce_sum(tf.abs(roi_mean_signal_per_coil) ** 2))
    estimated_std = np.array(sum_of_squares_mean / tf.constant(target_snr, dtype=tf.float32))

    if kwargs.get('iteratively_refine', True) and coil_sensitivities is not None:
        assert all((s1 == s2 for s1, s2 in zip(noiseless_single_coil_images.shape,
                                               coil_sensitivities.shape)))
        refined_stds = []
        for target, initial_std in zip(target_snr, estimated_std.flatten()):
            refined_stds += [_iteratively_refine_std_calculation(noiseless_single_coil_images,
                                                                 coil_sensitivities,
                                                                 target, initial_std, mask), ]
        estimated_std = np.array(refined_stds)

    return estimated_std


def _iteratively_refine_std_calculation(noise_less_image: Union[np.ndarray, tf.Tensor],
                                        coil_sensitivities: Union[np.ndarray, tf.Tensor],
                                        target_snr: float, initial_std: Optional[float] = 1.,
                                        mask: Optional[Union[np.ndarray, tf.Tensor]] = None
                                        ) -> float:
    """Iteratively adapts the noise standard deviation while checking the actual Roemer
    reconstructed SNR for multi coil data.

    This is based on the implementation of Robbert van Gorkum in the MRXCAT DIFF package:
    https://git.ee.ethz.ch/kozerkes/mrXCAT/-/blob/MRXCAT_2.0/@MRXCAT_CMR_DIFF/MRXCAT_CMR_DIFF.m

    :param noise_less_image: (n_coils, X, Y, [Z])
    :param coil_sensitivities: (n_coils, X, Y, [Z])
    :param target_snr: float
    :param initial_std: float
    :param mask: (X, Y, [Z])
    :return: refined_snr: float
    """
    if mask is None:
        mask = tf.ones(noise_less_image.shape[1:], dtype=tf.float32)

    # Set up loop variables
    max_iterations = 100
    current_noise_std = initial_std

    number_of_pixels_in_mask = tf.reduce_sum(mask)
    flat_mask = tf.reshape(mask, [-1])

    # Loop and increase/decrease std-estimation as long as target_snr is not met within the
    # tolerance of 0.5 or the maximum number of iterations is reached
    for _ in range(max_iterations):
        noise_vectors = tf.random.normal(shape=(2, ) + tuple(noise_less_image.shape))
        noise_vectors *= current_noise_std
        complex_noise_map = tf.complex(noise_vectors[0], noise_vectors[1])
        noisy_images = noise_less_image + complex_noise_map
        snr_map = calculate_snr(single_coil_images=noisy_images,
                                dynamic_noise_scan=complex_noise_map,
                                coil_sensitivities=coil_sensitivities)

        # Calculate SNR in ROI only (defined by mask argument)
        flat_snr_map = tf.reshape(snr_map, [-1])
        mean_snr_in_roi = tf.reduce_sum(flat_snr_map * flat_mask) / number_of_pixels_in_mask
        snr_diff_to_target = mean_snr_in_roi - target_snr

        if tf.abs(snr_diff_to_target) < 0.4:
            return current_noise_std
        else:
            if snr_diff_to_target < 0:
                current_noise_std *= 0.99
            else:
                current_noise_std *= 1.01

    # This is only reached if tolerance boundary is not reached within 100 iterations.
    warnings.warn("While iteratively refining the noise standard deviation, the target snr was"
                  " not met within defined tolerance boundary (+- 0.5). Function returns value of"
                  " last iteration")
    return current_noise_std
