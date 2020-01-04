"""
Test Cypher Queries and data
"""


basic_query = "CYPHER 1.9 START taxon = \
    node:taxons(name=\"Syacium papillosum\") MATCH \
    taxon<-[x:CLASSIFIED_AS]-predatorSpecimen-[:ATE]->preySpecimen-[:CLASSIFIED_AS]->preyTaxon \
    where has(preyTaxon.externalId) and has(taxon.externalId) \
    RETURN distinct preyTaxon.externalId as preyTaxonId, \
    taxon.externalId as predatorTaxonId LIMIT 10"