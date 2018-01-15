# Copyright (c) 2018 Stephen Bunn (stephen@bunn.io)
# MIT License <https://opensource.org/licenses/MIT>


class AnicodeResult(object):
    """ The anicode result object.
    """

    def __init__(self, name, code):
        """ Initializes the anicode result object.

        :param str name: The name of the unicode character
        :param int code: The unicode index
        """

        (self.name, self.code,) = (name, code,)

    def __repr__(self):
        """ Returns a readable representation of the object.

        :returns: A readable representation of the object
        :rtype: str
        """

        return (
            '<{self.__class__.__name__} {self.char}  "{self.name}">'
        ).format(**locals())

    @property
    def char(self):
        """ The copyable character of the result.

        :getter: Returns the copyable character of the result
        :setter: Does not allow setting
        :rtype: str
        """

        if not hasattr(self, '_char'):
            self._char = chr(self.code)
        return self._char
