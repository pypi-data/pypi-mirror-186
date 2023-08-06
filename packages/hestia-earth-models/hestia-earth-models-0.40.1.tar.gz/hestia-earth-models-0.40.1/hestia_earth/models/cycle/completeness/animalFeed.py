"""
Animal feed

This model checks if the site is a cropland and updates the
[Data Completeness](https://hestia.earth/schema/Completeness#animalFeed) value.
"""
from hestia_earth.schema import SiteSiteType

from hestia_earth.models.log import logger
from . import MODEL

REQUIREMENTS = {
    "Cycle": {
        "completeness.animalFeed": "False",
        "site": {
            "@type": "Site",
            "siteType": ["cropland", "glass or high accessible cover"]
        }
    }
}
RETURNS = {
    "Completeness": {
        "animalFeed": ""
    }
}
MODEL_KEY = 'animalFeed'
ALLOWED_SITE_TYPES = [
    SiteSiteType.CROPLAND.value,
    SiteSiteType.GLASS_OR_HIGH_ACCESSIBLE_COVER.value
]


def run(cycle: dict):
    site_type = cycle.get('site', {}).get('siteType')
    site_type_allowed = site_type in ALLOWED_SITE_TYPES
    is_complete = all([site_type_allowed])
    logger.debug('model=%s, key=%s, value=%s', MODEL, MODEL_KEY, is_complete)
    return is_complete
