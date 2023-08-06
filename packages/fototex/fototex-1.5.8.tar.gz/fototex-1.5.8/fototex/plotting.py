# -*- coding: utf-8 -*-

""" Plotting functions for FOTO outputs

"""
import tkinter

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends._backend_tk import NavigationToolbar2Tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from fototex import R_SPECTRA_NO_DATA_VALUE
from fototex._numba import get_bin_sectors, get_sector_directions
from fototex.foto_tools import azimuth_to_counterclockwise, get_window_over_multiple_images

GRID_X = 1
GRID_Y = 1
PAD_FACTOR = 6
PC_AXIS_1 = 0
PC_AXIS_2 = 1
SUBFIG_PAD = 0.06
TK_WINDOW_SIZE = 1000
DPI = 100
NORTH_DIRECTION = 0
NORM_FONT_SIZE = 8
NORM_FONT_COLOR = "red"


def factorial_plan_plot(root, directions,
                        tk_window_size, fig_rel_size,
                        dpi):

    subfig_rel_height = min((1 - fig_rel_size) / 2 - SUBFIG_PAD,
                            1/(1 + len(directions)/4) - SUBFIG_PAD)
    subfig_rel_width = min((1 - fig_rel_size) / 2 - SUBFIG_PAD,
                           1/(1 + len(directions)/4) - SUBFIG_PAD)

    root.wm_title("Factorial plan")
    root.geometry("%dx%d" % (tk_window_size, tk_window_size))

    pad_x = PAD_FACTOR * fig_rel_size
    pad_y = PAD_FACTOR * fig_rel_size
    grid_x_min = (1 - fig_rel_size) / pad_x - GRID_X / 2
    grid_y_min = (1 - fig_rel_size) / pad_y - GRID_Y / 2
    grid_x_max = (pad_x - 1 + fig_rel_size) / pad_x - GRID_X / 2
    grid_y_max = (pad_y - 1 + fig_rel_size) / pad_y - GRID_Y / 2

    main_fig = Figure(dpi=dpi)
    canvas = FigureCanvasTkAgg(main_fig, master=root)
    canvas.get_tk_widget().place(relx=(1 - fig_rel_size) / 2, rely=(1 - fig_rel_size) / 2,
                                 relheight=fig_rel_size, relwidth=fig_rel_size)

    toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
    toolbar.update()

    subfig = []
    canvas_subfig = []

    for i, d in enumerate(directions):

        subfig.append(Figure(dpi=dpi))
        canvas_subfig.append(FigureCanvasTkAgg(subfig[i], master=root))

        if d > 7 * np.pi / 4 or d <= np.pi / 4:
            y = grid_y_max
            x = y / np.tan(azimuth_to_counterclockwise(d))
        elif 3 * np.pi / 4 >= d > np.pi / 4:
            x = grid_x_max
            y = x * np.tan(azimuth_to_counterclockwise(d))
        elif 5 * np.pi / 4 >= d > 3 * np.pi / 4:
            y = grid_y_min
            x = y / np.tan(azimuth_to_counterclockwise(d))
        else:
            x = grid_x_min
            y = x * np.tan(azimuth_to_counterclockwise(d))

        canvas_subfig[i].get_tk_widget().place(relx=x + GRID_X / 2,
                                               rely=GRID_Y / 2 - y,
                                               relwidth=subfig_rel_width,
                                               relheight=subfig_rel_height,
                                               anchor="center")

    toolbar.pack(side="bottom", fill="x")

    return main_fig, subfig, canvas, canvas_subfig


def factorial_plan_quadrants(x, y, nb_quadrants):
    """ Retrieve to which quadrant belong factorial plan points

    Parameters
    ----------
    x: numpy.ndarray
        Axis 2 (horizontal) components
    y: numpy.ndarray
        Axis 1 (vertical) components
    nb_quadrants: int
        Number of quadrants

    Returns
    -------

    """
    sectors = get_bin_sectors(nb_quadrants, 0)
    az = np.arctan2(x, y)
    clusters = np.digitize(az, sectors)
    clusters[clusters == 0] = nb_quadrants

    return clusters


def get_data_range(raster_band, range_min, range_max):
    """ Get data range covered by colormap based on cumulative count cut

    Parameters
    ----------
    raster_band: gdal.Band
        GDAL raster band
    range_min: float
        Minimum relative range value (between 0 and 1)
    range_max: float
        Maximum relative range value (between 0 and 1)

    Returns
    -------
    tuple
        Tuple of data range values as (vmin, vmax)

    """
    min_, max_ = raster_band.ComputeRasterMinMax()
    hist = raster_band.GetHistogram(min_ - 0.5, max_ + 0.5, int(max_ - min_) + 1)
    percentile = np.cumsum(hist) / np.sum(hist)

    vmin = min_ + np.argmax(percentile > range_min)
    vmax = min_ + np.argmax(percentile > range_max) - 1

    return vmin, vmax


def get_norm_indices(axis1, axis2, indices, quadrants,
                     nb_quadrants, nb_values, method):
    """ Retrieve full table indices of PC axis1/axis2 corresponding
    to given norm with respect to method selection

    Parameters
    ----------
    axis1: numpy.ndarray
    axis2: numpy.ndarray
    indices: numpy.ndarray
    quadrants: numpy.ndarray
    nb_quadrants: int
        Number of quadrants
    nb_values: int
        Number of indices to retrieve per quadrant
    method: str
        Method used to retrieve indices corresponding
         to a given norm ('random': at random or
        "max" corresponding to maximum norm values)

    Returns
    -------

    """
    norm = np.sqrt(axis1 ** 2 + axis2 ** 2)

    if method == "random":
        rng = np.random.default_rng()
        norm_idx = [rng.choice(indices[quadrants == n + 1], nb_values, replace=False)
                    for n in range(nb_quadrants)]
    elif method == "max":
        rg_idx = np.arange(0, len(norm))
        norm_idx = [indices[rg_idx[quadrants == n + 1][
            norm[quadrants == n + 1].argsort()[::-1][:nb_values]]]
                    for n in range(nb_quadrants)]
    else:
        norm_idx = []

    return norm, norm_idx


def get_pc_axis(reduced_r_spectra, nb_elements=10000, percentile=None):
    """ Get PC axis values from reduced r-spectra

    Parameters
    ----------
    reduced_r_spectra: h5py._hl.dataset.Dataset or numpy.ndarray
        HDF5 dataset or numpy array of values
    nb_elements: int, default 10000
        Number of elements to select at random in r-spectra table
    percentile: list[float, float]
        If not None, extract cumulative count between percentile bounds

    Returns
    -------
    tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]
    """
    rng = np.random.default_rng()
    indices = np.sort(rng.choice(reduced_r_spectra.shape[0], nb_elements,
                                 replace=False, shuffle=False))
    values = reduced_r_spectra[indices, :]
    indices = indices[values[:, 0] != R_SPECTRA_NO_DATA_VALUE]
    axis1 = values[values[:, 0] != R_SPECTRA_NO_DATA_VALUE, PC_AXIS_1]
    axis2 = values[values[:, 1] != R_SPECTRA_NO_DATA_VALUE, PC_AXIS_2]

    if percentile is not None:
        p = np.percentile(axis1, percentile)
        axis2 = axis2[(axis1 >= p[0]) & (axis1 <= p[1])]
        indices = indices[(axis1 >= p[0]) & (axis1 <= p[1])]
        axis1 = axis1[(axis1 >= p[0]) & (axis1 <= p[1])]

    return axis1, axis2, indices


def plot_correlation_circle(foto, loadings, unit, pca1_on_y_axis, fontsize, circle):
    """ Plot correlation circle

    Thanks to the work of Marc Lang (2018)

    Parameters
    ----------
    foto: fototex.foto.Foto
    loadings: numpy.ndarray
    unit: str
    pca1_on_y_axis: bool
    fontsize: int
    circle: bool

    Returns
    -------

    """
    if unit == 'n_occ':
        frequency_label = range(1, foto.nb_sampled_frequencies + 1)
    elif unit == 'km':
        frequency_label = foto.cycles_km
    else:
        frequency_label = [None for f in range(1, foto.nb_sampled_frequencies + 1)]

    ax = plt.subplots()[1]

    if pca1_on_y_axis:
        pca_x = 1
        pca_y = 0
    else:
        pca_x = 0
        pca_y = 1

    for freq in range(foto.nb_sampled_frequencies):
        x = loadings[freq, pca_x]
        y = loadings[freq, pca_y]
        ax.plot(x, y, '.', color='black')
        if unit:
            ax.text(x, y, f"{frequency_label[freq]}",
                    fontsize=fontsize, color='darkslategrey')

    # Plot circle and legend
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)

    if circle:
        circle = plt.Circle((0, 0), 1, fill=False)
        ax.add_patch(circle)
        ax.axhline(0, color="gray")
        ax.axvline(0, color="gray")

    ax.set_xlabel(f'PC axis {pca_x + 1}')
    ax.set_ylabel(f'PC axis {pca_y + 1}')
    ax.set_title("PC correlation")
    ax.set_facecolor("ivory")

    plt.show()


def plot_factorial_plan(root, foto, window_size, reduced_r_spectra,
                        sliding_window_method, nb_points, data_range, nb_quadrants,
                        method, main_fig_rel_size, nb_of_windows_per_side, contrast_range,
                        pca1_on_y_axis):
    """ Plot factorial plan and corresponding windows for each quadrant

    Parameters
    ----------
    root: tkinter.Tk
        Tkinter root window
    foto: fototex.foto.Foto or fototex.foto.FotoSector or list
    window_size: int
        Size of window used in computing r-spectra
    reduced_r_spectra: h5py._hl.dataset.Dataset or numpy.ndarray
        HDF5 dataset or numpy array of values
    sliding_window_method: str
        Sliding method used in computing r-spectra ('block' or 'moving')
    nb_points: int
        Number of PC points to be plotted
    data_range: list[float, float]
        Data range as cumulative cut count for
        PC axis1 and axis2 (e.g. [2, 98])
    nb_quadrants: int
        Number of quadrants the factorial plan must
        be divided in
    method: str
        Method used to retrieve windows in each quadrant:
        'max' retrieve window(s) with respect to maximum norm
        'random' retrieve window(s) at random in quadrant
    main_fig_rel_size: float
        Relative size of central figure between 0 and 1
    nb_of_windows_per_side: int
        Number of windows per side (Each quadrant corresponds 
        to a square set of windows such as 1x1, 2x2, 3x3, etc.)
    contrast_range: list[float, float]
        Percentile contrast range used to render
        windows with respect to the whole image.
        ex.: enhance contrast based on cumulative
        count cut between 2% and 98% --> [2, 98]
    pca1_on_y_axis: bool
        If True, pca component 1 is set on y axis while pca
        component 2 is set on x axis. If False, pca component 1
        is set on x axis and pca component 2 is set on y axis.

    Returns
    -------

    """
    directions = get_sector_directions(nb_quadrants, NORTH_DIRECTION)
    factorial_plan = factorial_plan_plot(root, directions, TK_WINDOW_SIZE,
                                         main_fig_rel_size, DPI)
    axis1, axis2, indices = get_pc_axis(reduced_r_spectra,
                                        nb_elements=nb_points,
                                        percentile=data_range)

    pca_x_label = "PC axis 2"
    pca_y_label = "PC axis 1"

    if pca1_on_y_axis is False:
        axis1, axis2 = axis2, axis1
        pca_x_label, pca_y_label = pca_y_label, pca_x_label

    if not isinstance(foto, (list, tuple)):
        foto = [foto]

    vmin = [get_data_range(f.dataset.GetRasterBand(f.band),
                           contrast_range[0]/100,
                           contrast_range[1]/100)[0]
            for f in foto]
    vmax = [get_data_range(f.dataset.GetRasterBand(f.band),
                           contrast_range[0]/100,
                           contrast_range[1]/100)[1]
            for f in foto]

    raster_x_size = [f.dataset.RasterXSize for f in foto]
    raster_y_size = [f.dataset.RasterYSize for f in foto]

    quadrants = factorial_plan_quadrants(axis2, axis1, nb_quadrants)
    norm, norm_idx = get_norm_indices(axis1, axis2, indices, quadrants,
                                      nb_quadrants, nb_of_windows_per_side ** 2,
                                      method)

    main_axes = factorial_plan[0].add_subplot(111)
    main_axes.scatter(axis2, axis1, c=quadrants)
    main_axes.set_ylabel(pca_y_label)
    main_axes.set_xlabel(pca_x_label)

    xabs_max = abs(max(main_axes.get_xlim(), key=abs))
    yabs_max = abs(max(main_axes.get_ylim(), key=abs))
    xy_abs_max = max(xabs_max, yabs_max)
    main_axes.set_xlim(xmin=-xy_abs_max, xmax=xy_abs_max)
    main_axes.set_ylim(ymin=-xy_abs_max, ymax=xy_abs_max)

    for i, idx in enumerate(norm_idx):
        sub_axes = factorial_plan[1][i].add_gridspec(nb_of_windows_per_side,
                                                     nb_of_windows_per_side,
                                                     wspace=0, hspace=0).subplots()
        for n, ax in enumerate(sub_axes.ravel()):
            img_id, window = \
                get_window_over_multiple_images(idx[n],
                                                window_size,
                                                raster_x_size,
                                                raster_y_size,
                                                sliding_window_method)
            image = foto[img_id].dataset.GetRasterBand(
                foto[img_id].band).ReadAsArray(*window)
            ax.imshow(image, cmap="gray", vmin=vmin[img_id],
                      vmax=vmax[img_id], aspect="auto")
            ax.set_title(r"$r=%.1f$" % norm[indices == idx[n]], y=1.0,
                         pad=-8, color=NORM_FONT_COLOR, fontsize=NORM_FONT_SIZE)
            ax.set(xticks=[], yticks=[])
            plt.setp(ax.spines.values(), color="white")
        factorial_plan[1][i].subplots_adjust(0, 0, 1, 1)
