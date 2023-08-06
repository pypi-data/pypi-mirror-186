from unittest.mock import patch
import json
from tests.utils import fixtures_path, fake_new_measurement

from hestia_earth.models.spatial.precipitationAnnual import MODEL, TERM_ID, run

class_path = f"hestia_earth.models.{MODEL}.{TERM_ID}"
fixtures_folder = f"{fixtures_path}/{MODEL}/{TERM_ID}"


def fake_cycles(*args): return [{'@id': 'id', 'endDate': '2009'}]


@patch(f"{class_path}.find_existing_measurement", return_value=None)
@patch(f"{class_path}._new_measurement", side_effect=fake_new_measurement)
@patch(f"{class_path}.related_cycles", side_effect=fake_cycles)
@patch(f"{class_path}.download", return_value={})
def test_run(mock_download, *args):
    with open(f"{fixtures_path}/{MODEL}/site.jsonld", encoding='utf-8') as f:
        site = json.load(f)

    run(site)
    mock_download.assert_called_once()
