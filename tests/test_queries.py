# -*- encoding: utf-8

import sys

import pytest

import pyglobi

from testdata import neo_taxon

def test_interactions_by_taxa():
    source_taxon = pyglobi.models.Taxon()
    source_taxon.from_neo(neo_taxon)
    query = pyglobi.queries.__interactions_by_taxa(source_taxon)
    print (query)
    assert query == ""