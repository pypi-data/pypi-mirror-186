from hestia_earth.schema import NodeType
from hestia_earth.utils.model import find_term_match
from hestia_earth.utils.tools import flatten

from hestia_earth.validation.utils import _find_linked_node
from .shared import (
    validate_list_min_below_max, validate_region_in_country, validate_country, validate_is_region,
    validate_list_term_percent, validate_linked_source_privacy, validate_date_lt_today,
    validate_list_model, validate_private_has_source, validate_list_value_between_min_max
)
from .indicator import validate_characterisedIndicator_model, validate_landTransformation


def validate_linked_cycle_product(impact_assessment: dict, cycle: dict):
    product = impact_assessment.get('product', {})
    product_id = product.get('@id')
    has_product = find_term_match(cycle.get('products', []), product_id, None) is not None
    return has_product or {
        'level': 'error',
        'dataPath': '.product',
        'message': 'should be included in the cycle products',
        'params': {
            'product': product,
            'node': {
                'type': 'Cycle',
                'id': cycle.get('id', cycle.get('@id'))
            }
        }
    }


def _filter_same_cycle(cycle: dict):
    def filter(impact_assessment: dict):
        ia_cycle = impact_assessment.get('cycle', {})
        return any([
            ia_cycle.get('id') and ia_cycle.get('id') == cycle.get('id'),
            ia_cycle.get('@id') and ia_cycle.get('@id') == cycle.get('@id')
        ])
    return filter


def validate_single_linked_impact_assessment(impact_assessment: dict, node_map: dict, cycle: dict):
    product = impact_assessment.get('product', {})
    product_id = product.get('@id')
    uploaded_impact_assessments = node_map.get(NodeType.IMPACTASSESSMENT.value).values()
    related_impact_assessments = list(filter(_filter_same_cycle(cycle), uploaded_impact_assessments))
    same_product_id = list(filter(lambda v: v.get('product', {}).get('@id') == product_id, related_impact_assessments))
    return len(same_product_id) == 1 or {
        'level': 'error',
        'dataPath': '.product',
        'message': 'multiple ImpactAssessment are associated with the same Product of the same Cycle',
        'params': {
            'product': product,
            'node': {
                'type': 'Cycle',
                'id': cycle.get('id', cycle.get('@id'))
            }
        }
    }


def validate_impact_assessment(impact_assessment: dict, node_map: dict = {}):
    """
    Validates a single `ImpactAssessment`.

    Parameters
    ----------
    impact_assessment : dict
        The `ImpactAssessment` to validate.
    node_map : dict
        The list of all nodes to do cross-validation, grouped by `type` and `id`.

    Returns
    -------
    List
        The list of errors for the `ImpactAssessment`, which can be empty if no errors detected.
    """
    cycle = _find_linked_node(node_map, impact_assessment.get('cycle', {}))
    return [
        validate_date_lt_today(impact_assessment, 'startDate'),
        validate_date_lt_today(impact_assessment, 'endDate'),
        validate_linked_source_privacy(impact_assessment, 'source', node_map),
        validate_private_has_source(impact_assessment, 'source'),
        validate_country(impact_assessment) if 'country' in impact_assessment else True,
        validate_is_region(impact_assessment) if 'region' in impact_assessment else True,
        validate_region_in_country(impact_assessment) if 'region' in impact_assessment else True,
        validate_linked_cycle_product(impact_assessment, cycle) if cycle else True,
        validate_single_linked_impact_assessment(impact_assessment, node_map, cycle) if cycle else True
    ] + flatten(
        ([
            validate_list_min_below_max(impact_assessment, 'emissionsResourceUse'),
            validate_list_value_between_min_max(impact_assessment, 'emissionsResourceUse'),
            validate_list_term_percent(impact_assessment, 'emissionsResourceUse'),
            validate_characterisedIndicator_model(impact_assessment, 'emissionsResourceUse'),
            validate_landTransformation(impact_assessment, 'emissionsResourceUse')
        ] if len(impact_assessment.get('emissionsResourceUse', [])) > 0 else []) +
        ([
            validate_list_min_below_max(impact_assessment, 'impacts'),
            validate_list_value_between_min_max(impact_assessment, 'impacts'),
            validate_list_term_percent(impact_assessment, 'impacts'),
            validate_list_model(impact_assessment, 'impacts'),
            validate_characterisedIndicator_model(impact_assessment, 'impacts')
        ] if len(impact_assessment.get('impacts', [])) > 0 else []) +
        ([
            validate_list_min_below_max(impact_assessment, 'endpoints'),
            validate_list_value_between_min_max(impact_assessment, 'endpoints'),
            validate_list_term_percent(impact_assessment, 'endpoints')
        ] if len(impact_assessment.get('endpoints', [])) > 0 else [])
    )
