# -*- coding: utf-8 -*-

""" Module summary description.

More detailed description.
"""
import itertools
import multiprocessing as mp
import os
import tkinter as tk
from functools import wraps

import numpy as np
from abc import abstractmethod

from fototex import MAX_NB_OF_SAMPLED_FREQUENCIES, NB_PCA_COMPONENTS, R_SPECTRA_NO_DATA_VALUE, \
    _ISOTROPIC_R_SPECTRA_AXIS, _ISOTROPIC_NB_SAMPLE_AXIS, _ANISOTROPIC_R_SPECTRA_AXIS, \
    _ANISOTROPIC_NB_SAMPLE_AXIS, MAX_NB_SECTORS, R_SPECTRA_H5_DS_NAME, \
    REDUCED_R_SPECTRA_H5_DS_NAME, EIGEN_VECTOR_H5_DS_NAME, WINDOW_SIZE_ATTR_NAME, METHOD_ATTR_NAME, LOADINGS_H5_DS_NAME, \
    EXPLAINED_VARIANCE_RATIO_DS_NAME
from fototex._numba import get_sector_directions, get_valid_values
from fototex._tools import mp_r_spectra, mp_h5_r_spectra, normal_pca, \
    h5_incremental_pca, h5_pca_transform, h5_incremental_pca_sector, \
    normal_pca_sector, mp_h5_r_spectra_sector, mp_r_spectra_sector, pca_transform
from fototex.exceptions import FotoBaseError
from fototex.io import H5File, H5TempFile, write_h5
from fototex.plotting import plot_correlation_circle
from fototex.utils import lazyproperty, check_string, check_type, isdir


# TODO: save all FOTO data (eigen vectors, r-spectra and reduced r-spectra) in one unique HDF5 file


def boolean(setter):

    @wraps(setter)
    def _bool(self, value):
        try:
            check_type(value, bool)
        except TypeError:
            raise FotoBaseError("'%s' must be boolean but is: '%s'" %
                                (setter.__name__, type(value).__name__))
        output = setter(self, value)

    return _bool


def directory(setter):

    @wraps(setter)
    def _directory(self, path):
        if not isdir(path):
            raise FotoBaseError("'%s' must be a valid directory path" % setter.__name__)
        output = setter(self, path)

    return _directory


def integer(setter):

    @wraps(setter)
    def _integer(self, value):
        try:
            check_type(value, int)
        except TypeError:
            raise FotoBaseError("'%s' must be an integer value but is: '%s'" %
                                (setter.__name__, type(value).__name__))
        output = setter(self, value)

    return _integer


def odd(setter):

    @wraps(setter)
    def _odd(self, value):
        if value % 2 == 0:
            raise FotoBaseError("'%s' must be an odd value (=%d)" % (setter.__name__, value))
        output = setter(self, value)

    return _odd


def positive(setter):

    @wraps(setter)
    def _positive(self, value):
        if value <= 0:
            raise FotoBaseError("'%s' must be positive (=%d)" % (setter.__name__, value))
        output = setter(self, value)

    return _positive


class FotoBase:
    """ Foto base class

    Main Foto abstract class for all Foto subclasses
    """
    _r_spectra = None
    _r_spectra_reduced = None
    _in_memory = None
    _keep_dc_component = None
    _method = None
    _out_dir = None
    _nb_sampled_frequencies = None
    _normalized = None
    _standardized = None
    _window_size = None
    _window_step = None

    data_chunk_size = None
    max_nb_sampled_frequencies = MAX_NB_OF_SAMPLED_FREQUENCIES
    nb_pca_components = NB_PCA_COMPONENTS
    no_data_value = R_SPECTRA_NO_DATA_VALUE
    eigen_vectors = None
    loadings = None
    explained_variance_ratio = None

    r_spectra_axis = _ISOTROPIC_R_SPECTRA_AXIS
    nb_sample_axis = _ISOTROPIC_NB_SAMPLE_AXIS

    def _compute_pca(self, *args, **kwargs):
        if self.in_memory:
            self.eigen_vectors, \
                self.loadings, \
                self._r_spectra_reduced, \
                self.explained_variance_ratio = normal_pca(self)
        else:
            self.eigen_vectors, \
                self.loadings, \
                self.explained_variance_ratio = h5_incremental_pca(self, *args, **kwargs)

    def _compute_r_spectra(self, nb_processes, *args, **kwargs):
        if self.in_memory:
            self._r_spectra = mp_r_spectra(self, nb_processes)
        else:
            mp_h5_r_spectra(self, nb_processes)

    @abstractmethod
    def _plot_factorial_plan(self, root, window_size, reduced_r_spectra,
                             method, nb_points, data_range, nb_quadrants,
                             norm_method, nb_windows_per_side,
                             main_fig_rel_size, contrast_range, invert_axis,
                             *args, **kwargs):
        pass

    def compute_pca(self, standardized=True, at_random=False,
                    batch_size=None, max_iter=1000, *args, **kwargs):
        """ Compute PCA for r-spectra tables

        Description
        -----------
        Reduce dimensionality of r-spectra table, with
        respect to number of components (by default set
        to 3 for RGB maps calculation), by applying
        principal component analysis (PCA)

        Parameters
        ----------
        standardized : bool
            if True, standardize r-spectrum data before PCA (subtract mean and divide by std)
        at_random: bool
            apply random incremental pca
        batch_size: int
            size of batch for random incremental pca if at_random=True
        max_iter: int
            maximum number of iterations if at_random=True

        Returns
        -------
        FotoBase:
            the current instance
        """
        self.standardized = standardized
        self._compute_pca(at_random, batch_size, max_iter)

    def compute_r_spectra(self, window_size, window_step=1, nb_sampled_frequencies=None,
                          normalized=False, keep_dc_component=False, nb_processes=mp.cpu_count(),
                          *args, **kwargs):
        """ Compute r-spectra over image with respect to sliding window method

        Description
        -----------
        Compute rspectra tables for given image,
        depending on the selected sliding window
        method and other parameters (window size,
        standardization, etc.)

        Parameters
        ---------
        window_size: int
            size of window
        window_step: int, default 1
            step used in sliding window if method is "moving_window"
        nb_sampled_frequencies: int
            number of sampled frequencies (optional)
            If None, is inferred from window size
        normalized: bool
            if True, divide by window variance
        keep_dc_component: bool
            keep the DC component (0 frequency) of the FFT. Use carefully as it may
            substantially change the final results!
        nb_processes: int
            number of processes for multiprocessing calculation

        Returns
        -------
        FotoBase:
            the current instance with r-spectra that have been computed
        """
        # Set window size and standardize bool
        self.window_size = window_size
        self.window_step = window_step
        self.normalized = normalized
        self.keep_dc_component = keep_dc_component

        if not nb_sampled_frequencies:
            self.nb_sampled_frequencies = min(int(window_size / 2),
                                              self.max_nb_sampled_frequencies)
        else:
            self.nb_sampled_frequencies = nb_sampled_frequencies

        self._compute_r_spectra(nb_processes)

    def fit_transform(self, other, nb_processes=mp.cpu_count(), *args, **kwargs):
        """ Apply eigen vectors from other Foto object to current object's R-spectra

        Description
        -----------
        Use the PCA eigen vectors retrieved from
        another FotoBase class that has been run
        in order to get reduced r-spectra for the
        current instance

        Examples
        --------

        Parameters
        ----------
        other : FotoBase
            FotoBase class instance that have been run
        nb_processes : int
            number of processes to open for multiprocessing

        Returns
        -------
        FotoBase:
            the current instance
        """
        # TODO: prototype method (apply eigen vectors computed from some image to another)

        # Compute r-spectra and project in input Foto eigenvector's base
        self.compute_r_spectra(other.window_size,
                               nb_sampled_frequencies=other.nb_sampled_frequencies,
                               normalized=other.normalized,
                               nb_processes=nb_processes)

        if self.in_memory:
            self._r_spectra_reduced = pca_transform(self, other)
        else:
            h5_pca_transform(self, other)

    @abstractmethod
    def get_window_generator(self):
        pass

    def plot_correlation_circle(self, h5path=None, unit='km', invert_axis=False, fontsize=12, circle=True):
        """ Plot correlation circle

        Parameters
        ----------
        h5path: str
            Path to HDF5 file where reduced r-spectra
            are stored. If None, instance r-spectra are
            used. Useful for later plotting.
        unit: str
            'n_occ' or 'km'
        invert_axis: bool
            if True, set PCA 1 on y axis / PCA 2 on x axis
        fontsize: int
            Text size of frequency labels
        circle: bool
            If True, plot circle

        Returns
        -------

        """
        if h5path is not None:
            h5file = H5File(h5path)
            loadings = h5file[LOADINGS_H5_DS_NAME]
        else:
            loadings = self.loadings

        plot_correlation_circle(self, loadings, unit, invert_axis, fontsize, circle)

    def plot_factorial_plan(self, h5path=None, nb_points=10000, data_range=None,
                            nb_quadrants=12, norm_method="max", nb_windows_per_side=2,
                            main_fig_rel_size=0.6, contrast_range=(2, 98), invert_axis=False,
                            *args, **kwargs):
        """ Plot factorial plan and corresponding windows for each quadrant

        Parameters
        ----------
        h5path: str
            Path to HDF5 file where reduced r-spectra
            are stored. If None, instance r-spectra are
            used. Useful for later plotting.
        nb_points: int
            Number of PC points to be plotted
        data_range: list[float, float]
            Data range as cumulative cut count for
            PC axis1 and axis2 (e.g. [2, 98])
        nb_quadrants: int
            Number of quadrants the factorial plan must
            be divided in
        norm_method: str
            Method used to retrieve windows in each quadrant:
            'max' retrieve window(s) with respect to maximum norm
            'random' retrieve window(s) at random in quadrant
        nb_windows_per_side: int
            Number of windows per side (Each quadrant corresponds
            to a square set of windows such as 1x1, 2x2, 3x3, etc.)
        main_fig_rel_size: float
            Relative size of central figure between 0 and 1
        contrast_range: list[float, float]
            Percentile contrast range used to render
            windows with respect to the whole image.
            ex.: enhance contrast based on cumulative
            count cut between 2% and 98% --> [2, 98]
        invert_axis: bool
            if True, set PCA 1 on y axis / PCA 2 on x axis

        Returns
        -------

        """
        # Initialize tkinter window
        root = tk.Tk()

        # Get reduced r-spectra from current instance or from
        # formerly stored HDF5 dataset
        if h5path is not None:
            h5file = H5File(h5path)
            reduced_r_spectra = h5file[REDUCED_R_SPECTRA_H5_DS_NAME]
            window_size = h5file[REDUCED_R_SPECTRA_H5_DS_NAME].attrs[WINDOW_SIZE_ATTR_NAME]
            method = h5file[REDUCED_R_SPECTRA_H5_DS_NAME].attrs[METHOD_ATTR_NAME]
        else:
            reduced_r_spectra = self.r_spectra_reduced
            window_size = self.window_size
            method = self.method

        # Call plot protected method
        self._plot_factorial_plan(root, window_size, reduced_r_spectra, method, nb_points, data_range,
                                  nb_quadrants, norm_method, nb_windows_per_side, main_fig_rel_size,
                                  contrast_range, invert_axis, *args, **kwargs)

        tk.mainloop()

    def run(self, window_size, window_step=1, nb_sampled_frequencies=None, standardized=True,
            normalized=False, keep_dc_component=False, at_random=False, batch_size=None,
            max_iter=1000, nb_processes=mp.cpu_count(), *args, **kwargs):
        """ Run FOTO algorithm

        Description
        -----------
        Run the whole FOTO algorithm, consisting
        in computing r-spectra and applying PCA,
        with respect to window size and corresponding
        method ("block" or "moving window")

        Parameters
        ----------
        window_size : int
            size of the window for 2-D FFT (must be an odd number when method = "moving")
        window_step: int
            Step used in sliding window if method is "moving_window"
        nb_sampled_frequencies : int
            number of sampled frequencies (if None, is inferred)
        standardized : bool
            if True, standardize r-spectrum data before PCA
        normalized : bool
            if True, divide power spectrum density by window's variance
        keep_dc_component : bool
            either keep or not the DC component (0 frequency) part of the signal FFT. Use it
            carefully as it may change substantially the final results !
        at_random: bool
            if True, use random incremental pca
        batch_size: int
            size of batch for random incremental pca (if None, batch size is inferred)
        max_iter: int
            maximum number of iterations when using random incremental PCA
        nb_processes: int
            number of processes for parallelization

        Examples
        --------
        >>> FotoBase.run(window_size=11, keep_dc_component=True)
        >>> FotoBase.run(window_size=15, standardized=False, normalized=True)

        Returns
        -------
        FotoBase :
            the current instance
        """
        self.compute_r_spectra(window_size,
                               window_step,
                               nb_sampled_frequencies,
                               normalized,
                               keep_dc_component,
                               nb_processes)
        self.compute_pca(standardized, at_random, batch_size, max_iter)

    def save_data(self):
        """ Save FOTO data to H5 file

        Returns
        -------

        """
        self.save_eigen_vectors()
        self.save_r_spectra()
        self.save_reduced_r_spectra()

    def save_eigen_vectors(self):
        """ Save eigen vectors computed with PCA

        Description
        -----------
        Write eigen vectors retrieved from PCA
        to H5 file

        Returns
        -------
        """
        write_h5(self,
                 self.eigen_vectors,
                 EIGEN_VECTOR_H5_DS_NAME)

    def save_explained_variance(self):
        """ Save explained variance ratios computed from PCA

        Returns
        -------

        """
        write_h5(self,
                 self.explained_variance_ratio,
                 EXPLAINED_VARIANCE_RATIO_DS_NAME)

    def save_loadings(self):
        """ Save loadings computed with PCA

        Description
        -----------

        Returns
        -------

        """
        write_h5(self,
                 self.loadings,
                 LOADINGS_H5_DS_NAME)

    def save_r_spectra(self):
        """ Save r-spectra table to h5 file

        Description
        -----------
        Write computed r-spectra to H5 file

        Returns
        -------
        """
        write_h5(self,
                 self._r_spectra,
                 R_SPECTRA_H5_DS_NAME,
                 [WINDOW_SIZE_ATTR_NAME, METHOD_ATTR_NAME],
                 [self.window_size, self.method])

    def save_reduced_r_spectra(self):
        """ Save reduced r-spectra to h5 file

        Returns
        -------

        """
        write_h5(self,
                 self._r_spectra_reduced,
                 REDUCED_R_SPECTRA_H5_DS_NAME,
                 [WINDOW_SIZE_ATTR_NAME, METHOD_ATTR_NAME],
                 [self.window_size, self.method])

    @property
    def chunk_size(self):
        return int(self.data_chunk_size / self.nb_sampled_frequencies)

    @property
    def cycles_km(self):
        """ Return sampled frequencies in cycles.km-1

        Returns
        -------

        """
        return [np.round((f * 1000) / (self.window_size * self.pixel_size))
                for f in range(1, self.nb_sampled_frequencies + 1)]

    @lazyproperty
    def h5(self):
        if not self.in_memory:
            return H5TempFile()

    @lazyproperty
    def h5_file(self):
        return H5File(self.path + "foto_data.h5")

    @property
    def in_memory(self):
        return self._in_memory

    @in_memory.setter
    @boolean
    def in_memory(self, value):
        self._in_memory = value

    @property
    def keep_dc_component(self):
        return self._keep_dc_component

    @keep_dc_component.setter
    @boolean
    def keep_dc_component(self, value):
        self._keep_dc_component = value

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, value):
        try:
            self._method = check_string(value, {'block', 'moving_window'})
        except (TypeError, ValueError) as e:
            raise FotoBaseError("Invalid sliding window method: '%s'" % value)

    @property
    @abstractmethod
    def nb_windows(self):
        pass

    @property
    @abstractmethod
    def gdal_no_data_value(self):
        pass

    @property
    @abstractmethod
    def pixel_size(self):
        pass

    @property
    def out_dir(self):
        return self._out_dir

    @out_dir.setter
    @directory
    def out_dir(self, path):
        self._out_dir = path

    @property
    def path(self):
        return os.path.join(self.out_dir, f"{self.__class__.__name__.upper()}_method"
                                          f"={self.method}_wsize="
                                          f"{self.window_size}_wstep={self.window_step}_"
                                          f"dc={self.keep_dc_component}_normalized={self.normalized}_")

    @property
    def mean(self):
        if self.in_memory:
            return get_valid_values(self._r_spectra, self.no_data_value).mean(axis=0)
        else:
            return self.h5[R_SPECTRA_H5_DS_NAME].attrs['mean']

    @property
    def nb_sampled_frequencies(self):
        return self._nb_sampled_frequencies

    @nb_sampled_frequencies.setter
    @integer
    @positive
    def nb_sampled_frequencies(self, value):
        if value < self.nb_pca_components:
            raise ValueError("You cannot sample less frequencies than PCA components ! "
                             "(you may want to check window size)")
        self._nb_sampled_frequencies = value

    @property
    def normalized(self):
        return self._normalized

    @normalized.setter
    @boolean
    def normalized(self, value):
        self._normalized = value

    @property
    def std(self):
        if self.in_memory:
            return get_valid_values(self._r_spectra, self.no_data_value).std(axis=0)
        else:
            return self.h5[R_SPECTRA_H5_DS_NAME].attrs['std']

    @property
    def r_spectra(self):
        if self.in_memory:
            return self._r_spectra
        else:
            return self.h5[R_SPECTRA_H5_DS_NAME]

    @property
    def r_spectra_reduced(self):
        if self.in_memory:
            return self._r_spectra_reduced
        else:
            return self.h5[REDUCED_R_SPECTRA_H5_DS_NAME]

    @property
    def standardized(self):
        return self._standardized

    @standardized.setter
    @boolean
    def standardized(self, value):
        self._standardized = value

    @property
    def window_size(self):
        return self._window_size

    @window_size.setter
    @integer
    @odd
    @positive
    def window_size(self, value):
        self._window_size = value

    @property
    def window_step(self):
        return self._window_step

    @window_step.setter
    @integer
    @positive
    def window_step(self, value):
        self._window_step = value


class Batch(FotoBase):
    """ Batch abstract class

    Description
    -----------
    Batch is used to allow the FOTO algorithm
    to be applied from multiple image batches.
    This class should not be used, but be
    inherited by subclasses that must implement
    the batch process, especially by using
    multiple inheritance
    """

    foto_instances = None

    def get_window_generator(self):
        w_gen = []
        for foto in self.foto_instances:
            w_gen.append(foto.get_window_generator())

        return itertools.chain(*w_gen)

    @property
    @abstractmethod
    def gdal_no_data_value(self):
        pass

    @property
    def nb_windows(self):
        nb_rspec = 0
        for foto in self.foto_instances:
            nb_rspec += foto.nb_windows
        return nb_rspec


class Sector(FotoBase):
    """ Sector abstract method to implement anisotropy within FOTO algorithm

    Note
    ----
    In order to correctly override FotoBase and use Sector with
    other subclasses of FotoBase, we must keep the constructor
    syntax order. That is to put "nb_sectors" at the end. In case
    we later use multiple inheritance, it is very important so that
    there is no conflict between multiple constructors inheriting
    from the same superclass (here FotoBase)
    """

    nb_sectors = None
    start_sector = None
    r_spectra_axis = _ANISOTROPIC_R_SPECTRA_AXIS
    nb_sample_axis = _ANISOTROPIC_NB_SAMPLE_AXIS
    max_nb_sectors = MAX_NB_SECTORS

    def _compute_pca(self, *args, **kwargs):
        if self.in_memory:
            self.eigen_vectors, self._r_spectra_reduced = normal_pca_sector(self)
        else:
            self.eigen_vectors = h5_incremental_pca_sector(self, *args, **kwargs)

    def _compute_r_spectra(self, nb_processes, *args, **kwargs):
        if self.in_memory:
            self._r_spectra = mp_r_spectra_sector(self, nb_processes)
        else:
            self._r_spectra = mp_h5_r_spectra_sector(self, nb_processes)

    def save_eigen_vectors(self):
        """ Save eigen vectors from PCA decomposition

        Description
        -----------

        Returns
        -------
        :return:
        """
        for path, eigen_vectors in zip(self.path, self.eigen_vectors):
            np.savetxt(path + "eigen_vectors.csv", eigen_vectors, delimiter=',')

    @property
    def chunk_size(self):
        return int(self.data_chunk_size / (self.nb_sampled_frequencies * self.nb_sectors))

    @lazyproperty
    def sectors(self):
        return get_sector_directions(self.nb_sectors, self.start_sector) * 180 / np.pi

    @abstractmethod
    def get_window_generator(self):
        pass

    @property
    @abstractmethod
    def nb_windows(self):
        pass
