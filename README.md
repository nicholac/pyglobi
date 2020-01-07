# pyglobi

TODO: 

* NEXT: queries.py - interactions by taxa the query is good, but gateway is timing out, 
    so I really need a local Neo instance to develop against...
* Then connect up queries.py to API for interactions_by_taxa
* Should I be doing all this in NetworkX? - How big would this be?
* Also its a very old version of Neo - should I upgrade this?

* Cypher is working - NEXT: Data IO from Cypher results (Dict, Pandas, networkX as MVP)
* Make wrapped Cypher queries (as per rglobi)
* Offline queries - by pulling and importing the various tar.gz implementations to some local cache
* Implement doc building
* Check building (Done), packaging (done - not tested publish), testing (doing), docs
* Continue to implement everything rglobi has
* Local Neo4J (with Dockerfiles etc to make spinning it up easy)

API:

Copy These:

https://docs.ropensci.org/rglobi/reference/

get_child_taxa
get_data_fields
get_interaction_areas
get_interaction_matrix
get_interaction_table
get_interaction_types
get_interactions
get_interactions_by_taxa
get_interactions_by_type
get_interactions_in_area
get_predators_of
get_prey_of
query

### Hints:

Neo Browser: https://neo4j.globalbioticinteractions.org/browser/

Main Globi Help for Cypher: https://github.com/globalbioticinteractions/globalbioticinteractions/wiki/Cypher#find-mammals-eaten-by-homo-sapiens-in-coastal-areas


More Geo Globi info: https://github.com/globalbioticinteractions/globalbioticinteractions/issues/19

Rglobi: https://github.com/ropensci/rglobi

Typing: https://docs.python.org/3/library/typing.html

Globi: https://www.globalbioticinteractions.org/data.html

EoL: https://eol.org/pages/1174377

Google Sphinx Style Docstrings: https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html


### Building

python setup.py build

pip install .


### Testing

python -m pytest tests/

Notes:

interactions.json has been sourced from the api, with the addition of the two missing relationship types (visits and vistedBy) - which occur in the Cypher interface