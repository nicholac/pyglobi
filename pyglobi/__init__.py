# -*- coding: utf-8 -*-

#  PyGlobi

# TODO:

"""
PyGlobi Library
~~~~~~~~~~~~~~~~~~~~~
Python API for the Global Biotic Interactions (GloBI) dataset.
Basic usage:
   >>> import pyglobi
   >>> ...
"""

import warnings

from .__version__ import __title__, __description__, __url__, __version__
from .__version__ import __build__, __author__, __author_email__, __license__
from .__version__ import __copyright__

from . import config
from . import utils
from .models import *
from .api import *
from .sessions import *
from .status_codes import *
from .exceptions import *

# Set default logging handler to avoid "No handler found" warnings.
import logging
from logging import NullHandler

logging.getLogger(__name__).addHandler(NullHandler())
