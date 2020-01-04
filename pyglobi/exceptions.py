# -*- coding: utf-8 -*-

"""
pyglobi.exceptions
~~~~~~~~~~~~
Exceptions used by pyglobi
:copyright: (c) 2019 by Chris Nicholas.
:license: MIT, see LICENSE for more details.
"""

class PyGlobiException(IOError):
    """There was an ambiguous exception that occurred.
    """

    def __init__(self, *args, **kwargs):
        """Initialize PyGlobiException"""
        super(PyGlobiException, self).__init__(*args, **kwargs)


class EoLIDNotFound(PyGlobiException):
    """EoL ID not fgound - no data associated with the requested EoL ID"""

class HTTPError(PyGlobiException):
    """An HTTP error occurred."""