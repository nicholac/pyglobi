# -*- coding: utf-8 -*-

"""
pyglobi.models
~~~~~~~~~~~~
Data models used by pyglobi
:copyright: (c) 2019 by Chris Nicholas.
:license: MIT, see LICENSE for more details.
"""

class Interaction(object):
    """Interaction Class
    
    Attributes:
        name: str
        source: str
        target: str
        term_iri: str
        neo_type: str
    """
    
    def __init__(self, name=None, source=None, target=None, term_iri=None, neo_type=None):
        self.name = name
        self.source = source
        self.target = target
        self.term_iri = term_iri
        self.neo_type = neo_type

    def from_neo(self, neo_interaction_json: dict):
        """Instantiate using Neo4J schema json data, e.g.:
            {
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

        Args:
            neo_interaction_json: Dictionary of neo4j Interaction
        """
        self.name = neo_interaction_json.get("data").get("label")
        self.source = None
        self.target = None
        self.term_iri = neo_interaction_json.get("data").get("iri")
        self.neo_type = neo_interaction_json.get("type")

class Taxon(object):
    """Taxon Class

    Attributes:
        name: str 
        path_ids: str 
        external_url: str 
        kingdom_name: str 
        path_names: str 
        order_id: str 
        phylum_name: str 
        external_ids: str 
        genus_id: str 
        external_id: str 
        class_name: str 
        species_id: str 
        name_ids: str 
        family_id: str 
        phylum_id: str 
        path: str 
        class_id: str 
        species_name: str 
        genus_name: str 
        family_name: str 
        rank: str 
        kingdom_id: str 
        thumbnail_url: str 
        order_name: str 
    """
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.path_ids = kwargs.get("path_ids")
        self.external_url = kwargs.get("external_url")
        self.kingdom_name = kwargs.get("kingdom_name")
        self.path_names = kwargs.get("path_names")
        self.order_id = kwargs.get("order_id")
        self.phylum_name = kwargs.get("phylum_name")
        self.external_ids = kwargs.get("external_ids")
        self.genus_id = kwargs.get("genus_id")
        self.external_id = kwargs.get("external_id")
        self.class_name = kwargs.get("class_name")
        self.species_id = kwargs.get("species_id")
        self.name_ids = kwargs.get("name_ids")
        self.family_id = kwargs.get("family_id")
        self.phylum_id = kwargs.get("phylum_id")
        self.path = kwargs.get("path")
        self.class_id = kwargs.get("class_id")
        self.species_name = kwargs.get("species_name")
        self.genus_name = kwargs.get("genus_name")
        self.family_name = kwargs.get("family_name")
        self.rank = kwargs.get("rank")
        self.kingdom_id = kwargs.get("kingdom_id")
        self.thumbnail_url = kwargs.get("thumbnail_url")
        self.order_name = kwargs.get("order_name")

    def from_neo(self, neo_taxon_json: dict):
        """Instantiate using Neo4J schema json data

        Args:
            neo_taxon_json: Dictionary of neo4j Taxon, e.g.:
                {
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
        """
        self.name = neo_taxon_json.get("data").get("name")
        self.path_ids = neo_taxon_json.get("data").get("pathIds")
        self.external_url = neo_taxon_json.get("data").get("externalUrl")
        self.kingdom_name = neo_taxon_json.get("data").get("kingdomName")
        self.path_names = neo_taxon_json.get("data").get("pathNames")
        self.order_id = neo_taxon_json.get("data").get("orderId")
        self.phylum_name = neo_taxon_json.get("data").get("phylumName")
        self.external_ids = neo_taxon_json.get("data").get("externalIds")
        self.genus_id = neo_taxon_json.get("data").get("genusId")
        self.external_id = neo_taxon_json.get("data").get("externalId")
        self.class_name = neo_taxon_json.get("data").get("className")
        self.species_id = neo_taxon_json.get("data").get("speciesId")
        self.name_ids = neo_taxon_json.get("data").get("nameIds")
        self.family_id = neo_taxon_json.get("data").get("familyId")
        self.phylum_id = neo_taxon_json.get("data").get("phylumId")
        self.path = neo_taxon_json.get("data").get("path")
        self.class_id = neo_taxon_json.get("data").get("classId")
        self.species_name = neo_taxon_json.get("data").get("speciesName")
        self.genus_name = neo_taxon_json.get("data").get("genusName")
        self.family_name = neo_taxon_json.get("data").get("familyName")
        self.rank = neo_taxon_json.get("data").get("rank")
        self.kingdom_id = neo_taxon_json.get("data").get("kingdomId")
        self.thumbnail_url = neo_taxon_json.get("data").get("thumbnailUrl")
        self.order_name = neo_taxon_json.get("data").get("orderName")
