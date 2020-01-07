# -*- encoding: utf-8

import sys

import pytest

import pyglobi

def test_interactions_by_taxa() :
    with pytest.raises(pyglobi.exceptions.UnknownInteractionType):
        pyglobi.api.interactions_by_taxa("", interaction_type="unknown")