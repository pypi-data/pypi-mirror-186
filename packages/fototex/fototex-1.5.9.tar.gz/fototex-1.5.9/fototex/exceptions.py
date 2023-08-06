# -*- coding: utf-8 -*-

""" Module summary description.

More detailed description.
"""


class FotoBaseError(Exception):
    pass


class FotoError(FotoBaseError):
    pass


class FotoBatchError(FotoError):
    pass


class FotoSectorBatchError(FotoBaseError):
    pass


class H5FileError(Exception):
    pass


class H5FileAppendError(H5FileError):
    pass


class ImportSklearnWarning(Warning):
    pass
