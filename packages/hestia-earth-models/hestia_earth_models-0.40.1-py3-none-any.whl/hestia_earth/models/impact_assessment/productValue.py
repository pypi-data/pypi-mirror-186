"""
Product Value

Returns the [value](https://hestia.earth/schema/Product#value) of the Product linked to the Cycle.
"""
from hestia_earth.utils.tools import list_sum

from hestia_earth.models.log import logger
from hestia_earth.models.utils.impact_assessment import get_product
from . import MODEL

REQUIREMENTS = {
    "ImpactAssessment": {
        "cycle": {
            "@type": "Cycle",
            "products": [{"@type": "Product", "value": ""}]
        }
    }
}
RETURNS = {
    "The product value as a number": ""
}
MODEL_KEY = 'productValue'


def run(impact: dict):
    value = list_sum(get_product(impact).get('value', []), None)
    logger.debug('model=%s, key=%s, value=%s', MODEL, MODEL_KEY, value)
    return value
