# Copyright (c) 2018 Stephen Bunn (stephen@bunn.io)
# MIT License <https://opensource.org/licenses/MIT>

import abc

import furl


class BaseSource(abc.ABC):

    @abc.abstractmethod
    def search(self, query):
        raise NotImplementedError()
