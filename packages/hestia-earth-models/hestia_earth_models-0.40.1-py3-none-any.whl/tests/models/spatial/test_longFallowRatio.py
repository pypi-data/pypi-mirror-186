from unittest.mock import patch
import json
from tests.utils import fixtures_path, fake_new_practice

from hestia_earth.models.spatial.croppingIntensity import MODEL, TERM_ID, run, _should_run

class_path = f"hestia_earth.models.{MODEL}.{TERM_ID}"
fixtures_folder = f"{fixtures_path}/{MODEL}/{TERM_ID}"


@patch(f"{class_path}.is_orchard", return_value=False)
@patch(f"{class_path}.should_download", return_value=True)
@patch(f"{class_path}.has_geospatial_data")
def test_should_run(mock_has_geospatial_data, *args):
    cycle = {'@type': 'Cycle', 'site': {'@type': 'Site'}}

    mock_has_geospatial_data.return_value = True
    assert _should_run(cycle) is True

    mock_has_geospatial_data.return_value = False
    assert not _should_run(cycle)


@patch(f"{class_path}._new_practice", side_effect=fake_new_practice)
@patch(f"{class_path}.download", return_value=10)
def test_run(*args):
    with open(f"{fixtures_folder}/cycle.jsonld", encoding='utf-8') as f:
        cycle = json.load(f)

    with open(f"{fixtures_folder}/result.jsonld", encoding='utf-8') as f:
        expected = json.load(f)

    result = run(cycle)
    assert result == expected
