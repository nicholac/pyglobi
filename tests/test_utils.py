# -*- encoding: utf-8

import sys

import pytest

from pyglobi import utils

def test_internet():
    """Verify we are connected to the internet"""
    assert(utils.check_internet_connectivity() == True)

def test_interaction_types_to_neo_query():
    __types = utils.interaction_types_to_neo_query()
    assert __types == "ATE|EATEN_BY|PREYS_ON|PREYED_UPON_BY|KILLS|KILLED_BY|PARASITE_OF|HAS_PARASITE|HOST_OF|HAS_HOST|POLLINATES|POLLINATED_BY|PATHOGEN_OF|HAS_PATHOGEN|FLOWERS_VISITED_BY|VISITS_FLOWERS_OF|RELATED_TO|CO_OCCURS_WITH|INTERACTS_WITH|VISITS|VISITED_BY"