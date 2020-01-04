# -*- coding: utf-8 -*-

"""
pyglobi.api
~~~~~~~~~~~~
This module implements the Main PyGlobi API.
:copyright: (c) 2019 by Chris Nicholas.
:license: MIT, see LICENSE for more details.
"""

from . import sessions

def cypher(cypher: str, **kwargs) -> bool:
    """Constructs, sends and returns results of a cypher request to Globi 

    Args:
        cypher: Cypher string query.
        url: The second parameter.

    Returns:
        The return value. True for success, False otherwise.

    """
    with sessions.CypherSession(cypher=cypher) as session:
        return session.run_cypher()

def geodata(eol_id: int, **kwargs) -> dict:
    """Constructs, sends and returns results of a EoL geodata request to Globi 

    Args:
        eol_id: EoL identifier string query.

    Returns:
        GeoJson for success, raises exception otherwise

    """
    with sessions.GeoDataSession(eol_id) as session:
        return session.run_cypher()