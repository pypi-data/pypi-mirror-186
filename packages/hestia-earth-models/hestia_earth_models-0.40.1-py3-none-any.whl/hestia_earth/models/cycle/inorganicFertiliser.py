"""
Inorganic Fertiliser

This model calculates the amount of other nutrient(s) supplied by multi-nutrients inorganic fertilisers when only
the amount of one of the nutrients is recorded by the user.
"""
from hestia_earth.schema import InputStatsDefinition, TermTermType
from hestia_earth.utils.model import filter_list_term_type, find_term_match
from hestia_earth.utils.tools import non_empty_list, safe_parse_float, list_sum

from hestia_earth.models.log import debugValues, logRequirements, logShouldRun
from hestia_earth.models.utils.input import _new_input
from hestia_earth.models.utils.constant import Units
from hestia_earth.models.utils.inorganicFertiliser import get_term_lookup
from . import MODEL

REQUIREMENTS = {
    "Cycle": {
        "inputs": [{
            "@type": "Input",
            "term.termType": "inorganicFertiliser",
            "value": "> 0"
        }]
    }
}
RETURNS = {
    "Input": [{
        "term.termType": "inorganicFertiliser",
        "value": "",
        "statsDefinition": "modelled"
    }]
}
LOOKUPS = {
    "inorganicFertiliser": ["mustIncludeId", "nitrogenContent", "phosphateContentAsP2O5", "potassiumContentAsK2O"]
}
MODEL_KEY = 'inorganicFertiliser'
MODEL_LOG = '/'.join([MODEL, MODEL_KEY])

UNITS = [
    Units.KG_P2O5.value,
    Units.KG_K2O.value
]
VALUE_BY_UNIT = {
    Units.KG_N.value: {
        Units.KG_K2O.value: lambda value, nContent, p2O5Content, k2OContent: value * k2OContent / nContent,
        Units.KG_P2O5.value: lambda value, nContent, p2O5Content, k2OContent: value * p2O5Content / nContent
    },
    Units.KG_K2O.value: {
        Units.KG_N.value: lambda value, nContent, p2O5Content, k2OContent: value / k2OContent * nContent,
        Units.KG_P2O5.value: lambda value, nContent, p2O5Content, k2OContent: value / k2OContent * p2O5Content
    },
    Units.KG_P2O5.value: {
        Units.KG_N.value: lambda value, nContent, p2O5Content, k2OContent: value / p2O5Content * nContent,
        Units.KG_K2O.value: lambda value, nContent, p2O5Content, k2OContent: value / p2O5Content * k2OContent
    }
}


def _input(value: float, term_id: str):
    input = _new_input(term_id)
    input['value'] = [value]
    input['statsDefinition'] = InputStatsDefinition.MODELLED.value
    return input


def _run_input(cycle: dict, input: dict):
    term_id = input.get('term', {}).get('@id')
    include_term_id = get_term_lookup(term_id, 'mustIncludeId')
    nitrogenContent = safe_parse_float(get_term_lookup(term_id, 'nitrogenContent'), 0)
    phosphateContentAsP2O5 = safe_parse_float(get_term_lookup(term_id, 'phosphateContentAsP2O5'), 0)
    potassiumContentAsK2O = safe_parse_float(get_term_lookup(term_id, 'potassiumContentAsK2O'), 0)

    from_units = input.get('term', {}).get('units')
    to_units = Units.KG_N.value if include_term_id.endswith('KgN') else (
        Units.KG_K2O.value if include_term_id.endswith('KgK2O') else Units.KG_P2O5.value
    )
    input_value = list_sum(input.get('value'))

    debugValues(cycle, model=MODEL_LOG, term=term_id,
                from_units=from_units,
                to_units=to_units,
                input_value=input_value)

    value = VALUE_BY_UNIT.get(input.get('term', {}).get('units'), {}).get(to_units, lambda *args: None)(
        input_value, nitrogenContent, phosphateContentAsP2O5, potassiumContentAsK2O
    )
    return _input(value, include_term_id) if value else None


def _should_run_input(cycle: dict, input: dict):
    term_id = input.get('term', {}).get('@id')
    mustIncludeId = get_term_lookup(term_id, 'mustIncludeId')
    has_value = list_sum(input.get('value', [])) > 0
    nitrogenContent = safe_parse_float(get_term_lookup(term_id, 'nitrogenContent'), None)
    phosphateContentAsP2O5 = safe_parse_float(get_term_lookup(term_id, 'phosphateContentAsP2O5'), None)
    potassiumContentAsK2O = safe_parse_float(get_term_lookup(term_id, 'potassiumContentAsK2O'), None)

    logRequirements(cycle, model=MODEL_LOG, term=mustIncludeId,
                    nitrogenContent=nitrogenContent,
                    phosphateContentAsP2O5=phosphateContentAsP2O5,
                    potassiumContentAsK2O=potassiumContentAsK2O)

    should_run = all([
        has_value,
        len(non_empty_list([nitrogenContent, phosphateContentAsP2O5, potassiumContentAsK2O])) >= 2
    ])
    logShouldRun(cycle, MODEL_LOG, mustIncludeId, should_run)
    return should_run


def _filter_input(inputs: list):
    def exec(input: dict):
        term_id = input.get('term', {}).get('@id')
        mustIncludeId = get_term_lookup(term_id, 'mustIncludeId')
        input_to_include = find_term_match(inputs, mustIncludeId) if mustIncludeId else {}
        has_value = len(input_to_include.get('value', [])) > 0
        # skip inputs that already have the inlcuded term with a value
        return not all([input_to_include.get('term', {}).get('@id'), has_value])
    return exec


def run(cycle: dict):
    inputs = filter_list_term_type(cycle.get('inputs', []), TermTermType.INORGANICFERTILISER)
    inputs = list(filter(_filter_input(inputs), inputs))
    inputs = [i for i in inputs if _should_run_input(cycle, i)]
    return non_empty_list([_run_input(cycle, i) for i in inputs])
