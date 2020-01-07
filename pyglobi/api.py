# -*- coding: utf-8 -*-

"""
pyglobi.api
~~~~~~~~~~~~
This module implements the Main PyGlobi API.
:copyright: (c) 2019 by Chris Nicholas.
:license: MIT, see LICENSE for more details.
"""

from . import sessions
from . import config
from pyglobi import TEST
from pyglobi import interactions
from .exceptions import UnknownInteractionType

def check_config():
    return config.globi_neo_url

def cypher(cypher: str, **kwargs) -> bool:
    """Constructs, sends and returns results of a cypher request to Globi 

    Args:
        cypher: Cypher string query.

    Returns:
        TODO: Data parsing options with this setting 
        Neo4j JSON

    """
    with sessions.CypherSession(globi_neo_url=config.globi_neo_url) as session:
        return session.query(cypher)


def interactions_by_taxa(source_taxon: str, target_taxon: str="", 
    interaction_type: str="", bbox: list=None):
    """Constructs, sends and returns results of a cypher request to Globi 

    Args:
        source_taxon: Source Taxon (name of EOL ID)
    
    Kwargs:
        target_taxon: Filter interactions to a specific target 
            Name or EOLID
        interation_type: Name of interaction.  See :pyglobi.interactions
        TODO: BBOX
        bbox: Filter interactions to the given bounding box

    Returns:
        result: JSON TODO: Data IO
    """
    if interaction_type != "":
        try:
            interaction = interactions[interaction_type]
        except KeyError:
            raise UnknownInteractionType()

    cypher = 
    



def geodata(eol_id: int, **kwargs) -> dict:
    """Constructs, sends and returns results of a EoL geodata request to Globi 

    Args:
        eol_id: EoL identifier string query.

    Returns:
        GeoJson for success, raises exception otherwise

    """
    with sessions.GeoDataSession(eol_id) as session:
        return session.run_cypher()