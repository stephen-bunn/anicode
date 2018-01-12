# Copyright (c) 2018 Stephen Bunn (stephen@bunn.io)
# MIT License <https://opensource.org/licenses/MIT>

import os
import pathlib
import importlib.util


def normalize_path(filepath, expand_vars=False):
    """ Fully normalizes a given filepath to an absolute path.

    :param str filepath: The filepath to normalize
    :param bool expand_vars: Expands embedded environment variables if True
    :returns: The fully noralized filepath
    :rtype: str
    """

    filepath = str(pathlib.Path(filepath).expanduser().resolve())
    if expand_vars:
        filepath = os.path.expandvars(filepath)
    return filepath


def is_importable(name):
    """ Determines if a given package name can be found.

    :param str name: The name of the pacakge
    :returns: True if the package can be found
    :rtype: bool
    """

    return bool(importlib.util.find_spec(name))
