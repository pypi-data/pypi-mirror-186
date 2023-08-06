"""
Material

This model checks if the `machinery` Input has been added and updates the
[Data Completeness](https://hestia.earth/schema/Completeness#material) value.
"""
from hestia_earth.schema import SiteSiteType
from hestia_earth.utils.model import find_term_match

from hestia_earth.models.log import logger
from . import MODEL

REQUIREMENTS = {
    "Cycle": {
        "inputs": [{"@type": "Input", "value": "", "term.@id": "machineryInfrastructureDepreciatedAmountPerCycle"}],
        "site": {
            "@type": "Site",
            "siteType": ["cropland", "glass or high accessible cover"]
        }
    }
}
RETURNS = {
    "Completeness": {
        "material": ""
    }
}
MODEL_KEY = 'material'
ALLOWED_SITE_TYPES = [
    SiteSiteType.CROPLAND.value,
    SiteSiteType.GLASS_OR_HIGH_ACCESSIBLE_COVER.value
]


def run(cycle: dict):
    site_type = cycle.get('site', {}).get('siteType')
    site_type_allowed = site_type in ALLOWED_SITE_TYPES
    input = find_term_match(cycle.get('inputs', []), 'machineryInfrastructureDepreciatedAmountPerCycle', None)
    is_complete = all([site_type_allowed, input])
    logger.debug('model=%s, key=%s, value=%s', MODEL, MODEL_KEY, is_complete)
    return is_complete
