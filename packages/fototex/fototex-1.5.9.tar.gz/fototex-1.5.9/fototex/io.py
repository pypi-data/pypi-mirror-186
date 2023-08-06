# -*- coding: utf-8 -*-

""" Module summary description.

More detailed description.
"""

import os
import tempfile

import h5py
import numpy as np
from tqdm import tqdm

from fototex import GDAL_DRIVER, GDAL_FLOAT32, WRITE_RGB_PG_DESCRIPTION
from fototex.exceptions import H5FileAppendError
from fototex.foto_tools import get_slice_along_axis


class H5File:

    def __init__(self, path):
        self.h5 = h5py.File(path, 'a')
        self.path = self.h5.filename
        # Personal note: never put the following line in the class
        # definition (i.e. defined as a class attribute) !! As the
        # dictionary is a mutable object, a modification in any
        # instance will override in all the other instances !!
        self.row_caret_pos = {}

    def __del__(self):
        self.close()

    def __getitem__(self, item):
        if self.has_dataset(item):
            return self.h5[item]

    def append(self, dataset_name, data, axis=0):
        """ Append data to dataset (by row)

        :param dataset_name:
        :param data: data to append to dataset
        :param axis: dataset axis on which append data
        :return:
        """
        if self.has_dataset(dataset_name):
            if dataset_name not in self.row_caret_pos.keys():
                self.row_caret_pos[dataset_name] = 0
            start = self.row_caret_pos[dataset_name]
            self.row_caret_pos[dataset_name] += data.shape[axis]
            idx = get_slice_along_axis(data.ndim, axis,
                                       slice(start, self.row_caret_pos[dataset_name]))
            try:
                self.h5[dataset_name][idx] = data
            except IndexError as e:
                raise H5FileAppendError(e)
            # self.h5[dataset_name][start:self.row_caret_pos[dataset_name], :] = data

    def close(self):
        self.h5.close()

    def copy(self, h5, dataset_name):
        """ Copy H5File dataset to current file

        Dataset must exist in other H5File and must not exist in current file
        :param h5: H5File
        :param dataset_name: name of the corresponding dataset
        :return:
        """
        if h5.has_dataset(dataset_name) and not self.has_dataset(dataset_name):
            self.h5.create_dataset(dataset_name,
                                   data=h5[dataset_name],
                                   shape=h5[dataset_name].shape,
                                   dtype=h5[dataset_name].dtype)

    def create_dataset(self, name, shape, dtype=np.float32):
        """ Create dataset

        :param name:
        :param shape:
        :param dtype:
        :return:
        """
        if not self.has_dataset(name):
            self.h5.create_dataset(name, shape=shape, dtype=dtype)

    def has_dataset(self, name):
        """ Test if h5 file has dataset

        :param name:
        :return:
        """
        return name in self.dataset_names

    def read(self, dataset_name, chunk_size, axis=0):
        """ Sequentially read dataset by row with respect to batch size

        Last batch shall have size <= batch_size

        Parameters
        ----------
        dataset_name: str
        chunk_size: int
        axis: int

        Returns
        -------
        """
        nb_iter = self.h5[dataset_name].shape[axis] // chunk_size + \
            min(1, self.h5[dataset_name].shape[axis] % chunk_size)
        if self.has_dataset(dataset_name):
            for i in range(0, nb_iter):
                yield self.h5[dataset_name][get_slice_along_axis(self.h5[dataset_name].ndim, axis,
                                                                 slice(i * chunk_size,
                                                                       (i+1) * chunk_size))]
                # yield self.h5[dataset_name][i * chunk_size:(i + 1) * chunk_size, :]

    def read_at(self, dataset_name, indices, axis=0):
        """ Read data in dataset at given indices

        Parameters
        ----------
        dataset_name: str
            Name of the dataset
        indices: numpy.ndarray
            indices for which must be returned data in dataset
        axis: int
            Axis for which indices are defined

        Returns
        -------

        """
        if self.has_dataset(dataset_name):
            return self.h5[dataset_name][get_slice_along_axis(self.h5[dataset_name].ndim,
                                                              axis, indices)]

    def read_at_random(self, dataset_name, batch_size, axis=0, max_iter=1000):
        """ Read dataset at random row by row with respect to batch size

        Parameters
        ----------
        dataset_name: str
            Dataset name
        batch_size: int
            Size of each batch to read from dataset
        axis: int
            Axis along which data must be read row by row
        max_iter: int
            Maximum number of iterations for batch process

        Returns
        -------
        """
        rng = np.random.default_rng()
        if self.has_dataset(dataset_name):
            for _ in range(max_iter):
                items = sorted(rng.choice(self.h5[dataset_name].shape[axis],
                                          size=batch_size,
                                          replace=False,
                                          shuffle=False))
                yield self.h5[dataset_name][get_slice_along_axis(self.h5[dataset_name].ndim,
                                                                 axis, items)]
                # yield self.h5[dataset_name][items, :]

    def remove_dataset(self, dataset_name):
        """ Remove dataset within h5 file

        Parameters
        ----------
        dataset_name:

        Returns
        -------
        """
        if self.has_dataset(dataset_name):
            self.reset_caret(dataset_name)
            del self.h5[dataset_name]

    def reset_caret(self, dataset_name):
        try:
            self.row_caret_pos.pop(dataset_name)
        except KeyError:
            pass

    def reset_dataset(self, dataset_name, shape, dtype=np.float32):
        """ Reset dataset

        Parameters
        ----------
        dataset_name: str
            Dataset name
        shape: tuple
            Shape of the dataset table
        dtype:

        Returns
        -------
        """
        self.remove_dataset(dataset_name)
        self.create_dataset(dataset_name, shape, dtype)

    @property
    def dataset_names(self):
        return list(self.h5.keys())

    @property
    def attributes(self):
        return self.h5.attrs

    @property
    def attribute_names(self):
        return list(self.h5.attrs.keys())


class H5TempFile(H5File):

    def __init__(self):

        super().__init__(tempfile.mkstemp(suffix='.h5')[1])

    def __del__(self):
        super().__del__()
        try:
            os.remove(self.path)
        except FileNotFoundError:
            pass


def write_h5(foto, data, ds_name, attr_names=None, attr_values=None):
    """ Write FOTO data into H5 file

    Parameters
    ----------
    foto
    data
    ds_name
    attr_names
    attr_values

    Returns
    -------

    """
    foto.h5_file.remove_dataset(ds_name)
    if foto.in_memory:
        foto.h5_file.create_dataset(ds_name,
                                    shape=data.shape,
                                    dtype=data.dtype)
        foto.h5_file.append(ds_name,
                            data)
    else:
        foto.h5_file.copy(foto.h5, ds_name)

    if attr_names is not None:
        for name, value in zip(attr_names, attr_values):
            foto.h5_file[ds_name].attrs[name] = value


def write_h5_scalar(foto, value, ds_name):
    """ Write FOTO scalar value into H5 file

    Parameters
    ----------
    foto
    value
    ds_name

    Returns
    -------

    """

    foto.h5_file.remove_dataset(ds_name)
    foto.h5_file[ds_name] = value


def write_rgb(foto):
    """ Write RGB image to raster file using gdal

    Write image to raster line by line
    """

    def _write_rgb(rgb_file, r_spectra_reduced):

        try:
            os.remove(rgb_file)
        except FileNotFoundError:
            pass

        # Open or create output dataset
        out_dataset = GDAL_DRIVER.Create(rgb_file,
                                         foto.rgb_width,
                                         foto.rgb_height,
                                         foto.nb_pca_components,
                                         GDAL_FLOAT32)

        topleftx, pxsizex, rotx, toplefty, roty, pxsizey = foto.dataset.GetGeoTransform()

        if foto.method == "block":
            out_dataset.SetGeoTransform((topleftx, pxsizex * foto.window_size, rotx, toplefty, roty,
                                         pxsizey * foto.window_size))
        else:
            out_dataset.SetGeoTransform((topleftx + foto.offset * pxsizex,
                                         pxsizex * foto.window_step, rotx,
                                         toplefty + foto.offset * pxsizey,
                                         roty, pxsizey * foto.window_step))
            # out_dataset.SetGeoTransform(foto.dataset.GetGeoTransform())
        out_dataset.SetProjection(foto.dataset.GetProjection())

        # Set no data value
        for band in range(foto.nb_pca_components):
            out_dataset.GetRasterBand(band + 1).SetNoDataValue(foto.no_data_value)

        # Write to dataset
        row_width = out_dataset.RasterXSize
        for y in tqdm(range(0, out_dataset.RasterYSize),
                      desc=WRITE_RGB_PG_DESCRIPTION % out_dataset.GetDescription(),
                      unit_scale=True):
            for band in range(foto.nb_pca_components):
                rgb = np.expand_dims(r_spectra_reduced[y * row_width:(y + 1) * row_width, band],
                                     axis=0)
                out_dataset.GetRasterBand(band + 1).WriteArray(rgb, 0, y)

        # Close dataset
        out_dataset = None

    try:
        _write_rgb(foto.rgb_file, foto.r_spectra_reduced)
    except (RuntimeError, TypeError):
        for file, r_spectra in zip(foto.rgb_file, foto.r_spectra_reduced):
            _write_rgb(file, r_spectra)
