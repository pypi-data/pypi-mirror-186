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
        "startDate": "",
        "endDate": "",
        "statsDefinition": "spatial"
    }]
}
TERM_ID = 'precipitationLongTermAnnualMean'
START_DATE = '1979-01-01'
END_DATE = '2020-12-31'
EE_PARAMS = {
    'collection': 'ECMWF/ERA5/MONTHLY',
    'ee_type': 'raster_by_period',
    'reducer': 'sum',
    'reducer_regions': 'mean',
    'reducer_years': 'mean',
    'band_name': 'total_precipitation',
    'start_date': START_DATE,
    'end_date': END_DATE
}
BIBLIO_TITLE = 'ERA5: Fifth generation of ECMWF atmospheric reanalyses of the global climate'


def _measurement(value: float):
    measurement = _new_measurement(TERM_ID, MODEL, BIBLIO_TITLE)
    measurement['value'] = [value]
    measurement['statsDefinition'] = MeasurementStatsDefinition.SPATIAL.value
    measurement['startDate'] = START_DATE
    measurement['endDate'] = END_DATE
    return measurement


def _download(site: dict):
    # collection is in meters, convert to millimeters
    factor = 1000
    value = download(TERM_ID, site, EE_PARAMS).get(EE_PARAMS['reducer_years'])
    return value * factor if value else None


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
