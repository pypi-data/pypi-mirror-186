from hestia_earth.schema import MeasurementStatsDefinition, TermTermType

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
        ],
        "none": {
            "measurements": [{"@type": "Measurement", "value": "", "term.termType": "soilType"}]
        }
    }
}
RETURNS = {
    "Measurement": [{
        "value": "",
        "statsDefinition": "spatial"
    }]
}
TERM_ID = 'histosol'
EE_PARAMS = {
    'collection': 'histosols_perc',
    'ee_type': 'raster',
    'reducer': 'mean',
    'fields': 'mean'
}
BIBLIO_TITLE = 'Harmonized World Soil Database Version 1.2. Food and Agriculture Organization of the United Nations (FAO).'  # noqa: E501


def _measurement(value: float):
    measurement = _new_measurement(TERM_ID, MODEL, BIBLIO_TITLE)
    measurement['value'] = [round(value, 7)]
    measurement['statsDefinition'] = MeasurementStatsDefinition.SPATIAL.value
    return measurement


def _download(site: dict):
    return download(TERM_ID, site, EE_PARAMS).get(EE_PARAMS['reducer'])


def _run(site: dict):
    value = find_existing_measurement(TERM_ID, site) or _download(site)
    return [_measurement(value)] if value is not None else []


def _should_run(site: dict):
    measurements = site.get('measurements', [])
    no_soil_type = all([m.get('term', {}).get('termType') != TermTermType.SOILTYPE.value for m in measurements])
    contains_geospatial_data = has_geospatial_data(site)
    below_max_area_size = should_download(TERM_ID, site)

    logRequirements(site, model=MODEL, term=TERM_ID,
                    contains_geospatial_data=contains_geospatial_data,
                    below_max_area_size=below_max_area_size,
                    no_soil_type=no_soil_type)

    should_run = all([contains_geospatial_data, below_max_area_size, no_soil_type])
    logShouldRun(site, MODEL, TERM_ID, should_run)
    return should_run


def run(site: dict): return _run(site) if _should_run(site) else []
