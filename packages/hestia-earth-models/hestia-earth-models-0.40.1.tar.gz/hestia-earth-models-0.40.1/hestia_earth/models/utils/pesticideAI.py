from hestia_earth.schema import TermTermType
from hestia_earth.utils.model import filter_list_term_type

from hestia_earth.models.log import logRequirements, logShouldRun
from .impact_assessment import convert_value_from_cycle, get_product
from .cycle import impact_lookup_value as cycle_lookup_value


def impact_lookup_value(model: str, term_id: str, impact_assessment: dict, lookup_col: str):
    cycle = impact_assessment.get('cycle', {})
    pesticides_complete = cycle.get('completeness', {}).get('pesticidesAntibiotics', False)
    product = get_product(impact_assessment)
    pesticides = filter_list_term_type(cycle.get('inputs', []), TermTermType.PESTICIDEAI)
    has_pesticides_inputs = len(pesticides) > 0
    pesticides_value = convert_value_from_cycle(
        product, cycle_lookup_value(model, term_id, pesticides, lookup_col, False), None
    )
    logRequirements(impact_assessment, model=model, term=term_id,
                    pesticides_complete=pesticides_complete,
                    has_pesticides_inputs=has_pesticides_inputs)

    should_run = any([
        pesticides_complete and not has_pesticides_inputs,
        pesticides_complete and pesticides_value is not None
    ])
    logShouldRun(impact_assessment, model, term_id, should_run)

    return (pesticides_value or 0) if should_run else None
