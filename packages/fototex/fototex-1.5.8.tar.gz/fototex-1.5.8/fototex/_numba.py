# -*- coding: utf-8 -*-

""" Module gathering all numba-based optimized functions

We preferentially use numba jit decorator without signature. As detailed
in the numba documentation in that case:
"The decorated function implements lazy compilation.
Each call to the decorated function will try to re-use an existing
specialization if it exists (for example, a call with two integer
arguments may re-use a specialization for argument types
(numba.int64, numba.int64)). If no suitable specialization exists,
a new specialization is compiled on-the-fly, stored for later use,
and executed with the converted arguments."
"""

import numpy as np

from numba import jit, int64


@jit(nopython=True, nogil=True)
def contains(array, value):
    for n in array.ravel():
        if n == value:
            return True
    return False


@jit(nopython=True, nogil=True)
def only_contains(array, value):
    for n in array.ravel():
        if n != value:
            return False
    return True


# @jit([(float64[:, :], ), (float32[:, :], )], nopython=True, nogil=True)
@jit(nopython=True, nogil=True)
def upper_neighbor(array):
    """ Replace NaNs in given 2D array column by upper neighbor

    Replace NaNs in place in 2D array by
    using nearest upper neighbor
    :param array:
    :return:
    """
    # Using a loop with numba is faster
    for n, value in enumerate(array.ravel()):
        if np.isnan(value):
            array.ravel()[n] = array.ravel()[n - array.shape[1]]

    # Numpy-based method (slower)
    # no_value = np.where(np.isnan(array.ravel()))[0]
    # upper = no_value - array.shape[1]
    # array.ravel()[no_value] = array.ravel()[upper]


# @jit([float64[:](int64[:], float64[:]),
# float32[:](int64[:], float32[:])], nopython=True, nogil=True)
@jit(nopython=True, nogil=True)
def get_average_per_radius(radius, values):
    """ Get average of all values with the same radius

    :param radius:
    :param values:
    :return:
    """
    average = np.bincount(radius, values) / np.bincount(radius)

    return average.astype(values.dtype)


# @jit([(float64[:, :], int64), (float32[:, :], int64)], nopython=True, nogil=True)
@jit(nopython=True, nogil=True)
def get_no_nan(array, idx_col):
    """ Get first no NaN value in column

    :param array:
    :param idx_col:
    :return:
    """
    for value in array[:, idx_col]:
        if ~np.isnan(value):
            return value


# @jit([(float64[:, :], int64[:], int64[:], int64),
#       (float32[:, :], int64[:], int64[:], int64)], nopython=True, nogil=True)
@jit(nopython=True, nogil=True)
def sector_average(window, radius, sectors, nb_sectors):
    window = window.ravel()
    r_average_per_sector = np.zeros((nb_sectors, radius.max() + 1))
    # for sector in np.unique(sectors):
    for sector in range(1, nb_sectors + 1):
        mask = np.where(sectors == sector)
        average = get_average_per_radius(radius[mask], window[mask])
        r_average_per_sector[sector - 1, 0:average.size] = average

    # r_average_per_sector[:, 0] = r_average_per_sector[~np.isnan(r_average_per_sector[:, 0]), 0]
    r_average_per_sector[:, 0] = get_no_nan(r_average_per_sector, 0)
    upper_neighbor(r_average_per_sector)

    return r_average_per_sector


# @jit([float64[:](int64[:], float64[:, :]), float32[:](int64[:],
# float32[:, :])], nopython=True, nogil=True)
@jit(nopython=True, nogil=True)
def azimuthal_average(radius, window):

    return get_average_per_radius(radius, window.ravel())


@jit(nopython=True, nogil=True)
def azimuthal_max(radius, window):

    return get_max_per_radius(radius, window)


@jit(nopython=True, nogil=True)
def get_max_per_radius(radius, window):
    """ Get maximum value in window over each radius

    :param radius:
    :param window:
    :return:
    """
    len_radius = radius.max()
    all_max = np.zeros(len_radius)
    window_view = window.ravel()
    for rad in range(len_radius):
        all_max[rad] = window_view[radius == rad].max()

    return all_max


# @jit(float64[:, :](int64[:, :], int64[:, :]), nopython=True, nogil=True)
@jit(nopython=True, nogil=True)
def get_azimuth(x, y):
    """ Return azimuth of all window pixels with respect to window origin

    :param x: pixel x coordinates as returned by np.indices function
    :param y: pixel y coordinates as returned by np.indices function
    :return:
    """
    return np.arctan2(x - (x.shape[1] - 1) / 2, (y.shape[0] - 1) / 2 - y)


# @jit([float64[:](int64, int64), float64[:](int64, float64)], nopython=True, nogil=True)
@jit(nopython=True, nogil=True)
def get_bin_sectors(nb_bins, center):
    """ Return bin circle sectors from required number of bins

    Return bin sectors centered on specified direction (default North, i.e 0°)
    :param nb_bins: (integer) number of bins
    :param center: center of the bin sectors in radians
    :return:
    """
    bin_vector = np.linspace(-(nb_bins - 1) * np.pi / nb_bins,
                             (nb_bins - 1) * np.pi / nb_bins, nb_bins)
    bin_quadrants = bin_vector + (nb_bins % 2) * np.pi/nb_bins + (center % (2*np.pi))
    bin_quadrants[bin_quadrants < np.pi] = bin_quadrants[bin_quadrants < np.pi] + 2*np.pi
    bin_quadrants[bin_quadrants > np.pi] = bin_quadrants[bin_quadrants > np.pi] - 2*np.pi
    bin_quadrants.sort()

    return bin_quadrants


# @jit([float64[:](int64, int64), float64[:](int64, float64)], nopython=True, nogil=True)
@jit(nopython=True, nogil=True)
def get_sector_directions(nb_sectors, start):
    """ Get direction of each sector

    Index of direction in array gives the bin number
    in get_sectors function (starting from 1)
    :param nb_sectors: number of sectors
    :param start: starting direction
    :return:
    """
    bins = get_bin_sectors(nb_sectors, start)
    inter_bins = (bins[0:-1] + bins[1::]) / 2
    inter_bins = np.asarray(list(inter_bins) + [inter_bins[-1] + 2 * np.pi / nb_sectors])
    inter_bins[inter_bins < 0] = inter_bins[inter_bins < 0] + 2 * np.pi

    return inter_bins


@jit(nopython=True, nogil=True)
def get_block_windows(window_size, raster_x_size, raster_y_size):
    """ Get block window coordinates

    Get block window coordinates depending
    on raster size and window size

    Parameters
    ----------
    window_size: int
        window size
    raster_x_size: int
        raster width
    raster_y_size: int
        raster height

    Returns
    -------

    """
    if raster_x_size % window_size:
        raster_x_size -= (raster_x_size % window_size)
    if raster_y_size % window_size:
        raster_y_size -= (raster_y_size % window_size)

    for y in range(0, raster_y_size, window_size):
        # ysize = min(window_size, raster_y_size - y)
        for x in range(0, raster_x_size, window_size):
            # xsize = min(window_size, raster_x_size - x)

            # yield x, y, xsize, ysize
            yield x, y, window_size, window_size


@jit(nopython=True, nogil=True)
def get_moving_windows(window_size, raster_x_size, raster_y_size, step=1):
    """ Get moving window coordinates

    Get moving window coordinates depending
    on raster size, window size and step

    Parameters
    ----------
    window_size: int
    raster_x_size: int
    raster_y_size: int
    step: int

    Returns
    -------

    """
    offset = int((window_size - 1) / 2)  # window_size must be an odd number
    # for each pixel, compute indices of the window (all included)

    if raster_x_size % step:
        raster_x_size -= (raster_x_size % step)
    if raster_y_size % step:
        raster_y_size -= (raster_y_size % step)

    for y in range(offset, raster_y_size - offset, step):
        y1 = y - offset
        y2 = y + offset
        ysize = (y2 - y1) + 1
        for x in range(offset, raster_x_size - offset, step):
            x1 = x - offset
            x2 = x + offset
            xsize = (x2 - x1) + 1

            yield x1, y1, xsize, ysize


# @jit([int64[:](int64[:, :], int64[:, :], int64, int64),
# int64[:](int64[:, :], int64[:, :], int64, float64)],
#      nopython=True, nogil=True)
@jit(nopython=True, nogil=True)
def get_sectors(x, y, nb_sectors, center):
    sectors = np.digitize(get_azimuth(x, y), get_bin_sectors(nb_sectors, center))
    sectors = sectors.ravel()
    mask = np.where(sectors == 0)
    sectors[mask] = nb_sectors

    return sectors


# @jit(int64[:](int64[:, :], int64[:, :]), nopython=True, nogil=True)
@jit(nopython=True, nogil=True)
def get_radius(x, y):
    """ Return radius of window pixels with respect to window origin

    :param x: pixel x coordinates
    :param y: pixel y coordinates
    :return:
    """
    radius = np.sqrt((x - (x.shape[1] - 1) / 2) ** 2 +
                     (y - (x.shape[0] - 1) / 2) ** 2).astype(int64)

    return radius.ravel()


# @jit([float64[:, :](float64[:, :], int64),
# float32[:, :](float32[:, :], int64)], nopython=True, nogil=True)
@jit(nopython=True, nogil=True)
def get_valid_values(array, no_data_value):
    """ Get valid values from 2d array

    It is assumed that no data are rows (i.e. axis=0)
    Whenever possible (when there is no "no data")
    return a reference to array
    :param array:
    :param no_data_value: value filling entire rows of the given array
    :return:
    """
    view = array.ravel()
    mask = np.where(view != no_data_value)

    if mask[0].size == view.size:
        return array
    else:
        return view[mask].reshape((mask[0].size // array.shape[1], array.shape[1]))


# @jit([float64[:, :, :](float64[:, :, :], int64), float32[:, :, :](float32[:, :, :], int64)],
#      nopython=True, nogil=True)
@jit(nopython=True, nogil=True)
def get_valid_values_3d(array, no_data_value):
    """ Get valid values from 3D array

    No data are plans normal to axis=1, i.e.
    with width along axis=0 and height along axis=2
    :param array:
    :param no_data_value:
    :return:
    """
    view = array.ravel()
    mask = np.where(view != no_data_value)

    if mask[0].size == view.size:
        return array
    else:
        return view[mask].reshape((array.shape[0],
                                   mask[0].size // (array.shape[0] * array.shape[2]),
                                   array.shape[2]))


@jit(nopython=True, nogil=True)
def zero_padding(window, no_data_value):
    """ Replace window no data by window mean

    Description
    -----------
    Replace window no data values by the mean
    over valid window values (corresponds to 0-padding
    with 0s as the mean over standardized windows)
    """
    new_window = window.copy()
    view = new_window.ravel()
    view[view == no_data_value] = view[view != no_data_value].mean()

    return new_window
