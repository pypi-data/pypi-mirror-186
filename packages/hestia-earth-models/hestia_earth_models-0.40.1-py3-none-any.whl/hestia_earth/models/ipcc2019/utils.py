from hestia_earth.utils.model import find_term_match

from hestia_earth.models.log import debugValues
from hestia_earth.models.utils.input import get_total_irrigation_m3
from hestia_earth.models.utils.cycle import get_ecoClimateZone
from . import MODEL


def get_FracLEACH_H(cycle: dict, term_id: str):
    eco_climate_zone = get_ecoClimateZone(cycle)
    is_eco_climate_zone_dry = eco_climate_zone % 2 == 0
    irrigation_value_m3 = get_total_irrigation_m3(cycle)
    is_drip_irrigated = find_term_match(cycle.get('practices', []), 'irrigatedDripIrrigation', None) is not None

    debugValues(cycle, model=MODEL, term=term_id,
                is_eco_climate_zone_dry=is_eco_climate_zone_dry,
                irrigation_value_m3=irrigation_value_m3,
                is_drip_irrigated=is_drip_irrigated)

    return (0, 0, 0, 0) if all([
        is_eco_climate_zone_dry,
        any([irrigation_value_m3 <= 250, is_drip_irrigated])
    ]) else (0.24, 0.01, 0.73, 0.18)  # value, min, max, sd
