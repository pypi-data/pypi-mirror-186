# -*- coding: utf-8 -*-

""" Module summary description.

More detailed description.
"""

import numpy as np

from itertools import chain, islice

from sklearn.decomposition import PCA

from fototex import R_SPECTRA_NO_DATA_VALUE
from fototex._numba import sector_average, azimuthal_average, zero_padding, only_contains


def azimuth_to_counterclockwise(az, unit="rad"):
    """ Convert azimuth (N=0°, E=90°, S=180°, W=270°)
    to counterclockwise angle (N=90°, E=0°, S=270°, W=180°)

    Parameters
    ----------
    az: float or numpy.ndarray[float]
        Azimuthal angle
    unit: str
        angle unit of azimuth ('rad', 'deg')

    Returns
    -------

    """
    if unit == "rad":
        return (2 * np.pi - (az - np.pi / 2)) % (2 * np.pi)
    else:
        return (360 - (az - 90)) % 360


def counterclockwise_to_azimuth(ccw, unit="rad"):
    """ Convert counterclockwise angle to azimuth

    Parameters
    ----------
    ccw: float or numpy.ndarray
        Counterclockwise angle
    unit: str
        angle unit of counterclockwise angle ('rad', 'deg')

    Returns
    -------

    """
    if unit == "rad":
        return (5 * np.pi/2 - ccw) % (2 * np.pi)
    else:
        return (450 - ccw) % 360


def degrees_to_cardinal(d):
    """ Convert degrees to cardinal direction

    Thanks to https://gist.github.com/RobertSudwarts/acf8df23a16afdb5837f

    Parameters
    ----------
    d: float

    Returns
    -------
    """
    dirs = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
            "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    ix = int((d + 11.25)/22.5)
    return dirs[ix % 16]


def get_slice_along_axis(ndim, axis, _slice):
    """ Used to make indexing with any n-dimensional numpy array

    Parameters
    ----------
    ndim: int
        number of dimensions
    axis: int
        axis for which we want the slice
    _slice: slice
        the required slice

    Returns
    -------
    """
    slc = [slice(None)] * ndim
    slc[axis] = _slice

    return tuple(slc)


def get_power_spectrum_density(window, normalized):
    """ Compute power spectrum density for given window

    Description
    -----------

    Parameters
    ----------
    window: numpy.ndarray
        2D window
    normalized: bool
        either divide by window variance or not

    Returns
    -------
    """
    # Fast Fourier Transform (FFT) in 2 dims,
    # center fft and then calculate 2D power spectrum density
    ft = np.fft.fft2(window, norm="ortho")
    ft = np.fft.fftshift(ft)
    psd = np.abs(ft) ** 2

    if normalized:
        var = np.var(window)
        if var != 0:
            psd /= var

    return psd


def pca(data, n_components):
    """ Principal component analysis

    Parameters
    ----------
    data: numpy.ndarray
        normalized data array
    n_components: int
        number of dimensions for PCA

    Returns
    -------
    """

    # replace nodata and inf values and standardize
    # data = np.nan_to_num(data)
    # Standardization (mean=0 and std=1)

    # if sklearn_pca:
    sk_pca = PCA(n_components=n_components)
    sk_pca.fit(data)

    eigen_vectors = sk_pca.components_.T
    loadings = eigen_vectors * np.sqrt(sk_pca.explained_variance_)

    return eigen_vectors, loadings, sk_pca.transform(data), sk_pca.explained_variance_ratio_


def rspectrum(window, radius, window_size, nb_sample, normalized, keep_dc_component, no_data_value):
    """ Compute r-spectrum for given window and filter smaller ones and the ones with no data

    Description
    -----------
    Calculate the azimuthally averaged 1D power
    spectrum (also called radial spectrum, i.e. r-spectrum)

    Parameters
    ----------
    window: numpy.ndarray
        window array
    radius: numpy.ndarray
        corresponding radius integer
    window_size: int
        window typical size
    nb_sample: int
        number of frequencies to sample within window
    normalized: bool
        divide r-spectrum by window variance
    keep_dc_component: bool
        either keep DC component of the FFT (0 frequency part of the signal) or not. It
        may substantially change the results, so use it carefully.
    no_data_value: int or float
        value corresponding to no data

    Returns
    -------
    numpy.ndarray:
        array of isotropic r-spectra
    """
    if only_contains(window, no_data_value):
        return np.full(nb_sample, R_SPECTRA_NO_DATA_VALUE)
    else:
        if no_data_value:
            window = zero_padding(window, no_data_value)
        if keep_dc_component:
            return azimuthal_average(radius,
                                     get_power_spectrum_density(window, normalized))[0:nb_sample]
        else:
            return azimuthal_average(radius,
                                     get_power_spectrum_density(window,
                                                                normalized))[1:nb_sample + 1]


def rspectrum_per_sector(window, radius, sectors, window_size, nb_sample,
                         nb_sectors, normalized, keep_dc_component, no_data_value):
    """ Compute r-spectrum for each sector

    Description
    -----------

    Calculate radial spectrum in specific directions, i.e. quadrants

    Parameters
    ----------

    window: numpy.array
        window
    radius:
    sectors: numpy.array
        result from get_sectors function
        (divide the circle into sectors according to nb_sectors)
    window_size: int
        window typical size
    nb_sample: int
        number of frequencies to sample within window
    nb_sectors: int
        number of sectors
    normalized: bool
        divide r-spectrum by window variance
    keep_dc_component: bool
        either keep DC component of the FFT (0 frequency part of the signal) or not. It
        may substantially change the results, so use it carefully.
    no_data_value: int
        value corresponding to no data

    Returns
    -------
    """
    if only_contains(window, no_data_value):
        return np.full((nb_sectors, nb_sample), R_SPECTRA_NO_DATA_VALUE)
    else:
        if no_data_value:
            window = zero_padding(window, no_data_value)
        if keep_dc_component:
            return sector_average(get_power_spectrum_density(window, normalized),
                                  radius, sectors, nb_sectors)[:, 0:nb_sample]
        else:
            return sector_average(get_power_spectrum_density(window, normalized),
                                  radius, sectors, nb_sectors)[:, 1:nb_sample + 1]


def scale_range(array, lower, upper, no_data=None, axis=0):
    """ Scale array to range values

    Parameters
    ----------
    array
    lower: int or float
        lower bound of range
    upper: int or float
        upper bound of range
    no_data
    axis

    Returns
    -------

    """
    if no_data is not None:
        return (array - np.min(array[array != no_data], axis=axis)) * (upper - lower) / \
               (np.max(array[array != no_data], axis=axis) - np.min(array[array != no_data],
                                                                    axis=axis)) + lower
    else:
        return (array - np.min(array, axis=axis)) * (upper - lower) / \
               (np.max(array, axis=axis) - np.min(array, axis=axis)) + lower


def split_into_chunks(iterable, size=10):
    """ Split iterable into chunks

    Parameters
    ----------
    iterable: iterable
    size: int
        size of each chunk

    Returns
    -------
    """
    iterator = iter(iterable)
    for first in iterator:
        yield chain([first], islice(iterator, size - 1))


def standard_deviation(nb_data, sum_of_values, sum_of_square_values):
    """ Compute standard deviation based on variance formula

    Parameters
    ----------
    nb_data: int
        number of data
    sum_of_values:
    sum_of_square_values:

    Returns
    -------
    """
    return np.sqrt(sum_of_square_values / nb_data - (sum_of_values / nb_data) ** 2)


def standardize(data):
    """ Standardize data (subtract mean and divide by std)

    """
    return (data - data.mean(axis=0)) / data.std(axis=0)


def get_window(idx, window_size, raster_x_size,
               raster_y_size, method, step=1):
    """ Get window corresponding to position index

    Parameters
    ----------
    idx: int
        position index
    window_size: int
        Window size
    raster_x_size: int
        Raster X size
    raster_y_size: int
        Raster Y size
    method: str
        Sliding window method {'block', 'moving'}
    step: int, default 1
        Step used in moving window method

    Returns
    -------
    tuple

    """
    if method == "block":
        n_x = raster_x_size // window_size  # + min(1, raster_x_size % window_size)
        n_y = raster_y_size // window_size  # + min(1, raster_y_size % window_size)
        if idx >= (n_x * n_y):
            raise ValueError(f"Position index is out of bounds: {idx} >= {n_x*n_y}")
        y1 = window_size * min(idx // n_x, n_y - 1)
        x1 = window_size * min(idx - (idx // n_x) * n_x, n_x - 1)
        x_size = min(window_size, raster_x_size - x1)
        y_size = min(window_size, raster_y_size - y1)
    else:
        offset = int((window_size - 1) / 2)
        n_x = raster_x_size // step + min(1, raster_x_size % step)
        n_y = raster_y_size // step + min(1, raster_y_size % step)
        if idx >= (n_x * n_y):
            raise ValueError(f"Position index is out of bounds: {idx} >= {n_x*n_y}")
        y = step * (idx // n_x)
        x = (idx - (idx // n_x) * n_x) * step
        x1 = max(0, x - offset)
        y1 = max(0, y - offset)
        x2 = min(raster_x_size - 1, x + offset)
        y2 = min(raster_y_size - 1, y + offset)
        x_size = (x2 - x1) + 1
        y_size = (y2 - y1) + 1

    return int(x1), int(y1), int(x_size), int(y_size)


def get_window_over_multiple_images(idx, window_size, raster_x_size,
                                    raster_y_size, method, step=1):
    """ Get window corresponding to global position index
     over multiple images

    Parameters
    ----------
    idx
    window_size
    raster_x_size
    raster_y_size
    method
    step

    Returns
    -------

    """

    coords = None
    raster_id = 0

    for x_size, y_size in zip(raster_x_size, raster_y_size):
        try:
            coords = get_window(idx, window_size, x_size, y_size, method, step)
            break
        except ValueError:
            if method == "block":
                n_x = x_size // window_size  # + min(1, x_size % window_size)
                n_y = y_size // window_size  # + min(1, y_size % window_size)
            else:
                n_x = x_size // step + min(1, x_size % step)
                n_y = y_size // step + min(1, y_size % step)

            idx -= int(n_x * n_y)
            raster_id += 1

    return raster_id, coords
