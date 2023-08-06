"""
Input Properties

This model adds properties to the `Input` when they are connected to another `Cycle` via the
[impactAssessment](https://hestia.earth/schema/Input#impactAssessment) field.
"""
from hestia_earth.schema import SchemaType
from hestia_earth.utils.model import find_term_match

from hestia_earth.models.log import logShouldRun
from hestia_earth.models.utils import _load_calculated_node
from .. import MODEL

REQUIREMENTS = {
    "Cycle": {
        "inputs": [{
            "@type": "Input",
            "impactAssessment": ""
        }]
    }
}
RETURNS = {
    "Inputs": [{
        "properties": [{
            "@type": "Property"
        }]
    }]
}
MODEL_KEY = 'properties'


def _run_input(cycle: dict):
    def exec(values: tuple):
        input, properties = values
        term_id = input.get('term', {}).get('@id')
        all_properties = input.get('properties', [])
        new_properties = [p for p in properties if not find_term_match(all_properties, p.get('term', {}).get('@id'))]
        for prop in new_properties:
            logShouldRun(cycle, MODEL, term_id, True, property=prop.get('term', {}).get('@id'))
        return {**input, 'properties': all_properties + new_properties}
    return exec


def _input_properties(input: dict):
    impact = input.get('impactAssessment')
    impact = _load_calculated_node(impact, SchemaType.IMPACTASSESSMENT) if impact else {}
    cycle = impact.get('cycle') if impact else None
    cycle = _load_calculated_node(cycle, SchemaType.CYCLE) if cycle else None
    products = (cycle or {}).get('products', [])
    return find_term_match(products, input.get('term', {}).get('@id')).get('properties', [])


def run(cycle: dict):
    # select inputs which have corresponding properties
    inputs = [(i, _input_properties(i)) for i in cycle.get('inputs', [])]
    inputs = [(input, properties) for input, properties in inputs if len(properties) > 0]
    return list(map(_run_input(cycle), inputs))
