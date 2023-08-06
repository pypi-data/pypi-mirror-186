from hestia_earth.schema import SchemaType, TermTermType
from hestia_earth.utils.api import find_node, search


def get_fuel_terms():
    """
    Find all "liquid" `fuel` terms from the Glossary:
    - https://hestia.earth/glossary?termType=fuel&query=gasoline
    - https://hestia.earth/glossary?termType=fuel&query=diesel

    Returns
    -------
    list
        List of matching term `@id` as `str`.
    """
    terms = search({
        "bool": {
            "must": [
                {
                    "match": {
                        "@type": SchemaType.TERM.value
                    }
                },
                {
                    "match": {
                        "termType.keyword": TermTermType.FUEL.value
                    }
                }
            ],
            "should": [
                {
                    "regexp": {
                        "name": "*gasoline*"
                    }
                },
                {
                    "regexp": {
                        "name": "*diesel*"
                    }
                }
            ],
            "minimum_should_match": 1
        }
    }, limit=100)
    return list(map(lambda n: n['@id'], terms))


def get_crop_residue_terms():
    terms = find_node(SchemaType.TERM, {'termType': TermTermType.CROPRESIDUE.value}, limit=1000)
    return [term.get('@id') for term in terms if term.get('@id')]


def get_methodModels():
    terms = find_node(SchemaType.TERM, {'termType': TermTermType.MODEL.value}, limit=1000)
    return [term.get('@id') for term in terms if term.get('@id')]
