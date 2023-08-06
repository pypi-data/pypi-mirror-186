from hestia_earth.schema import SchemaType, TermTermType
from hestia_earth.utils.api import download_hestia
from hestia_earth.utils.model import find_term_match, linked_node, filter_list_term_type
from hestia_earth.utils.tools import list_sum, non_empty_list, list_average
from hestia_earth.utils.lookup import download_lookup, get_table_value, column_name

from ..log import debugValues, logger
from . import _term_id, _include_methodModel, _filter_list_term_unit, _load_calculated_node, _filter_list_term_types
from .constant import Units
from .property import get_node_property_value, get_node_property_value_converted
from .blank_node import get_total_value, get_total_value_converted


def _new_input(term, model=None):
    node = {'@type': SchemaType.INPUT.value}
    node['term'] = linked_node(term if isinstance(term, dict) else download_hestia(_term_id(term)))
    return _include_methodModel(node, model)


def load_impacts(inputs: list):
    """
    Load and return `Input`s that have an `impactAssessment`.

    Parameters
    ----------
    inputs : list
        A list of `Input`.

    Returns
    -------
    list
        The filtered list of `Input` with full `impactAssessment` node.
    """
    def _load_impact(input: dict):
        impact = input.get('impactAssessment')
        impact = _load_calculated_node(impact, SchemaType.IMPACTASSESSMENT) if impact else None
        return {**input, 'impactAssessment': impact} if impact else None

    # filter by inputs that have an impactAssessment
    return non_empty_list(map(_load_impact, inputs))


def sum_input_impacts(inputs: list, term_id: str) -> float:
    """
    Load and return the sum of the `emissionsResourceUse` value linked to each `Input`.

    Parameters
    ----------
    inputs : list
        A list of `Input`.

    Returns
    -------
    float
        The total impact of the `Input` for the `Term` or `None` if none found.
    """
    def _input_value(input: dict):
        impact = input.get('impactAssessment', {})
        indicators = impact.get('emissionsResourceUse', []) + impact.get('impacts', [])
        value = find_term_match(indicators, term_id).get('value', None)
        input_value = list_sum(input.get('value', [0]))
        logger.debug('input with impact, term=%s, input=%s, input value=%s, impact value=%s',
                     term_id, input.get('term', {}).get('@id'), input_value, value)
        return value * input_value if value is not None else None

    inputs = load_impacts(inputs)
    logger.debug('term=%s, nb inputs impact=%s', term_id, len(inputs))
    return list_sum(non_empty_list(map(_input_value, inputs)), None)


def match_lookup_value(input: dict, col_name: str, col_value):
    """
    Check if input matches lookup value.

    Parameters
    ----------
    inputs : dict
        An `Input`.
    col_name : str
        The name of the column in the lookup table.
    col_value : Any
        The cell value matching the row/column in the lookup table.

    Returns
    -------
    list
        A list of `Input`.
    """
    term_type = input.get('term', {}).get('termType')
    lookup = download_lookup(f"{term_type}.csv")
    term_id = input.get('term', {}).get('@id')
    return get_table_value(lookup, 'termid', term_id, column_name(col_name)) == col_value


def _get_feed_inputs(inputs: list):
    inputs = _filter_list_term_unit(inputs, Units.KG)
    inputs = _filter_list_term_types(inputs, [
        TermTermType.CROP,
        TermTermType.ANIMALPRODUCT,
        TermTermType.OTHER
    ])
    return inputs


def get_feed(inputs: list, prop: str = 'energyContentHigherHeatingValue'):
    return list_sum([get_node_property_value_converted(input, prop) for input in _get_feed_inputs(inputs)])


def get_feed_nitrogen(node: dict, model: str, term_id: str, inputs: list):
    def prop_value(input: dict):
        value = get_node_property_value(input, 'nitrogenContent')
        return value / 100 if value > 0 else get_node_property_value(input, 'crudeProteinContent') / 625

    inputs_values = [(i, prop_value(i)) for i in _get_feed_inputs(inputs)]
    inputs_no_property = [i.get('term', {}).get('@id') for i, p_value in inputs_values if not p_value]

    debugValues(node, model=model, term=term_id,
                inputs_no_property=';'.join(inputs_no_property))

    return list_sum([
        list_sum(i.get('value', [])) * p_value for i, p_value in inputs_values
    ]) if len(inputs_no_property) == 0 else None


def get_feed_carbon(node: dict, model: str, term_id: str, inputs: list):
    def prop_value(input: dict):
        value = get_node_property_value(input, 'carbonContent')
        return value / 100 if value > 0 else get_node_property_value(input, 'energyContentHigherHeatingValue') * 0.021

    inputs_values = [(i, prop_value(i)) for i in _get_feed_inputs(inputs)]
    inputs_no_property = [i.get('term', {}).get('@id') for i, p_value in inputs_values if not p_value]

    debugValues(node, model=model, term=term_id,
                inputs_no_property=';'.join(inputs_no_property))

    return list_sum([
        list_sum(i.get('value', [])) * p_value for i, p_value in inputs_values
    ]) if len(inputs_no_property) == 0 else None


def total_excreta_tan(inputs: list):
    """
    Get the total excreta ammoniacal nitrogen from all the excreta inputs in `kg N` units.
    Will use the `totalAmmoniacalNitrogenContentAsN` property to convert to kg of TAN.

    Parameters
    ----------
    inputs : list
        List of `Input`s.

    Returns
    -------
    float
        The total value as a number.
    """
    excreta = filter_list_term_type(inputs, TermTermType.EXCRETA)
    excreta_kg_N = _filter_list_term_unit(excreta, Units.KG_N)
    return list_sum(get_total_value_converted(excreta_kg_N, 'totalAmmoniacalNitrogenContentAsN'))


def total_excreta(inputs: list, units=Units.KG_N):
    """
    Get the total excreta from all the excreta inputs in `kg N` units.

    Parameters
    ----------
    inputs : list
        List of `Input`s.
    units: Units
        The units of the excreta. Can be either `kg`, `kg N` or `kg VS`.

    Returns
    -------
    float
        The total value as a number.
    """
    excreta = filter_list_term_type(inputs, TermTermType.EXCRETA)
    excreta = _filter_list_term_unit(excreta, units)
    return list_sum(get_total_value(excreta))


def get_total_irrigation_m3(cycle: dict):
    irrigation_inputs = filter_list_term_type(cycle.get('inputs', []), TermTermType.WATER)
    return sum([list_average(i.get('value')) for i in irrigation_inputs if len(i.get('value', [])) > 0])
