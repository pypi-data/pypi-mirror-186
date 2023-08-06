# -*- coding: utf-8 -*-

""" Module summary description.

More detailed description.
"""
import os
# from collections import Collection


def check_string(string, list_of_strings):
    """ Check validity of and return string against list of valid strings

    :param string: searched string
    :param list_of_strings: list/tuple/set of valid strings string is to be checked against
    :return: validate string from list of strings if match
    """
    # check_type(string, str, list_of_strings, Collection)
    [check_type(x, str) for x in list_of_strings]

    output_string = []

    for item in list_of_strings:
        if item.lower().startswith(string.lower()):
            output_string.append(item)

    if len(output_string) == 1:
        return output_string[0]
    elif len(output_string) == 0:
        raise ValueError("input must match one of those: {}".format(list_of_strings))
    elif len(output_string) > 1:
        raise ValueError("input match more than one valid value among {}".format(list_of_strings))


def check_type(*args):
    """Check type of arguments

    :param args: tuple list of argument/type
    :return:
    """
    if len(args) % 2 == 0:
        for item in range(0, len(args), 2):
            if not isinstance(args[item], args[item + 1]):
                raise TypeError("Type of argument {} is '{}' but must be '{}'".format(
                    item//2 + 1, type(args[item]).__name__, args[item + 1].__name__))


def check_type_in_collection(collection, _type, include=True):
    """ Check type of elements in collection

    Check type of elements in collection through including or
    excluding specific types.

    :param collection: list/tuple/set/ndarray/etc. collection of data
    :param _type: type or tuple list of types
    :param include: should collection include or exclude type ?
    :return: none
    """
    # check_type(collection, Collection, _type, (type, tuple), include, bool)
    if include is True and not all(isinstance(element, _type) for element in collection):
        raise TypeError("All elements in collection '{}' "
                        "must be {}".format(type(collection), _type))
    elif include is False and any(isinstance(element, _type) for element in collection):
        raise TypeError("Collection '{}' cannot contain {}".format(type(collection), _type))


def isdir(path):
    try:
        return os.path.isdir(path)
    except (TypeError, ValueError):
        return False


def lazyproperty(func):
    name = '_lazy_' + func.__name__

    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)
            return value
    return lazy
