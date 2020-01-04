# -*- coding: utf-8 -*-

"""
pyglobi.utils
~~~~~~~~~~~~
Utility methods for URL's used by pyglobi
:copyright: (c) 2019 by Chris Nicholas.
:license: MIT, see LICENSE for more details.
"""
import os

from .config import (
    globi_neo_url,
    eol_url,
    eol_geo_url
)

def construct_eol_url(eol_id: int, **kwargs) -> str:
    """Build an EoL URL page for the given taxonomy ID

    Args:
        eol_id: Encyclopedia of Life Taxa ID

    Returns:
        Endpoint URL for the Taxa page

    """
    return os.path.join(eol_url, str(eol_id))

def construct_eol_geo_url(eol_id: int, **kwargs) -> str:
    """Build an EoL Geo Data URL page for the given taxonomy ID

    Reverse engineered from the page source, e.g: https://eol.org/pages/1174377

    Args:
        eol_id: Encyclopedia of Life Taxa ID

    Returns:
        Endpoint URL for the geodata associated with the taxa
    
    """
    _folder = str(eol_id)[-2:]
    return os.path.join(eol_geo_url, _folder, str(eol_id)+'.json')

