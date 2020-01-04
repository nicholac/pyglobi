# -*- coding: utf-8 -*-

"""
pyglobi.sessions
~~~~~~~~~~~~
Sessions used by pyglobi
:copyright: (c) 2019 by Chris Nicholas.
:license: MIT, see LICENSE for more details.
"""
import sys

import requests

config = sys.modules['pyglobi'].config

from .utils import (
    construct_eol_url,
    construct_eol_geo_url
)

from .exceptions import (
    EoLIDNotFound,
    GlobiCypherError
)

class CypherSession(object):
    """A session covering a request either for Neo4j endpoints
    
    Args:


    Kwargs:
        globi_neo_url
    """

    def __init__(self, globi_neo_url=config.globi_neo_url):

        #: Globi Neo URL
        #: :class: `CypherSession <CypherSession>`.
        self.globi_neo_url = globi_neo_url

        #: Current Cypher Query
        #: :class: `CypherSession <CypherSession>`.
        self.cypher = None

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def close(self, **kwargs):
        """Closes all connections etc for the session"""
        return True

    def query(self, cypher: str, **kwargs) -> dict:
        """Run the Cypher Query associated with the session

        Args:
            cypher: The Cypher query string
            params: Cypher Query Parameteres

        Returns:
            results dict  
        """
        print (self.globi_neo_url)
        self.cypher = cypher
        try:
            resp = requests.post(self.globi_neo_url, json={"query": self.cypher})
        except requests.exceptions.ConnectionError as err:
            raise GlobiCypherError(
                0, 
                "Request Error - check url:{}".format(err.__traceback__), 
                self.cypher
            )
        if resp.status_code != 200:
            raise GlobiCypherError(resp.status_code, "Response Status code was not 200", self.cypher)
        result = resp.json()
        if not result:
            raise GlobiCypherError(resp.status_code, "Result missing JSON", self.cypher)
        return result


class GeoDataSession(object):
    """A session covering a request for EoL Geodata endpoint
    # TODO: Add Basic Usage
    """

    def __init__(self, eol_id):

        #: eol_id Associated with the request (if session involves use of eol_id) 
        #: :class:`Session <Session>`.
        self.eol_id = None

        #: Endpoint used with the session - set when the internal session method is invoked
        #: :class:`Session <Session>`.
        self.endpoint = None

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()
    
    def close(self, **kwargs):
        """Closes all connections etc for the session"""
        return True

    def get_eol_data(self, eol_id: int, **kwargs) -> dict:
        """Attempt to get the EoL geodata associated with the given taxa 

        #TODO: Additional output-types

        Args:
            eol_id: EoL identifier for the taxa

        Returns:
            Dictionary response (geo-json) is successful, else raises EOLIDNotFound() Exception
        """
        endpoint = construct_eol_geo_url(self.eol_id)
        self.eol_id = eol_id
        self.endpoint = endpoint
        print (self.endpoint)
        #TODO: Complete requests call, with EoLIDNotFound where not found
        return {}

    
