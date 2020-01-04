# -*- encoding: utf-8

import sys

import pytest

from pyglobi import utils

def test_internet():
    """Verify we are connected to the internet"""
    assert(utils.check_internet_connectivity() == True)