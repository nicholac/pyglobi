# -*- encoding: utf-8

import sys

import pytest

import pyglobi
from pyglobi.models import Interaction

def test_system():
    """Verify we are loading everything correctly"""
    assert True == True

def test_interactions():
    """Test we've instantiated the local interactions successfully"""
    assert len(pyglobi.interactions) != 0
    for i in pyglobi.interactions.keys():
        assert isinstance(pyglobi.interactions[i], Interaction)
