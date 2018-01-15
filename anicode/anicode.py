# Copyright (c) 2018 Stephen Bunn (stephen@bunn.io)
# MIT License <https://opensource.org/licenses/MIT>

import inspect
import collections
import concurrent.futures

from . import (const, sources,)


class Anicode(object):
    """ The base Anicode client.
    """

    @property
    def sources(self):
        """ The dictionary of enabled sources.

        :getter: Returns the dictionary of enabled sources
        :setter: Does not allow setting
        :rtype: dict[str, BaseSource]
        """

        if not hasattr(self, '_sources'):
            self._sources = {}
            for (source_name, source_class,) in inspect.getmembers(
                sources,
                predicate=inspect.isclass
            ):
                self._sources[source_name] = source_class()
        return self._sources

    def _callback(self, source, result):
        """ The default client result callback.

        :param BaseSource source: The yeilding source object
        :param AnicodeResult result: The anicode result
        :returns: Does not return
        """

        if result.code not in self.results:
            self.results[result.code] = result

    def search(self, query, count=10):
        """ The default client search method.

        :param str query: The query string to search for
        :param int count: The number of results to yeild for each source
        """

        (self.results, futures,) = (collections.OrderedDict(), [],)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for (_, source,) in self.sources.items():
                futures.append(
                    executor.submit(
                        source.search, query, self._callback,
                        count=count
                    )
                )

        # wait for threads to stop
        for future in futures:
            future.result()

        return self.results
