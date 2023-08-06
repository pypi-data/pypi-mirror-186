from hestia_earth.schema import MeasurementStatsDefinition

from hestia_earth.models.log import logRequirements, logShouldRun
from hestia_earth.models.utils.measurement import _new_measurement
from .utils import download, find_existing_measurement, has_geospatial_data, should_download
from . import MODEL

REQUIREMENTS = {
    "Site": {
        "or": [
            {"latitude": "", "longitude": ""},
            {"boundary": {}},
            {"region": {"@type": "Term", "termType": "region"}}
        ]
    }
}
RETURNS = {
    "Measurement": [{
        "value": "",
        "depthUpper": "0",
        "depthLower": "30",
        "statsDefinition": "spatial"
    }]
}
TERM_ID = 'sandContent'
EE_PARAMS = {
    'collection': 'T_SAND',
    'ee_type': 'raster',
    'reducer': 'mean',
    'fields': 'mean'
}
BIBLIO_TITLE = 'Harmonized World Soil Database Version 1.2. Food and Agriculture Organization of the United Nations (FAO).'  # noqa: E501


def _measurement(value: int):
    measurement = _new_measurement(TERM_ID, MODEL, BIBLIO_TITLE)
    measurement['value'] = [value]
    measurement['depthUpper'] = 0
    measurement['depthLower'] = 30
    measurement['statsDefinition'] = MeasurementStatsDefinition.SPATIAL.value
    return measurement


def _download(site: dict):
    value = download(TERM_ID, site, EE_PARAMS).get(EE_PARAMS['reducer'])
    return None if value is None else round(value, 2)


def _run(site: dict):
    value = find_existing_measurement(TERM_ID, site) or _download(site)
    return [_measurement(value)] if value is not None else []


def _should_run(site: dict):
    contains_geospatial_data = has_geospatial_data(site)
    below_max_area_size = should_download(TERM_ID, site)

    logRequirements(site, model=MODEL, term=TERM_ID,
                    contains_geospatial_data=contains_geospatial_data,
                    below_max_area_size=below_max_area_size)

    should_run = all([contains_geospatial_data, below_max_area_size])
    logShouldRun(site, MODEL, TERM_ID, should_run)
    return should_run


def run(site: dict): return _run(site) if _should_run(site) else []
