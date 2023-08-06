"""
ecoinvent v3

This model calculates background emissions related to the production of Inputs from the ecoinvent database, version 3.

Note: to use the `ecoinventV3` model locally or in the
[Hestia Community Edition](https://gitlab.com/hestia-earth/hestia-community-edition) you need a valid ecoinvent license.
Please contact us at community@hestia.earth for instructions to download the required file to run the model.
"""
from functools import reduce
from hestia_earth.schema import EmissionMethodTier
from hestia_earth.utils.tools import flatten, list_sum, non_empty_list
from hestia_earth.utils.model import find_term_match

from hestia_earth.models.log import debugValues, logRequirements, logShouldRun
from hestia_earth.models.data.ecoinventV3 import ecoinventV3_emissions
from hestia_earth.models.utils.term import get_lookup_value
from hestia_earth.models.utils.emission import _new_emission
from hestia_earth.models.utils.blank_node import group_by_keys

REQUIREMENTS = {
    "Cycle": {
        "inputs": [{"@type": "Input", "value": "> 0"}]
    }
}
RETURNS = {
    "Emission": [{
        "term": "",
        "value": "",
        "methodTier": "background",
        "inputs": "",
        "operation": ""
    }]
}
MODEL = 'ecoinventV3'
MODEL_KEY = 'impactAssessment'  # keep to generate entry in "model-links.json"
TIER = EmissionMethodTier.BACKGROUND.value


def _emission(term_id: str, value: float, input: dict):
    emission = _new_emission(term_id, MODEL)
    emission['value'] = [value]
    emission['methodTier'] = TIER
    emission['inputs'] = [input.get('term')]
    if input.get('operation'):
        emission['operation'] = input.get('operation')
    return emission


def _add_emission(cycle: dict, input: dict):
    input_term_id = input.get('term', {}).get('@id')
    operation_term_id = input.get('operation', {}).get('term', {}).get('@id')

    def add(prev: dict, mapping: tuple):
        ecoinventName, coefficient = mapping
        emissions = ecoinventV3_emissions(ecoinventName)
        for id, value in emissions:
            # log run on each emission so we know it did run
            debugValues(cycle, model=MODEL, term=id,
                        value=value,
                        coefficient=coefficient,
                        input=input_term_id,
                        operation=operation_term_id)
            prev[id] = prev.get(id, 0) + (value * coefficient)
        return prev
    return add


def _get_input_mappings(cycle: dict, input: dict):
    term = input.get('term', {})
    term_id = term.get('@id')
    value = get_lookup_value(term, 'ecoinventMapping', model=MODEL, term=term_id)
    mappings = non_empty_list(value.split(';')) if value else []
    logRequirements(cycle, model=MODEL, term=term_id,
                    mappings=';'.join(mappings))
    return [(m.split(':')[0], float(m.split(':')[1])) for m in mappings]


def _run_input(cycle: dict):
    def run(inputs: list):
        input = inputs[0]
        input_value = list_sum(flatten(input.get('value', []) for input in inputs))
        mappings = _get_input_mappings(cycle, input)
        term_id = input.get('term', {}).get('@id')
        should_run = len(mappings) > 0
        logShouldRun(cycle, MODEL, term_id, should_run, methodTier=TIER)
        grouped_emissions = reduce(_add_emission(cycle, input), mappings, {}) if should_run else {}
        return [_emission(term_id, value * input_value, input) for term_id, value in grouped_emissions.items()]
    return run


def _should_run_input(products: list):
    def should_run(input: dict):
        return all([
            list_sum(input.get('value', [])) > 0,
            # make sure Input is not a Product as well or we might double-count emissions
            find_term_match(products, input.get('term', {}).get('@id'), None) is None
        ])
    return should_run


def run(cycle: dict):
    inputs = list(filter(_should_run_input(cycle.get('products', [])), cycle.get('inputs', [])))
    # group inputs with same id/operation to avoid adding emissions twice
    inputs = reduce(group_by_keys(['term', 'operation']), inputs, {})
    return flatten(map(_run_input(cycle), inputs.values()))
