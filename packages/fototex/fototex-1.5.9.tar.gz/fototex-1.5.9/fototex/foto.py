# -*- coding: utf-8 -*-

""" FOTO main module.

Main module of FOTO algorithm. Defines FotoBase class and inherited classes.
"""

import multiprocessing as mp
import os
from abc import abstractmethod

try:
    import gdal
except ModuleNotFoundError:
    from osgeo import gdal

from fototex.base import FotoBase, Batch, Sector
from fototex.plotting import plot_factorial_plan
from fototex.utils import lazyproperty, check_type_in_collection

from fototex.exceptions import FotoBatchError, FotoError, FotoSectorBatchError
from fototex._numba import get_block_windows, get_moving_windows
from fototex.foto_tools import degrees_to_cardinal
from fototex.io import write_rgb


# TODO: add standardize and keep_dc_component options in path names ?


class Foto(FotoBase):
    """ Foto class instance

    Foto object allows to run the Foto algorithm (Couteron et al., 2006) on
    any kind of raster.
    """

    def __init__(self, image, band=None, method="block", in_memory=True,
                 data_chunk_size=50000, *args, **kwargs):
        """ Foto class constructor

        Description
        -----------
        Build a Foto object on which might
        later be run the algorithm. It is
        specifically designed to run on one
        image.

        Parameters
        ----------
        image: str
            path to raster file (must be gdal readable)
        band: int
            band number if multi-band raster
        method: str
            method for window analysis ("block" or "moving")
        in_memory: bool
            if True, import whole raster or band as numpy array
        data_chunk_size: int
            size (nb of elements) of a chunk of data to load in memory (if in_memory == False)
        """
        try:
            self.dataset = gdal.Open(image, gdal.GA_ReadOnly)
        except RuntimeError as e:
            raise FotoError(e)

        if band is None:
            self.band = 1
        else:
            self.band = band

        self.out_dir = os.path.dirname(self.dataset.GetDescription())
        self.method = method
        self.in_memory = in_memory
        self.data_chunk_size = data_chunk_size

    def __del__(self):
        # Explicitly close GDAL dataset
        self.dataset = None

    def _plot_factorial_plan(self, root, window_size, reduced_r_spectra,
                             method, nb_points, data_range, nb_quadrants,
                             norm_method, nb_windows_per_side,
                             main_fig_rel_size, contrast_range, invert_axis,
                             *args, **kwargs):

        plot_factorial_plan(root, self, window_size, reduced_r_spectra, method,
                            nb_points, data_range, nb_quadrants, norm_method,
                            main_fig_rel_size, nb_windows_per_side, contrast_range,
                            invert_axis)

    def get_window_generator(self):
        """ Create window generator depending on the given memory method

        :return: window generator
        """
        if self.in_memory:
            return (self.image[w[1]:w[1] + w[3], w[0]:w[0] + w[2]] for w in self.windows)
        else:
            return (self.dataset.GetRasterBand(self.band).ReadAsArray(*window)
                    for window in self.windows)

    def save_rgb(self):
        """ Save RGB image to file using gdal

        Description
        -----------
        Save reduced r-spectra table to RGB map

        Returns
        -------
        """
        write_rgb(self)

    @property
    def nb_windows(self):
        return self.rgb_height * self.rgb_width

    @lazyproperty
    def image(self):
        if self.in_memory:
            return self.dataset.GetRasterBand(self.band).ReadAsArray()

    @property
    def image_name(self):
        return os.path.splitext(os.path.split(self.dataset.GetDescription())[1])[0]

    @lazyproperty
    def gdal_no_data_value(self):
        return self.dataset.GetRasterBand(self.band).GetNoDataValue()

    @property
    def offset(self):
        return int((self.window_size - 1) / 2)

    @property
    def path(self):
        new_path = super().path
        return new_path + f"image={self.image_name}_"

    @property
    def pixel_size(self):
        return self.dataset.GetGeoTransform()[1]  # TODO: be sure units are meters

    @property
    def rgb_file(self):
        return self.path + "rgb.tif"

    @property
    def rgb_width(self):
        if self.method == "block":
            return int(self.dataset.RasterXSize / self.window_size) #+ \
                   # min(1, self.dataset.RasterXSize % self.window_size)
        else:
            return int((self.dataset.RasterXSize - 2 * self.offset) / self.window_step) #+ \
                   # min(1, self.dataset.RasterXSize % self.window_step)

    @property
    def rgb_height(self):
        if self.method == "block":
            return int(self.dataset.RasterYSize / self.window_size) #+ \
                   # min(1, self.dataset.RasterYSize % self.window_size)
        else:
            return int((self.dataset.RasterYSize - 2 * self.offset) / self.window_step) #+ \
                   # min(1, self.dataset.RasterYSize % self.window_step)

    @property
    def windows(self):
        if self.method == 'block':
            return get_block_windows(self.window_size, self.dataset.RasterXSize,
                                     self.dataset.RasterYSize)
        else:
            return get_moving_windows(self.window_size, self.dataset.RasterXSize,
                                      self.dataset.RasterYSize, self.window_step)


class FotoBatch(Batch):
    """ FotoBatch class

    FotoBatch allows for supplying image batches to the Foto algorithm
    """

    def __init__(self, out_dir, foto_collection, method="block",
                 in_memory=True, data_chunk_size=50000):
        """ Build FotoBatch instance

        Description
        -----------
        FotoBatch instance allows for applying the
        FOTO algorithm on multiple images (batches)

        Parameters
        ----------
        out_dir: str
            path to directory where outputs will be saved
        foto_collection: list or tuple
            collection of Foto instances
        method: str
            sliding window method {'block' or 'moving_window'}
        in_memory: bool
            either implement FOTO in memory or using HDF5 file storage on the fly
        data_chunk_size: int
            if HDF5 storage is implemented, number of data per chunk
        """
        # Store Foto instances of images
        try:
            check_type_in_collection(foto_collection, Foto)
            self.foto_instances = foto_collection
        except TypeError as e:
            raise FotoBatchError(e)

        self.out_dir = out_dir
        self.method = method
        self.in_memory = in_memory
        self.data_chunk_size = data_chunk_size

    def _plot_factorial_plan(self, root, window_size, reduced_r_spectra,
                             method, nb_points, data_range, nb_quadrants,
                             norm_method, nb_windows_per_side,
                             main_fig_rel_size, contrast_range, invert_axis,
                             *args, **kwargs):

        plot_factorial_plan(root, self.foto_instances, window_size, reduced_r_spectra, method,
                            nb_points, data_range, nb_quadrants, norm_method, main_fig_rel_size,
                            nb_windows_per_side, contrast_range, invert_axis)

    def compute_r_spectra(self, window_size, window_step=1, nb_sampled_frequencies=None,
                          normalized=False, keep_dc_component=False, nb_processes=mp.cpu_count(),
                          *args, **kwargs):
        """ Compute r-spectra tables for all batches

        Description
        -----------
        Compute r-spectra table from all supplied
        image batches

        Parameters
        ----------
        window_size: int
            size of window
        window_step: int
            step used in sliding window if method is "moving_window"
        nb_sampled_frequencies: int
            number of frequencies to sample
        normalized: bool
            if True, divide by window variance
        keep_dc_component: bool
            if True, keep DC component in FFT
        nb_processes: int
            number of processes for multiprocessing
        args:
        kwargs:

        Returns
        -------
        FotoBatch:
            the current instance
        """
        for foto in self.foto_instances:
            foto.window_size = window_size
            foto.window_step = window_step
        super().compute_r_spectra(window_size, window_step, nb_sampled_frequencies,
                                  normalized, keep_dc_component, nb_processes)

    @property
    @abstractmethod
    def gdal_no_data_value(self):
        pass


class FotoSector(Foto, Sector):

    def __init__(self, image, nb_sectors=6, start_sector=0, band=None,
                 method="block", in_memory=True, data_chunk_size=50000):
        """ FotoSector constructor

        Description
        -----------
        FotoSector apply the anisotropic version
        of the FOTO algorithm. Typically, depending
        on the required number of sectors, r-spectra
        will be computed for each sector, i.e. circle
        division.

        Parameters
        ----------
        image: str
            valid path to raster image
        nb_sectors: int
            number of sectors
        start_sector: float
            sectors' starting direction (by default: North, i.e 0°)
        band: int
            band number
        method: str
            window sliding method
        in_memory: bool
            if True, store all computations in memory, otherwise use H5 file storage on-the-fly
        data_chunk_size: int
            when using H5 storage, number of data per chunk when reading/writing from/to file

        Note
        ----
        We use here the feature of multiple inheritance,
        by building FotoSector as the mixin of Foto and
        Sector. Look at the Note in Sector to understand
        how to avoid typical issues when doing this. Here,
        Foto and Sector both inherit from FotoBase, as a result
        we must take care of the argument order in the constructor
        of both Foto and Sector classes.
        """
        self.nb_sectors = nb_sectors
        self.start_sector = start_sector

        super().__init__(image, band, method, in_memory, data_chunk_size)

    @property
    def path(self):
        new_path = super().path
        return [new_path + f"sector={sector:.0f}_{degrees_to_cardinal(sector)}_"
                for sector in self.sectors]

    @property
    def rgb_file(self):
        return [path + "rgb.tif" for path in self.path]


class FotoSectorBatch(FotoBatch, Sector):

    def __init__(self, out_dir, foto_collection, nb_sectors=6, start_sector=0,
                 method="block", in_memory=True, data_chunk_size=50000):
        """ FotoSectorBatch

        Description
        -----------
        Run FOTO anisotropic algorithm from
        image batches

        Parameters
        ----------
        out_dir: str
            valid path to output directory where results must be stored
        foto_collection: list or tuple
            collection of FotoSector instances
        nb_sectors: int
            number of sectors
        start_sector: int
            starting sector
        method: str
            valid sliding window method
        in_memory: bool
            if True, all computations are made in memory, otherwise use H5 storage on-the-fly
        data_chunk_size: int
            if H5 storage is used, number of data per chunk when reading/writing from/to file
        """
        super().__init__(out_dir, foto_collection, method, in_memory, data_chunk_size)

        try:
            check_type_in_collection(foto_collection, FotoSector)
        except TypeError as e:
            raise FotoSectorBatchError(e)

    @property
    @abstractmethod
    def gdal_no_data_value(self):
        pass
