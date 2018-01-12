# Copyright (c) 2018 Stephen Bunn (stephen@bunn.io)
# MIT License <https://opensource.org/licenses/MIT>

import contextlib

from anicode.anicode import (Anicode,)

import pytest


@contextlib.contextmanager
def anicode_manager(*args, **kwargs):
    """ A context manager for test objects.
    """

    manager = Anicode(*args, **kwargs)
    try:
        yield manager
    finally:
        del manager


class TestAnicode(object):
    """ Base test object.
    """

    def test_initialization(self):
        """ Base initialization test case.
        """

        with anicode_manager() as test_anicode:
            assert isinstance(test_anicode, Anicode)
            # TODO: test initialization
