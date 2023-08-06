from hestia_earth.schema import TermTermType, CycleFunctionalUnit
from hestia_earth.utils.model import find_primary_product
from hestia_earth.utils.lookup import get_table_value, download_lookup, column_name
from hestia_earth.utils.tools import list_sum, flatten, non_empty_list
from hestia_earth.distribution.posterior_yield import get_post
from hestia_earth.distribution.prior_yield import get_prior

from hestia_earth.validation.log import logger
from hestia_earth.validation.utils import _list_sum, _filter_list_errors


def validate_economicValueShare(products: list):
    sum = _list_sum(products, 'economicValueShare')
    return sum <= 100.5 or {
        'level': 'error',
        'dataPath': '.products',
        'message': 'economicValueShare should sum to 100 or less across all products',
        'params': {
            'sum': sum
        }
    }


def validate_value_empty(products: list):
    def validate(values: tuple):
        index, product = values
        return len(product.get('value', [])) > 0 or {
            'level': 'warning',
            'dataPath': f".products[{index}]",
            'message': 'may not be 0'
        }

    return _filter_list_errors(map(validate, enumerate(products)))


def validate_value_0(products: list):
    def validate(values: tuple):
        index, product = values
        value = list_sum(product.get('value', [-1]), -1)
        eva = product.get('economicValueShare', 0)
        revenue = product.get('revenue', 0)
        return value != 0 or _filter_list_errors([
            eva == 0 or {
                'level': 'error',
                'dataPath': f".products[{index}].value",
                'message': 'economicValueShare must be 0 for product value 0',
                'params': {
                    'value': eva,
                    'term': product.get('term')
                }
            },
            revenue == 0 or {
                'level': 'error',
                'dataPath': f".products[{index}].value",
                'message': 'revenue must be 0 for product value 0',
                'params': {
                    'value': revenue,
                    'term': product.get('term')
                }
            }
        ])

    return _filter_list_errors(flatten(map(validate, enumerate(products))))


MAX_PRIMARY_PRODUCTS = 1


def validate_primary(products: list):
    primary = list(filter(lambda p: p.get('primary', False), products))
    return len(primary) <= MAX_PRIMARY_PRODUCTS or {
        'level': 'error',
        'dataPath': '.products',
        'message': f"only {MAX_PRIMARY_PRODUCTS} primary product allowed"
    }


def _get_excreta_term(lookup, product_id: str, column: str):
    value = get_table_value(lookup, 'termid', product_id, column_name(column))
    return non_empty_list((value or '').split(';'))


UNITS_TO_EXCRETA_LOOKUP = {
    'kg': ['allowedExcretaKgMassTermIds', 'recommendedExcretaKgMassTermIds'],
    'kg N': ['allowedExcretaKgNTermIds', 'recommendedExcretaKgNTermIds'],
    'kg VS': ['allowedExcretaKgVsTermIds', 'recommendedExcretaKgVsTermIds']
}


def validate_excreta(cycle: dict, list_key: str = 'products'):
    primary_product = find_primary_product(cycle) or {}
    product_term_id = primary_product.get('term', {}).get('@id')
    lookup = download_lookup(f"{primary_product.get('term', {}).get('termType')}.csv")

    def validate(values: tuple):
        index, product = values
        term_id = product.get('term', {}).get('@id')
        term_type = product.get('term', {}).get('termType')
        term_units = product.get('term', {}).get('units')
        allowed_column, recommended_column = UNITS_TO_EXCRETA_LOOKUP.get(term_units, [None, None])
        allowed_ids = _get_excreta_term(lookup, product_term_id, allowed_column)
        recommended_ids = _get_excreta_term(lookup, product_term_id, recommended_column)
        return term_type != TermTermType.EXCRETA.value or (
            len(allowed_ids) != 0 and term_id not in allowed_ids and {
                'level': 'error',
                'dataPath': f".{list_key}[{index}].term.@id",
                'message': 'is too generic',
                'params': {
                    'product': primary_product.get('term'),
                    'term': product.get('term', {}),
                    'current': term_id,
                    'expected': allowed_ids
                }
            }
        ) or (
            len(recommended_ids) != 0 and term_id not in recommended_ids and {
                'level': 'warning',
                'dataPath': f".{list_key}[{index}].term.@id",
                'message': 'is too generic',
                'params': {
                    'product': primary_product.get('term'),
                    'term': product.get('term', {}),
                    'current': term_id,
                    'expected': recommended_ids
                }
            }
        ) or True

    return _filter_list_errors(map(validate, enumerate(cycle.get(list_key, []))))


def validate_product_ha_functional_unit_ha(cycle: dict, list_key: str = 'products'):
    functional_unit = cycle.get('functionalUnit', CycleFunctionalUnit.RELATIVE.value)

    def validate(values: tuple):
        index, product = values
        term_units = product.get('term', {}).get('units')
        value = list_sum(product.get('value', [0]))
        return term_units != 'ha' or value <= 1 or {
            'level': 'error',
            'dataPath': f".{list_key}[{index}].value",
            'message': 'must be below or equal to 1 for unit in ha',
            'params': {
                'term': product.get('term', {})
            }
        }

    return functional_unit != CycleFunctionalUnit._1_HA.value or \
        _filter_list_errors(map(validate, enumerate(cycle.get(list_key, []))))


DEFAULT_THRESHOLD = 0.95
DEFAULT_ZSCORE = 1.96
CI_TO_ZSCORE = {
    0.9: 1.65,
    DEFAULT_THRESHOLD: DEFAULT_ZSCORE,
    0.99: 2.58
}


def _get_mu_sd(country_id: str, product_id: str):
    mu, sd = get_post(country_id, product_id)
    return (mu, sd) if mu is not None else get_prior(country_id, product_id)


def _validate_yield(country_id: str, product_id: str, yields: list[float], threshold: float = DEFAULT_THRESHOLD):
    z = CI_TO_ZSCORE[threshold]
    mu, sd = _get_mu_sd(country_id, product_id)
    min = mu-(z*sd) if mu is not None else None
    max = mu+(z*sd) if mu is not None else None
    passes = [min <= y <= max if mu is not None else True for y in yields]
    outliers = [y for y in yields if not min <= y <= max] if mu is not None else []
    return all(passes), outliers, min, max


def validate_product_yield(cycle: dict, site: dict, list_key: str = 'products', threshold: float = DEFAULT_THRESHOLD):
    country_id = site.get('country', {}).get('@id')

    def validate(values: tuple):
        index, product = values

        product_id = product.get('term', {}).get('@id')
        product_value = product.get('value', [])

        valid, outliers, min, max = _validate_yield(country_id, product_id, product_value, threshold)
        return valid or {
            'level': 'warning',
            'dataPath': f".{list_key}[{index}].value",
            'message': 'is outside confidence interval',
            'params': {
                'term': product.get('term', {}),
                'country': site.get('country', {}),
                'outliers': outliers,
                'threshold': threshold,
                'min': min,
                'max': max
            }
        }

    try:
        return _filter_list_errors(map(validate, enumerate(cycle.get(list_key, []))))
    except Exception as e:
        logger.error(f"Error validating using distribution: '{str(e)}'")
        return True
