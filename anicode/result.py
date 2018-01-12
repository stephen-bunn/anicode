# Copyright (c) 2018 Stephen Bunn (stephen@bunn.io)
# MIT License <https://opensource.org/licenses/MIT>


class AnicodeResult(object):

    def __init__(self, name, code):
        (self.name, self.code,) = (name, code,)

    def __repr__(self):
        return (
            '<{self.__class__.__name__} {self.char}  "{self.name}">'
        ).format(**locals())

    @property
    def char(self):
        if not hasattr(self, '_char'):
            self._char = chr(self.code)
        return self._char
