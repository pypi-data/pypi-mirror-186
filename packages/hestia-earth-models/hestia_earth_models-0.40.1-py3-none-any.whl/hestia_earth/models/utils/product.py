from hestia_earth.schema import SchemaType, TermTermType
from hestia_earth.utils.api import download_hestia
from hestia_earth.utils.model import filter_list_term_type, find_term_match, linked_node
from hestia_earth.utils.tools import flatten, list_sum

from hestia_earth.models.utils.blank_node import get_total_value, get_total_value_converted
from . import _term_id, _include_methodModel
from .constant import Units
from .currency import DEFAULT_CURRENCY
from .property import _get_nitrogen_content, get_node_property
from .term import get_rice_paddy_terms


def _new_product(term, value: float = 0, model=None):
    node = {'@type': SchemaType.PRODUCT.value}
    node['term'] = linked_node(term if isinstance(term, dict) else download_hestia(_term_id(term)))
    node['value'] = [value]
    if value == 0:
        node['economicValueShare'] = 0
        node['revenue'] = 0
        node['currency'] = DEFAULT_CURRENCY
    return _include_methodModel(node, model)


def has_flooded_rice(products: list):
    """
    Checks if one of the product is a flooded rice.

    Parameters
    ----------
    products : list
        List of `Product`s.

    Returns
    -------
    float
        True if one product matches a rice paddy crop.
    """
    terms = get_rice_paddy_terms()
    return any([True for p in products if p.get('term', {}).get('@id') in terms])


def abg_total_residue_nitrogen_content(products: list):
    """
    Get the nitrogen content from the `aboveGroundCropResidueTotal` product.

    Parameters
    ----------
    products : list
        List of `Product`s.

    Returns
    -------
    float
        The total value as a number.
    """
    return _get_nitrogen_content(find_term_match(products, 'aboveGroundCropResidueTotal'))


def abg_residue_on_field_nitrogen_content(products: list):
    """
    Get the total nitrogen content from the above ground `cropResidue` left on the field.

    Parameters
    ----------
    products : list
        List of `Product`s.

    Returns
    -------
    float
        The total value as a number.
    """
    left_on_field = find_term_match(products, 'aboveGroundCropResidueLeftOnField').get('value', [0])
    incorporated = find_term_match(products, 'aboveGroundCropResidueIncorporated').get('value', [0])
    return list_sum(left_on_field + incorporated) * abg_total_residue_nitrogen_content(products) / 100


def blg_residue_nitrogen(products: list):
    """
    Get the total nitrogen content from the `belowGroundCropResidue` product.

    Parameters
    ----------
    products : list
        List of `Product`s.

    Returns
    -------
    float
        The total value as a number.
    """
    residue = find_term_match(products, 'belowGroundCropResidue')
    return list_sum(residue.get('value', [0])) * _get_nitrogen_content(residue) / 100


def discarded_total_residue_nitrogen_content(products: list):
    """
    Get the nitrogen content from the `discardedCropTotal` product.

    Parameters
    ----------
    products : list
        List of `Product`s.

    Returns
    -------
    float
        The total value as a number.
    """
    return _get_nitrogen_content(find_term_match(products, 'discardedCropTotal'))


def discarded_residue_on_field_nitrogen_content(products: list):
    """
    Get the total nitrogen content from the discarded `cropResidue` left on the field.

    Parameters
    ----------
    products : list
        List of `Product`s.

    Returns
    -------
    float
        The total value as a number.
    """
    left_on_field = find_term_match(products, 'discardedCropLeftOnField').get('value', [0])
    incorporated = find_term_match(products, 'discardedCropIncorporated').get('value', [0])
    return list_sum(left_on_field + incorporated) * discarded_total_residue_nitrogen_content(products) / 100


def animal_produced(products: list, prop: str = 'nitrogenContent') -> float:
    products = (
        filter_list_term_type(products, TermTermType.LIVEANIMAL) +
        filter_list_term_type(products, TermTermType.ANIMALPRODUCT) +
        filter_list_term_type(products, TermTermType.LIVEAQUATICSPECIES)
    )

    def product_value(product: dict):
        value = convert_product_to_unit(product, Units.KG_LIVEWEIGHT)
        property = get_node_property(product, prop)
        return value * property.get('value', 0) if property else 0

    return list_sum(list(map(product_value, products)))


PRODUCT_UNITS_CONVERSIONS = {
    Units.KG.value: {
        Units.KG_LIVEWEIGHT.value: [],
        Units.KG_N.value: [
            ('nitrogenContent', True)
        ],
        Units.KG_VS.value: [
            ('volatileSolidsContent', True)
        ]
    },
    Units.KG_N.value: {
        Units.KG.value: [
            ('nitrogenContent', False)
        ],
        Units.KG_VS.value: [
            ('nitrogenContent', False),
            ('volatileSolidsContent', True)
        ]
    },
    Units.KG_VS.value: {
        Units.KG.value: [
            ('volatileSolidsContent', False)
        ],
        Units.KG_N.value: [
            ('volatileSolidsContent', False),
            ('nitrogenContent', True)
        ]
    },
    Units.KG_LIVEWEIGHT.value: {
        Units.KG_LIVEWEIGHT.value: [],
        Units.KG_COLD_CARCASS_WEIGHT.value: [
            ('processingConversionLiveweightToColdCarcassWeight', True)
        ],
        Units.KG_COLD_DRESSED_CARCASS_WEIGHT.value: [
            ('processingConversionLiveweightToColdDressedCarcassWeight', True)
        ],
        Units.KG_READY_TO_COOK_WEIGHT.value: [
            (
                [
                    'processingConversionLiveweightToColdCarcassWeight',
                    'processingConversionColdCarcassWeightToReadyToCookWeight'
                ],
                True
            ),
            (
                [
                    'processingConversionLiveweightToColdDressedCarcassWeight',
                    'processingConversionColdDressedCarcassWeightToReadyToCookWeight'
                ],
                True
            )
        ]
    },
    Units.KG_COLD_CARCASS_WEIGHT.value: {
        Units.KG_LIVEWEIGHT.value: [
            ('processingConversionLiveweightToColdCarcassWeight', False)
        ],
        Units.KG_COLD_DRESSED_CARCASS_WEIGHT.value: [],
        Units.KG_COLD_CARCASS_WEIGHT.value: [],
        Units.KG_READY_TO_COOK_WEIGHT.value: [
            ('processingConversionColdCarcassWeightToReadyToCookWeight', True)
        ]
    },
    Units.KG_COLD_DRESSED_CARCASS_WEIGHT.value: {
        Units.KG_LIVEWEIGHT.value: [
            ('processingConversionLiveweightToColdDressedCarcassWeight', False)
        ],
        Units.KG_COLD_DRESSED_CARCASS_WEIGHT.value: [],
        Units.KG_COLD_CARCASS_WEIGHT.value: [],
        Units.KG_READY_TO_COOK_WEIGHT.value: [
            ('processingConversionColdDressedCarcassWeightToReadyToCookWeight', True)
        ]
    },
    Units.KG_READY_TO_COOK_WEIGHT.value: {
        Units.KG_LIVEWEIGHT.value: [
            (
                [
                    'processingConversionColdCarcassWeightToReadyToCookWeight',
                    'processingConversionLiveweightToColdCarcassWeight',
                ],
                False
            ),
            (
                [
                    'processingConversionColdDressedCarcassWeightToReadyToCookWeight',
                    'processingConversionLiveweightToColdDressedCarcassWeight'
                ],
                False
            )
        ],
        Units.KG_COLD_CARCASS_WEIGHT.value: [
            ('processingConversionColdCarcassWeightToReadyToCookWeight', False)
        ],
        Units.KG_COLD_DRESSED_CARCASS_WEIGHT.value: [
            ('processingConversionColdDressedCarcassWeightToReadyToCookWeight', False)
        ],
        Units.KG_READY_TO_COOK_WEIGHT.value: []
    },
    Units.HEAD.value: {
        Units.KG_LIVEWEIGHT.value: [
            ('liveweightPerHead', True)
        ]
    }
}


def convert_product_to_unit(product: dict, dest_unit: Units):
    units = product.get('term', {}).get('units')
    dest_key = dest_unit if isinstance(dest_unit, str) else dest_unit.value
    conversions = PRODUCT_UNITS_CONVERSIONS.get(units, {}).get(dest_key)
    return 0 if conversions is None else list_sum(
        flatten([
            get_total_value_converted([product], properties, multiply) for properties, multiply in conversions
        ]) if len(conversions) > 0 else get_total_value([product])
    )


def liveweight_produced(products: list):
    return list_sum([convert_product_to_unit(p, Units.KG_LIVEWEIGHT) for p in products])
