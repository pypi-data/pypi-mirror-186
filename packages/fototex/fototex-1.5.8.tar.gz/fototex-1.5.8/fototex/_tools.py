# -*- coding: utf-8 -*-

""" Module summary description.

More detailed description.
"""

import multiprocessing as mp
import numpy as np
import time
from functools import partial

from sklearn.decomposition import IncrementalPCA
from tqdm import tqdm

from fototex import R_SPECTRA_PG_DESCRIPTION, R_SPECTRA_SECTOR_PG_DESCRIPTION, \
    INC_PCA_PG_DESCRIPTION, REDUCED_R_SPECTRA_PG_DESCRIPTION, PCA_PG_DESCRIPTION, \
    R_SPECTRA_H5_DS_NAME, REDUCED_R_SPECTRA_H5_DS_NAME, PCA_TRANSFORM_PG_DESCRIPTION, MP_CHUNK_SIZE
from fototex._numba import get_radius, get_sectors, get_valid_values, get_valid_values_3d
from fototex.foto_tools import rspectrum, split_into_chunks, pca, standard_deviation, \
    rspectrum_per_sector, standardize


def incremental_pca(chunks, n_components, no_data_value, axis,
                    population_mean=None, population_std=None,
                    standardized=True, nb_sectors=None):
    """ Incremental PCA

    Description
    -----------

    Parameters
    ----------
    chunks: generator
        iterator over data chunks
    n_components: int
        number of dimensions for PCA
    no_data_value: int
        no data value
    axis: int
        r-spectra axis in data chunks
    population_mean: float
        mean of the entire population from which is extracted each chunk
    population_std: float
        std of the entire population from which is extracted each chunk
    standardized: bool
        True if data must be standardized before pca
    nb_sectors: int
        number of sectors (if None, no sectors)
    Returns
    -------
    """
    if nb_sectors is None:
        ipca = IncrementalPCA(n_components=n_components)
    else:
        ipca = [IncrementalPCA(n_components=n_components)] * nb_sectors

    for chunk in chunks:

        if chunk.ndim == 2:
            chunk = get_valid_values(chunk, no_data_value)
        else:
            chunk = get_valid_values_3d(chunk, no_data_value)

        if standardized:
            if population_mean is None:
                chunk -= np.expand_dims(chunk.mean(axis=axis), axis=axis)
            else:
                chunk -= np.expand_dims(population_mean, axis=axis)

            if population_std is None:
                chunk /= np.expand_dims(chunk.std(axis=axis), axis=axis)
            else:
                chunk /= np.expand_dims(population_std, axis=axis)

        if nb_sectors:
            ipca = [ipca_.partial_fit(sub_chunk) for ipca_, sub_chunk in zip(ipca, chunk)]
        else:
            ipca.partial_fit(chunk)

    return ipca


def pca_transform(foto, other):
    """ Transform, in memory, r-spectra to reduced r-spectra using given PCA eigen vectors

    """
    valid_r_spectra = get_valid_values(foto.r_spectra, foto.no_data_value)
    if other.standardized:
        valid_r_spectra = (valid_r_spectra - other.mean) / other.std
    r_spectra_reduced = np.full((foto.nb_windows, other.nb_pca_components), foto.no_data_value,
                                dtype=foto.r_spectra.dtype)
    r_spectra_reduced[foto.r_spectra[:, 0] != foto.no_data_value, :] = np.dot(valid_r_spectra,
                                                                              other.eigen_vectors)

    return r_spectra_reduced


def h5_pca_transform(foto, other):
    """ Transform R-spectra to reduced R-spectra using given PCA eigen vectors

    """
    nb_chunks = foto.h5[R_SPECTRA_H5_DS_NAME].shape[0] // foto.chunk_size + \
        min(1, foto.h5[R_SPECTRA_H5_DS_NAME].shape[0] % foto.chunk_size)
    foto.h5.reset_dataset(REDUCED_R_SPECTRA_H5_DS_NAME,
                          shape=(foto.h5[R_SPECTRA_H5_DS_NAME].shape[0],
                                 other.eigen_vectors.shape[1]))
    for r_spectra in tqdm(foto.h5.read(R_SPECTRA_H5_DS_NAME, foto.chunk_size),
                          total=nb_chunks, desc=PCA_TRANSFORM_PG_DESCRIPTION):
        r_spectra_reduced = np.full((r_spectra.shape[0], other.nb_pca_components),
                                    foto.no_data_value, dtype=r_spectra.dtype)
        valid_r_spectra = get_valid_values(r_spectra, foto.no_data_value)
        if other.standardized:
            valid_r_spectra = (valid_r_spectra - other.mean) / other.std
        r_spectra_reduced[r_spectra[:, 0] != foto.no_data_value, :] = np.dot(valid_r_spectra,
                                                                             other.eigen_vectors)
        foto.h5.append(REDUCED_R_SPECTRA_H5_DS_NAME, r_spectra_reduced)


# TODO: implement PCA transform for sector R-spectra
def pca_transform_sector():
    pass


def mp_h5_r_spectra(foto, nb_processes):
    """ Parallel processing of r-spectra with hdf5 storage

    """
    nb_sample = foto.nb_sampled_frequencies
    foto.h5.reset_dataset(R_SPECTRA_H5_DS_NAME,
                          (foto.nb_windows, nb_sample))

    # Pixel coordinates within window
    y, x = np.indices((foto.window_size, foto.window_size))
    radius = get_radius(x, y)

    # For statistics computation (population mean and std)
    sum_of_values = np.zeros(nb_sample)
    sum_of_square_values = np.zeros(nb_sample)
    nb_valid_r_spectra = 0

    # Compute r-spectra chunk by chunk
    pg = tqdm(total=foto.nb_windows // foto.chunk_size + 1, desc=R_SPECTRA_PG_DESCRIPTION)
    for chk_nb, window_generator in enumerate(split_into_chunks(foto.get_window_generator(),
                                                                foto.chunk_size)):
        with mp.Pool(processes=nb_processes) as pool:
            r_spectra = np.asarray(list(pool.map(partial(rspectrum, radius=radius,
                                                         window_size=foto.window_size,
                                                         nb_sample=nb_sample,
                                                         normalized=foto.normalized,
                                                         keep_dc_component=foto.keep_dc_component,
                                                         no_data_value=foto.gdal_no_data_value),
                                                 window_generator, chunksize=MP_CHUNK_SIZE)))
        valid_r_spectra = get_valid_values(r_spectra, foto.no_data_value)
        nb_valid_r_spectra += valid_r_spectra.shape[foto.r_spectra_axis]
        sum_of_values += np.sum(valid_r_spectra, axis=foto.r_spectra_axis)
        sum_of_square_values += np.sum(valid_r_spectra**2, axis=foto.r_spectra_axis)
        foto.h5.append(R_SPECTRA_H5_DS_NAME, r_spectra)
        pg.update(1)
    pg.close()

    # Write dataset statistics to attributes
    foto.h5[R_SPECTRA_H5_DS_NAME].attrs['mean'] = sum_of_values / nb_valid_r_spectra
    foto.h5[R_SPECTRA_H5_DS_NAME].attrs['std'] = standard_deviation(nb_valid_r_spectra,
                                                                    sum_of_values,
                                                                    sum_of_square_values)

    # TODO: see if chunksize for Pool.map should not be fixed (500 here)


def mp_h5_r_spectra_sector(foto, nb_processes):
    """ Parallel processing of anisotropic r-spectra with hdf5 storage

    """
    nb_sample = foto.nb_sampled_frequencies

    foto.h5.reset_dataset(R_SPECTRA_H5_DS_NAME,
                          (foto.nb_sectors, foto.nb_windows, nb_sample))
    y, x = np.indices((foto.window_size, foto.window_size))
    radius = get_radius(x, y)
    sectors = get_sectors(x, y, foto.nb_sectors, foto.start_sector)

    # Data used for population statistics
    sum_of_values = np.zeros((foto.nb_sectors, nb_sample))
    sum_of_square_values = np.zeros((foto.nb_sectors, nb_sample))
    nb_valid_r_spectra = 0

    # Compute r-spectra chunk by chunk
    pg = tqdm(total=foto.nb_windows // foto.chunk_size + 1, desc=R_SPECTRA_SECTOR_PG_DESCRIPTION)

    for chk_nb, window_generator in \
            enumerate(split_into_chunks(foto.get_window_generator(), foto.chunk_size)):
        with mp.Pool(processes=nb_processes) as pool:
            r_spectra = list(pool.map(partial(rspectrum_per_sector, radius=radius, sectors=sectors,
                                              window_size=foto.window_size, nb_sample=nb_sample,
                                              nb_sectors=foto.nb_sectors,
                                              normalized=foto.normalized,
                                              keep_dc_component=foto.keep_dc_component,
                                              no_data_value=foto.gdal_no_data_value),
                                      window_generator, chunksize=MP_CHUNK_SIZE))
        r_spectra = np.transpose(np.asarray(r_spectra), (1, 0, 2))
        valid_r_spectra = get_valid_values_3d(r_spectra, foto.no_data_value)
        nb_valid_r_spectra += valid_r_spectra.shape[foto.r_spectra_axis]
        sum_of_values += np.sum(valid_r_spectra, axis=foto.r_spectra_axis)
        sum_of_square_values += np.sum(valid_r_spectra ** 2, axis=foto.r_spectra_axis)
        foto.h5.append(R_SPECTRA_H5_DS_NAME,
                       r_spectra, axis=foto.r_spectra_axis)
        pg.update(1)
    pg.close()

    # Write dataset statistics to attributes
    foto.h5[R_SPECTRA_H5_DS_NAME].attrs['mean'] = sum_of_values / nb_valid_r_spectra
    foto.h5[R_SPECTRA_H5_DS_NAME].attrs['std'] = standard_deviation(nb_valid_r_spectra,
                                                                    sum_of_values,
                                                                    sum_of_square_values)


def mp_r_spectra(foto, nb_processes):
    """ Parallel processing of isotropic r-spectra in memory

    """
    nb_sample = foto.nb_sampled_frequencies

    # Pixel coordinates within window
    y, x = np.indices((foto.window_size, foto.window_size))
    radius = get_radius(x, y)

    # Parallel computation of r-spectra
    with mp.Pool(processes=nb_processes) as pool:
        r_spectra = list(tqdm(pool.imap(partial(rspectrum, radius=radius,
                                                window_size=foto.window_size,
                                                nb_sample=nb_sample, normalized=foto.normalized,
                                                keep_dc_component=foto.keep_dc_component,
                                                no_data_value=foto.gdal_no_data_value),
                                        foto.get_window_generator(), chunksize=MP_CHUNK_SIZE),
                              total=foto.nb_windows, unit_scale=True,
                              desc=R_SPECTRA_PG_DESCRIPTION))

    return np.asarray(r_spectra)


def mp_r_spectra_sector(foto, nb_processes):
    """ Parallel processing of r-spectra

    """
    nb_sample = foto.nb_sampled_frequencies

    # Get radius and sectors within window
    y, x = np.indices((foto.window_size, foto.window_size))
    radius = get_radius(x, y)
    sectors = get_sectors(x, y, foto.nb_sectors, foto.start_sector)

    # Parallel computation of r-spectra
    with mp.Pool(processes=nb_processes) as pool:
        r_spectra = list(tqdm(pool.imap(partial(rspectrum_per_sector,
                                                radius=radius,
                                                sectors=sectors,
                                                window_size=foto.window_size,
                                                nb_sample=nb_sample,
                                                nb_sectors=foto.nb_sectors,
                                                normalized=foto.normalized,
                                                keep_dc_component=foto.keep_dc_component,
                                                no_data_value=foto.gdal_no_data_value),
                                        foto.get_window_generator(), chunksize=MP_CHUNK_SIZE),
                              total=foto.nb_windows, unit_scale=True,
                              desc=R_SPECTRA_SECTOR_PG_DESCRIPTION))
        r_spectra = np.transpose(np.asarray(r_spectra), (1, 0, 2))

    return r_spectra


def h5_incremental_pca(foto, at_random, batch_size, max_iter):
    """ Incremental PCA based on hdf5 dataset chunks

    """
    nb_chunks = foto.nb_windows // foto.chunk_size + min(1, foto.nb_windows % foto.chunk_size)
    population_mean = foto.h5[R_SPECTRA_H5_DS_NAME].attrs["mean"]
    population_std = foto.h5[R_SPECTRA_H5_DS_NAME].attrs["std"]

    if at_random:
        if batch_size is None:
            batch_size = foto.nb_sampled_frequencies * 2**3
        r_spectra_generator = foto.h5.read_at_random(R_SPECTRA_H5_DS_NAME, batch_size)
        nb_iterations = max_iter
    else:
        r_spectra_generator = foto.h5.read(R_SPECTRA_H5_DS_NAME, foto.chunk_size)
        nb_iterations = nb_chunks

    # Incremental PCA
    # Read R-spectra by chunk or batch (if at random) and partial fit
    chunks = tqdm(r_spectra_generator, total=nb_iterations, desc=INC_PCA_PG_DESCRIPTION)
    ipca = incremental_pca(chunks, foto.nb_pca_components, foto.no_data_value, foto.r_spectra_axis,
                           population_mean, population_std, foto.standardized)

    # Finalization
    # Write R-spectra reduced to hdf5 dataset
    foto.h5.reset_dataset(REDUCED_R_SPECTRA_H5_DS_NAME,
                          shape=(foto.nb_windows, foto.nb_pca_components))
    for r_spectra in tqdm(foto.h5.read(R_SPECTRA_H5_DS_NAME, foto.chunk_size),
                          total=nb_chunks, desc=REDUCED_R_SPECTRA_PG_DESCRIPTION):
        r_spectra_reduced = np.full((r_spectra.shape[0], foto.nb_pca_components),
                                    foto.no_data_value, dtype=r_spectra.dtype)
        valid_r_spectra = get_valid_values(r_spectra, foto.no_data_value)
        if foto.standardized:
            valid_r_spectra = (valid_r_spectra - population_mean) / population_std
        try:
            r_spectra_reduced[r_spectra[:, 0] != foto.no_data_value, :] = \
                ipca.transform(valid_r_spectra)
        except ValueError:  # If valid_r_spectra is empty, ipca.transform returns ValueError
            pass
        foto.h5.append(REDUCED_R_SPECTRA_H5_DS_NAME, r_spectra_reduced)

    eigen_vectors = ipca.components_.T
    loadings = eigen_vectors * np.sqrt(ipca.explained_variance_)

    return eigen_vectors, loadings, ipca.explained_variance_ratio_


def h5_incremental_pca_sector(foto, at_random, batch_size, max_iter):
    """ Apply incremental PCA for anisotropic r-spectra based on H5 datasets

    """
    nb_chunks = foto.nb_windows // foto.chunk_size + min(1, foto.nb_windows % foto.chunk_size)
    population_mean = foto.h5[R_SPECTRA_H5_DS_NAME].attrs["mean"]
    population_std = foto.h5[R_SPECTRA_H5_DS_NAME].attrs["std"]

    if at_random:
        if batch_size is None:
            batch_size = foto.nb_sampled_frequencies * 2**3
        r_spectra_generator = foto.h5.read_at_random(R_SPECTRA_H5_DS_NAME,
                                                     batch_size,
                                                     axis=foto.r_spectra_axis)
        nb_iterations = max_iter
    else:
        r_spectra_generator = foto.h5.read(R_SPECTRA_H5_DS_NAME,
                                           foto.chunk_size,
                                           axis=foto.r_spectra_axis)
        nb_iterations = nb_chunks

    # Incremental PCA
    # Read R-spectra by chunk or batch (if at random) and partial fit
    chunks = tqdm(r_spectra_generator, total=nb_iterations, desc=INC_PCA_PG_DESCRIPTION)
    ipca = incremental_pca(chunks, foto.nb_pca_components, foto.no_data_value, foto.r_spectra_axis,
                           population_mean, population_std, foto.standardized, foto.nb_sectors)

    # Finalization
    # Write R-spectra reduced to hdf5 dataset
    foto.h5.reset_dataset(REDUCED_R_SPECTRA_H5_DS_NAME,
                          shape=(foto.nb_sectors, foto.nb_windows, foto.nb_pca_components))
    for r_spectra in tqdm(foto.h5.read(R_SPECTRA_H5_DS_NAME, foto.chunk_size,
                                       axis=foto.r_spectra_axis),
                          total=nb_chunks, desc=REDUCED_R_SPECTRA_PG_DESCRIPTION):
        r_spectra_reduced = np.full((foto.nb_sectors, r_spectra.shape[1], foto.nb_pca_components),
                                    foto.no_data_value, dtype=r_spectra.dtype)
        valid_r_spectra = get_valid_values_3d(r_spectra, foto.no_data_value)
        if foto.standardized:
            valid_r_spectra -= np.expand_dims(population_mean, axis=foto.r_spectra_axis)
            valid_r_spectra /= np.expand_dims(population_std, axis=foto.r_spectra_axis)
        ipca_transform = np.asarray([ipca_.transform(sector_r_spectra)
                                     for ipca_, sector_r_spectra in zip(ipca, valid_r_spectra)])
        r_spectra_reduced[:, r_spectra[0, :, 0] != foto.no_data_value, :] = ipca_transform
        foto.h5.append(REDUCED_R_SPECTRA_H5_DS_NAME,
                       r_spectra_reduced,
                       axis=foto.r_spectra_axis)

    return [ipca_.components_.T for ipca_ in ipca]


def normal_pca(foto):
    """ Normal PCA

    """
    valid_r_spectra = get_valid_values(foto.r_spectra, foto.no_data_value)
    if foto.standardized:
        valid_r_spectra = standardize(valid_r_spectra)

    # Start PCA process
    quit_process = mp.Event()
    p = mp.Process(target=_tqdm_pca, args=(valid_r_spectra.size // 100, quit_process))
    p.start()

    #
    r_spectra_reduced = np.full((foto.nb_windows, foto.nb_pca_components), foto.no_data_value,
                                dtype=foto.r_spectra.dtype)
    eigen_vectors, loadings, r_spectra_reduced[foto.r_spectra[:, 0] != foto.no_data_value, :] = \
        pca(valid_r_spectra, foto.nb_pca_components)
    # eigen_vectors, r_spectra_reduced = pca(foto.r_spectra, foto.nb_pca_components)

    # Stop PCA process
    quit_process.set()
    p.join()

    return eigen_vectors, loadings, r_spectra_reduced


def normal_pca_sector(foto):
    """ Compute PCA for each quadrant

    """
    valid_r_spectra = get_valid_values_3d(foto.r_spectra, foto.no_data_value)

    quit_process = mp.Event()
    p = mp.Process(target=_tqdm_pca,
                   args=(foto.nb_sectors * valid_r_spectra.size // 100, quit_process))
    p.start()

    r_spectra_reduced = np.full((foto.nb_sectors, foto.nb_windows, foto.nb_pca_components),
                                foto.no_data_value, dtype=foto.r_spectra.dtype)
    if foto.standardized:
        results = [pca(standardize(rspec), foto.nb_pca_components) for rspec in valid_r_spectra]
    else:
        results = [pca(rspec, foto.nb_pca_components) for rspec in valid_r_spectra]
    eigen_vectors = np.asarray([result[0] for result in results])
    r_spectra_reduced[:, foto.r_spectra[0, :, 0] != foto.no_data_value, :] = \
        np.asarray([result[1] for result in results])

    # Stop PCA process
    quit_process.set()
    p.join()

    return eigen_vectors, r_spectra_reduced


def _tqdm_pca(bar_length, quit_process):
    pg = tqdm(total=bar_length, desc=PCA_PG_DESCRIPTION, unit_scale=True)
    for i in range(int(bar_length)):
        pg.update(1)
        time.sleep(0.0001)
        if quit_process.is_set():
            break
    pg.n = bar_length
    pg.refresh()
    pg.close()
