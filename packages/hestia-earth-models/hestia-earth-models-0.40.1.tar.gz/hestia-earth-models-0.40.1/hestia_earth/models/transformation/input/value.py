"""
Input Value

This model calculates the `value` of the [Input](https://hestia.earth/schema/Input)
by taking the value of the same [Product](https://hestia.earth/schema/Product) of the Cycle and applying the
[share](https://hestia.earth/schema/Transformation/transformedShare).
"""
from hestia_earth.schema import NodeType
from hestia_earth.utils.model import find_term_match

from hestia_earth.models.log import logShouldRun
from .. import MODEL

REQUIREMENTS = {
    "Cycle": {
        "products": [{"@type": "Product", "value": ""}],
        "transformations": [
            {
                "@type": "Transformation",
                "transformedShare": "",
                "inputs": [{"@type": "Input"}]
            }
        ]
    }
}
RETURNS = {
    "Transformation": [{
        "inputs": [{
            "@type": "Input",
            "value": ""
        }]
    }]
}
MODEL_KEY = 'value'
MODEL_LOG = '/'.join([MODEL, 'input', MODEL_KEY])


def _run_input(cycle: dict, input: dict, share: float):
    term_id = input.get('term', {}).get('@id')
    product = find_term_match(cycle.get('products', []), term_id)
    should_run = all([product])
    logShouldRun(cycle, MODEL_LOG, term_id, should_run)
    return {**input, 'value': [v * share / 100 for v in product.get('value', [])]} if should_run else input


def _run(cycle: dict):
    transformation = cycle.get('transformations', [])[0]
    share = transformation.get('transformedShare', 100)
    transformation['inputs'] = [_run_input(cycle, i, share) for i in transformation.get('inputs', [])]
    return [transformation]


def _should_run(cycle: dict):
    node_type = cycle.get('type', cycle.get('@type'))
    has_transformations = len(cycle.get('transformations', [])) > 0
    should_run = all([node_type == NodeType.CYCLE.value, has_transformations])
    logShouldRun(cycle, MODEL_LOG, None, should_run)
    return should_run


def run(cycle: dict): return _run(cycle) if _should_run(cycle) else []
