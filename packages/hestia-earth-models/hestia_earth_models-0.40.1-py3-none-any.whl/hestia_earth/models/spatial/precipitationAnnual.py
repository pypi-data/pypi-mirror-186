"""
Must be associated with at least 1 `Cycle` that has an
[endDate](https://hestia.earth/schema/Cycle#endDate) after `1979-01-01` and before `2020-06-01`.
"""
from hestia_earth.schema import MeasurementStatsDefinition
from hestia_earth.utils.tools import non_empty_list

from hestia_earth.models.log import logRequirements, logShouldRun
from hestia_earth.models.utils.measurement import _new_measurement
from hestia_earth.models.utils.cycle import cycle_end_year
from hestia_earth.models.utils.site import related_cycles
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
TERM_ID = 'precipitationAnnual'
EE_PARAMS = {
    'collection': 'ECMWF/ERA5/MONTHLY',
    'ee_type': 'raster_by_period',
    'reducer': 'sum',
    'reducer_regions': 'mean',
    'band_name': 'total_precipitation'
}
BIBLIO_TITLE = 'ERA5: Fifth generation of ECMWF atmospheric reanalyses of the global climate'


def _valid_year(year: int):
    # NOTE: Currently uses the climate data for the final year of the study
    # see: https://developers.google.com/earth-engine/datasets/catalog/ECMWF_ERA5_MONTHLY
    # ERA5 data is available from 1979-01-01 to 2020-06-01
    return 1979 <= year and year <= 2020


def _measurement(value: float, year: int):
    measurement = _new_measurement(TERM_ID, MODEL, BIBLIO_TITLE)
    measurement['value'] = [value]
    measurement['statsDefinition'] = MeasurementStatsDefinition.SPATIAL.value
    measurement['startDate'] = f"{year}-01-01"
    measurement['endDate'] = f"{year}-12-31"
    return measurement


def _download(site: dict, year: int):
    # collection is in meters, convert to millimeters
    factor = 1000
    value = download(
        TERM_ID,
        site,
        {
            **EE_PARAMS,
            'year': str(year)
        }
    ).get(EE_PARAMS['reducer_regions'])
    return value * factor if value else None


def _run(site: dict, year: int):
    value = find_existing_measurement(TERM_ID, site, year) or _download(site, year)
    return _measurement(value, year) if value else None


def run(site: dict):
    contains_geospatial_data = has_geospatial_data(site)
    below_max_area_size = should_download(TERM_ID, site)

    cycles = related_cycles(site.get('@id'))
    years = non_empty_list(set(map(cycle_end_year, cycles)))
    years = list(filter(_valid_year, years))
    has_years = len(years) > 0

    logRequirements(site, model=MODEL, term=TERM_ID,
                    contains_geospatial_data=contains_geospatial_data,
                    below_max_area_size=below_max_area_size,
                    related_cycles=';'.join(map(lambda c: c.get('@id'), cycles)),
                    has_years=has_years,
                    years=';'.join(map(lambda y: str(y), years)))

    should_run = all([contains_geospatial_data, below_max_area_size, has_years])
    logShouldRun(site, MODEL, TERM_ID, should_run)

    return non_empty_list(map(lambda year: _run(site, year), years)) if should_run else []
