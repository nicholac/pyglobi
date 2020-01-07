# -*- coding: utf-8 -*-

"""
pyglobi.utils
~~~~~~~~~~~~
Utility methods for URL's used by pyglobi
:copyright: (c) 2019 by Chris Nicholas.
:license: MIT, see LICENSE for more details.
"""
import os
from urllib.request import urlopen
from urllib.error import URLError

from .config import (
    globi_neo_url,
    eol_url,
    eol_geo_url
)

from pyglobi import interactions as internal_interactions

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

def check_internet_connectivity(tries=5) -> bool:
    """Check for an internet connection (required for the API)
    Kwargs:
        tries: Number of tries before giving up
    
    Returns:
        True if internet else False
    """
    internet = False
    for _ in range(tries):
        try: 
            urlopen("http://www.google.com")
            internet = True
        except URLError:
            pass
    return internet

#TODO: Put this somewhere else
def interaction_types_to_neo_query(interactions: list=[]):
    """
    Convert the given interactions to a string suitable for the Neo Rels query
    Args:
        interactions: list[Interaction, ...] List of Interactions to convert
    """
    if len(interactions) == 0:
        __types =  [interaction.neo_type for _, interaction in internal_interactions.items() if interaction.neo_type != ""]
        return "|".join(__types)