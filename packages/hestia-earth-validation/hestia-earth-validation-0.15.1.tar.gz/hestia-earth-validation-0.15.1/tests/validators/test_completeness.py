import json
from unittest.mock import patch
from hestia_earth.schema import SiteSiteType, TermTermType

from tests.utils import fixtures_path
from hestia_earth.validation.validators.completeness import (
    validate_completeness, _validate_all_values, _validate_cropland, _validate_material
)

class_path = 'hestia_earth.validation.validators.completeness'


def test_validate_completeness_valid():
    with open(f"{fixtures_path}/completeness/valid.json") as f:
        data = json.load(f)
    assert validate_completeness({'completeness': data}) is True


def test_validate_all_values_valid():
    with open(f"{fixtures_path}/completeness/valid.json") as f:
        data = json.load(f)
    assert _validate_all_values(data) is True


def test_validate_all_values_warning():
    with open(f"{fixtures_path}/completeness/all-values/warning.json") as f:
        data = json.load(f)
    assert _validate_all_values(data) == {
        'level': 'warning',
        'dataPath': '.completeness',
        'message': 'may not all be set to false'
    }


def test_validate_cropland_valid():
    with open(f"{fixtures_path}/completeness/cropland/site.json") as f:
        site = json.load(f)
    with open(f"{fixtures_path}/completeness/cropland/valid.json") as f:
        data = json.load(f)
    assert _validate_cropland(data, site) is True

    # also works if siteType is not cropland
    site['siteType'] = SiteSiteType.LAKE.value
    data[TermTermType.EXCRETA.value] = False
    assert _validate_cropland(data, site) is True


def test_validate_cropland_warning():
    with open(f"{fixtures_path}/completeness/cropland/site.json") as f:
        site = json.load(f)
    with open(f"{fixtures_path}/completeness/cropland/warning.json") as f:
        data = json.load(f)
    assert _validate_cropland(data, site) == [
        {
            'level': 'warning',
            'dataPath': '.completeness.animalFeed',
            'message': 'should be true for site of type cropland'
        },
        {
            'level': 'warning',
            'dataPath': '.completeness.excreta',
            'message': 'should be true for site of type cropland'
        }
    ]


FUEL_IDS = [
    'gasoline',
    'diesel'
]


@patch(f"{class_path}.get_fuel_terms", return_value=FUEL_IDS)
def test_validate_material_valid(*args):
    with open(f"{fixtures_path}/completeness/material/valid-incomplete.json") as f:
        data = json.load(f)
    assert _validate_material(data) is True

    with open(f"{fixtures_path}/completeness/material/valid-no-fuel.json") as f:
        data = json.load(f)
    assert _validate_material(data) is True

    with open(f"{fixtures_path}/completeness/material/valid-fuel-material.json") as f:
        data = json.load(f)
    assert _validate_material(data) is True


@patch(f"{class_path}.get_fuel_terms", return_value=FUEL_IDS)
def test_validate_material_error(*args):
    with open(f"{fixtures_path}/completeness/material/error.json") as f:
        data = json.load(f)
    assert _validate_material(data) == {
        'level': 'error',
        'dataPath': '.completeness.material',
        'message': 'must be set to false when specifying fuel use',
        'params': {
            'allowedValues': FUEL_IDS
        }
    }
