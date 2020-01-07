# -*- encoding: utf-8

import sys

import pytest

import pyglobi

from testdata import (
    basic_query
)

def test_cypher_query():
    """Verify we can run a basic Cypher Query"""
    res = pyglobi.cypher(basic_query)
    assert(res)

def test_cypher_query_altered_neo_uri():
    """Verify change the neo endpoint and it fails"""
    pyglobi.config.globi_neo_url = "https://null"
    assert(pyglobi.config.globi_neo_url == "https://null")
    with pytest.raises(pyglobi.exceptions.GlobiCypherError):
        _ = pyglobi.cypher(basic_query)
