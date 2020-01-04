# -*- coding: utf-8 -*-

"""
pyglobi.sessions
~~~~~~~~~~~~
Sessions used by pyglobi
:copyright: (c) 2019 by Chris Nicholas.
:license: MIT, see LICENSE for more details.
"""

import requests

from .config import (
    globi_neo_url
)

from .utils import (
    construct_eol_url,
    construct_eol_geo_url
)

from .exceptions import (
    EoLIDNotFound
)

class CypherSession(object):
    """A session covering a request either for Neo4j endpoints
    # TODO: Add Basic Usage
    """

    def __init__(self, cypher):
        
        #: Cypher Query Text (if session associated with Cypher Query)
        #: :class:`Session <Session>`.
        self.cypher = cypher

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

    def run(self, **kwargs):
        """Run the Cypher Query associated with the session
        """
        return True


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

    
