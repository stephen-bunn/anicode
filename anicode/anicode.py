# Copyright (c) 2018 Stephen Bunn (stephen@bunn.io)
# MIT License <https://opensource.org/licenses/MIT>

import inspect
import collections
import concurrent.futures

from . import (const, sources,)


class Anicode(object):

    def __init__(self):
        self.results = collections.OrderedDict()

    @property
    def sources(self):
        if not hasattr(self, '_sources'):
            self._sources = {}
            for (source_name, source_class,) in inspect.getmembers(
                sources,
                predicate=inspect.isclass
            ):
                self._sources[source_name] = source_class()
        return self._sources

    def _callback(self, source, result):
        if result.code not in self.results:
            self.results[result.code] = result

    def search(self, query, count=10):
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
