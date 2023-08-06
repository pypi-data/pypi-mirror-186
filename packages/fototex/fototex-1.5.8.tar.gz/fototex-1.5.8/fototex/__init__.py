# -*- coding: utf-8 -*-

""" Compute Fourier Transform Textural Ordination.

FOTO algorithm package by and for python. Use to retrieve
textural information in satellite images.

- Example of usage:
>>> from fototex.foto import Foto
>>> foto = Foto("/path/to/image.tif", method="moving_window")
>>> foto.run(window_size=11)

"""

__version__ = '1.5.8'
__licence__ = "MIT"

try:
    import gdal
except ModuleNotFoundError:
    from osgeo import gdal

# Raise Python exceptions for gdal errors
gdal.UseExceptions()

# Multiprocessing variables
MP_CHUNK_SIZE = 5000

# R-spectra table axis (depending on number of dimensions)
# Isotropic: 2 dimensions, anisotropic: 3 dimensions
# Only advised users might modify it
_ISOTROPIC_R_SPECTRA_AXIS = 0
_ANISOTROPIC_R_SPECTRA_AXIS = 1
_ISOTROPIC_NB_SAMPLE_AXIS = 1
_ANISOTROPIC_NB_SAMPLE_AXIS = 2

# GDAL drivers and data type
GDAL_DRIVER = gdal.GetDriverByName("GTiff")
GDAL_FLOAT32 = gdal.GetDataTypeByName('Float32')

# Main variables
NB_PCA_COMPONENTS = 3
MAX_NB_OF_SAMPLED_FREQUENCIES = 29
MAX_NB_SECTORS = 16
R_SPECTRA_NO_DATA_VALUE = -999

# Progress descriptions
PCA_TRANSFORM_PG_DESCRIPTION = "Reduce R-spectra"
PCA_PG_DESCRIPTION = "Run Principal Component Analysis"
INC_PCA_PG_DESCRIPTION = "Run incremental PCA"
R_SPECTRA_PG_DESCRIPTION = "Retrieve isotropic R-spectra"
R_SPECTRA_SECTOR_PG_DESCRIPTION = "Retrieve anisotropic R-spectra"
REDUCED_R_SPECTRA_PG_DESCRIPTION = "Save reduced R-spectra"
WRITE_RGB_PG_DESCRIPTION = "Write RGB output image to '%s'"

# HDF5 variables
EIGEN_VECTOR_H5_DS_NAME = "eigen_vectors"
EXPLAINED_VARIANCE_RATIO_DS_NAME = "explained_variance_ratio"
LOADINGS_H5_DS_NAME = "loadings"
R_SPECTRA_H5_DS_NAME = "r-spectra"
REDUCED_R_SPECTRA_H5_DS_NAME = "r-spectra-reduced"
WINDOW_SIZE_ATTR_NAME = "window-size"
METHOD_ATTR_NAME = "method"
