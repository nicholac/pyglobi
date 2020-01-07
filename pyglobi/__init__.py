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
import os
import json
import warnings

from .__version__ import __title__, __description__, __url__, __version__
from .__version__ import __build__, __author__, __author_email__, __license__
from .__version__ import __copyright__

from .models import *

#Module Level Data
TEST = 10
#Instantiate the interal interactions
interactions = {}
#TODO: Load from local user directory cache
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', "interactions.json"), "r") as fptr:
   data = json.load(fptr)
   for _name, _values in data.items():
      interactions[_name] = Interaction(
         name=_name, 
         source=_values.get("source"),
         target=_values.get("target"), 
         term_iri=_values.get("termIRI"),
         neo_type=_values.get("neo_type")
      )

from . import config
from . import utils
from .models import *
from .api import *
from .sessions import *
from .status_codes import *
from .exceptions import *
from .queries import *

# Set default logging handler to avoid "No handler found" warnings.
import logging
from logging import NullHandler

logging.getLogger(__name__).addHandler(NullHandler())
