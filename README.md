# pyglobi

TODO: 

* Implement tests for the simple endpoints - DONE
* 
* Implement doc building
* Check building (Done), packaging, testing, docs
* Continue to implement everything rglobi has

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














