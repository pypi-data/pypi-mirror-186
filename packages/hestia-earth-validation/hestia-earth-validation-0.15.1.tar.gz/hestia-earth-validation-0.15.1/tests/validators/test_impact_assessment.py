import json

from tests.utils import fixtures_path
from hestia_earth.validation.utils import _group_nodes
from hestia_earth.validation.validators.impact_assessment import (
    validate_impact_assessment, validate_linked_cycle_product, validate_single_linked_impact_assessment
)


def test_validate_valid():
    with open(f"{fixtures_path}/impactAssessment/valid.json") as f:
        node = json.load(f)
    assert validate_impact_assessment(node) == [True] * 19


def test_validate_linked_cycle_product_valid():
    with open(f"{fixtures_path}/impactAssessment/cycle-contains-product/valid.json") as f:
        data = json.load(f)
    assert validate_linked_cycle_product(data, data.get('cycle')) is True


def test_validate_linked_cycle_product_invalid():
    with open(f"{fixtures_path}/impactAssessment/cycle-contains-product/invalid.json") as f:
        data = json.load(f)
    assert validate_linked_cycle_product(data, data.get('cycle')) == {
        'level': 'error',
        'dataPath': '.product',
        'message': 'should be included in the cycle products',
        'params': {
            'product': {
                '@type': 'Term',
                '@id': 'maizeGrain'
            },
            'node': {
                'type': 'Cycle',
                'id': 'fake-cycle'
            }
        }
    }


def test_validate_single_linked_impact_assessment_valid():
    with open(f"{fixtures_path}/impactAssessment/product-single-ia/cycle.json") as f:
        cycle = json.load(f)
    with open(f"{fixtures_path}/impactAssessment/product-single-ia/valid.json") as f:
        nodes = json.load(f).get('nodes')
    assert validate_single_linked_impact_assessment(nodes[0], _group_nodes(nodes), cycle) is True


def test_validate_single_linked_impact_assessment_invalid():
    with open(f"{fixtures_path}/impactAssessment/product-single-ia/cycle.json") as f:
        cycle = json.load(f)
    with open(f"{fixtures_path}/impactAssessment/product-single-ia/invalid.json") as f:
        nodes = json.load(f).get('nodes')
    assert validate_single_linked_impact_assessment(nodes[0], _group_nodes(nodes), cycle) == {
        'level': 'error',
        'dataPath': '.product',
        'message': 'multiple ImpactAssessment are associated with the same Product of the same Cycle',
        'params': {
            'product': {
                '@type': 'Term',
                '@id': 'maizeGrain'
            },
            'node': {
                'type': 'Cycle',
                'id': 'fake-cycle'
            }
        }
    }
