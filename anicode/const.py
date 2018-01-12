# Copyright (c) 2018 Stephen Bunn (stephen@bunn.io)
# MIT License <https://opensource.org/licenses/MIT>

import sys
import pathlib


class _const(object):
    """ Modules constant's namespace.
    """

    def __init__(self):
        """ Initializes module constants.
        """

        sys.excepthook = self.__exception_handler

    @property
    def base_dir(self):
        """ The base directory path of the module.

        :returns: The base directory path of the module
        :rtype: str
        """

        if not hasattr(self, '_base_dir'):
            self._base_dir = pathlib.Path(__file__).parent
        return self._base_dir

    @property
    def parent_dir(self):
        """ The parent directory path of the module.

        :returns: The parent directory path of the module
        :rtype: str
        """

        if not hasattr(self, '_parent_dir'):
            self._parent_dir = self.base_dir.parent
        return self._parent_dir

    def __exception_handler(self, exception_type, value, exception_traceback):
        """ A custom exception handler for logging to base loggers.

        :param Exception exception_type: The raised exception type
        :param str value: The message of the exception
        :param traceback exception_traceback: The traceback of the exception
        """

        sys.__excepthook__(exception_type, value, exception_traceback)


sys.modules[__name__] = _const()
