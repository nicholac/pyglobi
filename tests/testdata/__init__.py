"""
Test Cypher Queries and data
"""


basic_query = "CYPHER 1.9 START taxon = \
    node:taxons(name=\"Syacium papillosum\") MATCH \
    taxon<-[x:CLASSIFIED_AS]-predatorSpecimen-[:ATE]->preySpecimen-[:CLASSIFIED_AS]->preyTaxon \
    where has(preyTaxon.externalId) and has(taxon.externalId) \
    RETURN distinct preyTaxon.externalId as preyTaxonId, \
    taxon.externalId as predatorTaxonId LIMIT 10"

neo_interaction = {
    "extensions": {},
    "metadata": {
        "id": 53825449,
        "type": "VISITED_BY"
    },
    "data": {
        "iri": "http://purl.obolibrary.org/obo/RO_0002619",
        "count": 1,
        "label": "visitedBy",
        "inverted": "true"
    },
    "start": "https://neo4j.globalbioticinteractions.org/db/data/node/19018317",
    "property": "https://neo4j.globalbioticinteractions.org/db/data/relationship/53825449/properties/{key}",
    "self": "https://neo4j.globalbioticinteractions.org/db/data/relationship/53825449",
    "end": "https://neo4j.globalbioticinteractions.org/db/data/node/19018317",
    "type": "VISITED_BY",
    "properties": "https://neo4j.globalbioticinteractions.org/db/data/relationship/53825449/properties"
}


neo_taxon = {
    "metadata": {
    "id": 19018317,
    "labels": []
    },
    "data": {
        "pathIds": "ITIS:202422 | ITIS:954898 | ITIS:846494 | ITIS:954900 | ITIS:846496 | ITIS:846504 | ITIS:18063 | ITIS:846548 | ITIS:822428 | ITIS:28031 | ITIS:28260 | ITIS:28275",
        "externalUrl": "http://eol.org/pages/1147167",
        "kingdomName": "Plantae",
        "pathNames": "kingdom | subkingdom | infrakingdom | superphylum | phylum | subphylum | class | superorder | order | family | genus | species",
        "orderId": "ITIS:822428",
        "phylumName": "Tracheophyta",
        "externalIds": "Plantae | Viridiplantae | Streptophyta | Embryophyta | Tracheophyta | Spermatophytina | Magnoliopsida | Rosanae | Malpighiales | Euphorbiaceae | Croton | Croton glandulosus | ITIS:202422 | ITIS:954898 | ITIS:846494 | ITIS:954900 | ITIS:846496 | ITIS:846504 | ITIS:18063 | ITIS:846548 | ITIS:822428 | ITIS:28031 | ITIS:28260 | ITIS:28275 | GBIF:6 | GBIF:7707728 | GBIF:220 | GBIF:1414 | GBIF:4691 | GBIF:3057454 | GBIF:3058185 | GBIF:7965011 | | Croton glandulosus | WD:Q519802 | WD:Q3004373 | | Eukaryota | Streptophytina | Euphyllophyta | Spermatophyta | Magnoliophyta | Mesangiospermae | Gunneridae | Pentapetalae | Crotonoideae | Crotoneae | NCBI:131567 | NCBI:2759 | NCBI:33090 | NCBI:35493 | NCBI:131221 | NCBI:3193 | NCBI:58023 | NCBI:78536 | NCBI:58024 | NCBI:3398 | NCBI:1437183 | NCBI:71240 | NCBI:91827 | NCBI:1437201 | NCBI:71275 | NCBI:91835 | NCBI:3646 | NCBI:3977 | NCBI:235631 | NCBI:235891 | NCBI:100370 | NCBI:323052 | |  | Eukaryota | Archaeplastida | Chloroplastida | OTT:805080 | OTT:93302 | OTT:304358 | OTT:5268475 | OTT:361838 | OTT:916750 | OTT:5342313 | OTT:10210 | OTT:1007992 | OTT:10218 | OTT:99252 | OTT:5298374 | OTT:431495 | OTT:853757 | OTT:5316182 | OTT:1008296 | OTT:565281 | OTT:429482 | OTT:914245 | OTT:719244 | OTT:520959 | OTT:929953 | OTT:276574 | IRMNG:15 | IRMNG:221 | IRMNG:1102 | IRMNG:10112 | IRMNG:114198 | IRMNG:1068334 | IRMNG:11296636 | INAT_TAXON:128938",
        "genusId": "ITIS:28260",
        "externalId": "ITIS:28275",
        "className": "Magnoliopsida",
        "speciesId": "ITIS:28275",
        "nameIds": "ITIS:28275 | OTT:276574 | GBIF:3058185 | GBIF:7965011 | WD:Q3004373 | NCBI:323052 | INAT_TAXON:128938 | IRMNG:11296636",
        "familyId": "ITIS:28031",
        "phylumId": "ITIS:846496",
        "path": "Plantae | Viridiplantae | Streptophyta | Embryophyta | Tracheophyta | Spermatophytina | Magnoliopsida | Rosanae | Malpighiales | Euphorbiaceae | Croton | Croton glandulosus",
        "classId": "ITIS:18063",
        "speciesName": "Croton glandulosus",
        "genusName": "Croton",
        "familyName": "Euphorbiaceae",
        "name": "Croton glandulosus",
        "rank": "species",
        "kingdomId": "ITIS:202422",
        "thumbnailUrl": "",
        "orderName": "Malpighiales"
    },
    "paged_traverse": "https://neo4j.globalbioticinteractions.org/db/data/node/19018317/paged/traverse/{returnType}{?pageSize,leaseTime}",
    "outgoing_relationships": "https://neo4j.globalbioticinteractions.org/db/data/node/19018317/relationships/out",
    "outgoing_typed_relationships": "https://neo4j.globalbioticinteractions.org/db/data/node/19018317/relationships/out/{-list|&|types}",
    "create_relationship": "https://neo4j.globalbioticinteractions.org/db/data/node/19018317/relationships",
    "labels": "https://neo4j.globalbioticinteractions.org/db/data/node/19018317/labels",
    "traverse": "https://neo4j.globalbioticinteractions.org/db/data/node/19018317/traverse/{returnType}",
    "extensions": {},
    "all_relationships": "https://neo4j.globalbioticinteractions.org/db/data/node/19018317/relationships/all",
    "all_typed_relationships": "https://neo4j.globalbioticinteractions.org/db/data/node/19018317/relationships/all/{-list|&|types}",
    "property": "https://neo4j.globalbioticinteractions.org/db/data/node/19018317/properties/{key}",
    "self": "https://neo4j.globalbioticinteractions.org/db/data/node/19018317",
    "incoming_relationships": "https://neo4j.globalbioticinteractions.org/db/data/node/19018317/relationships/in",
    "properties": "https://neo4j.globalbioticinteractions.org/db/data/node/19018317/properties",
    "incoming_typed_relationships": "https://neo4j.globalbioticinteractions.org/db/data/node/19018317/relationships/in/{-list|&|types}"
}