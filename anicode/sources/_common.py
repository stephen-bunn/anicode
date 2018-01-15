# Copyright (c) 2018 Stephen Bunn (stephen@bunn.io)
# MIT License <https://opensource.org/licenses/MIT>

import abc


class BaseSource(abc.ABC):
    """ The base source abstract class.
    """

    @abc.abstractmethod
    def search(self, query, callback, count=10):
        """ Sends query results over a callback.

        .. note:: The callback should accept the following positional
            parameters:

            * The query source object
            * The AnicodeResult object

        :param str query: The search term to use
        :param callable callback: The callback function
        :param int count: The number of results to send to the callback
        :returns: Does not return
        """

        raise NotImplementedError()
