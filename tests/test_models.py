




# -*- encoding: utf-8

import sys

import pytest

import pyglobi

from testdata import (
    neo_interaction,
    neo_taxon
)

def test_interaction_from_neo() :
    t = pyglobi.models.Interaction()
    t.from_neo(neo_interaction)
    assert t.name == neo_interaction['data']['label']
    assert t.neo_type == neo_interaction['type']

def test_taxon_from_neo() :
    t = pyglobi.models.Taxon()
    t.from_neo(neo_taxon)
    assert t.genus_name == neo_taxon['data']['genusName']
    assert t.external_url == neo_taxon['data']['externalUrl']