# -*- coding: utf-8 -*-

"""
pyglobi.queries
~~~~~~~~~~~~
Cypher Queries used throughout.
:copyright: (c) 2019 by Chris Nicholas.
:license: MIT, see LICENSE for more details.
"""

from .models import Taxon, Interaction
from .utils import interaction_types_to_neo_query

def __interactions_by_taxa(source_taxon: Taxon, target_taxon: str="()", **kwargs):
    """
    Args:
        source_taxon: :class Taxon
    Kwargs:
        target_taxon: :class Taxon
        interaction_types: List [:class Interaction, :class Interaction...]
    """
    if not kwargs.get("study"):
        study = "study=node:studies('*:*')"
    source_taxon = "source=node:taxons(name=\"{source_taxon_name}\")".format(
        source_taxon_name = source_taxon.name
    )
    pre_vars = ','.join([study, source_taxon])
    if not kwargs.get("interactions_types"):
        interaction_types = interaction_types_to_neo_query()
    __q = "CYPHER 1.9 START {pre_vars} "\
          "MATCH study-[:COLLECTED]->source-[:CLASSIFIED_AS]->sourceTaxon, "\
          "source-[rel:{interaction_types}]->target-[:CLASSIFIED_AS]->targetTaxon "\
          "RETURN source, rel, targetTaxon".format(
              pre_vars=pre_vars,
              interaction_types=interaction_types
          )
    return __q