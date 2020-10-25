import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from .deserialize_additional_data import deserialize_additional_data
from .deserialize_aggregate_invoice_line_data import deserialize_aggregate_invoice_line_data
from .deserialize_diesel_oil_purchase import deserialize_diesel_oil_purchase
from .deserialize_discount_data import deserialize_discount_data
from .deserialize_ekaer_ids import deserialize_ekaer_ids
from .deserialize_line_amounts_normal import deserialize_line_amounts_normal
from .deserialize_line_amounts_simplified import deserialize_line_amounts_simplified
from .deserialize_line_modification_reference import deserialize_line_modification_reference
from .deserialize_new_transport_mean import deserialize_new_transport_mean
from .deserialize_product_codes import deserialize_product_codes
from .deserialize_product_fee_clause import deserialize_product_fee_clause
from .deserialize_product_fee_data import deserialize_product_fee_data
from .deserialize_references_to_other_lines import deserialize_references_to_other_lines
from ..Line import Line
from ..LineAmountsNormal import LineAmountsNormal
from ..LineAmountsSimplified import LineAmountsSimplified
from ..LineNatureIndicator import LineNatureIndicator
from ..Lines import Lines
from ..MarginScheme import MarginScheme
from ..UnitOfMeasure import UnitOfMeasure
from ...constants import NAMESPACE_DATA


def _get_line_amounts(element: ET.Element) -> Union[LineAmountsNormal, LineAmountsSimplified, None]:
    if element is None:
        return None

    line_amounts = None
    line_amounts_normal = XR.find_child(element, 'lineAmountsNormal', NAMESPACE_DATA)

    if line_amounts_normal is not None:
        line_amounts = deserialize_line_amounts_normal(line_amounts_normal)
    else:
        line_amounts_simplified = XR.find_child(element, 'lineAmountsSimplified', NAMESPACE_DATA)

        if line_amounts_simplified is not None:
            line_amounts = deserialize_line_amounts_simplified(
                XR.find_child(element, 'lineAmountsSimplified', NAMESPACE_DATA))

    return line_amounts


def _deserialize_invoice_line(element: ET.Element) -> Union[Line, None]:
    if element is None:
        return None

    line_nature_indicator = XR.find_child(element, 'lineNatureIndicator', NAMESPACE_DATA)
    unit_of_measure = XR.find_child(element, 'unitOfMeasure', NAMESPACE_DATA)
    margin_scheme = XR.find_child(element, 'marginSchemeIndicator', NAMESPACE_DATA)

    result = Line(
        line_number=XR.get_child_int(element, 'lineNumber', NAMESPACE_DATA),
        line_modification_reference=deserialize_line_modification_reference(
            XR.find_child(element, 'lineModificationReference', NAMESPACE_DATA)),
        references_to_other_lines=deserialize_references_to_other_lines(
            XR.find_child(element, 'referencesToOtherLines', NAMESPACE_DATA)),
        advance_indicator=XR.get_child_bool(element, 'advanceIndicator', NAMESPACE_DATA, False),
        product_codes=deserialize_product_codes(XR.find_child(element, 'productCodes', NAMESPACE_DATA)),
        line_expression_indicator=XR.get_child_bool(element, 'lineExpressionIndicator', NAMESPACE_DATA, False),
        line_nature_indicator=LineNatureIndicator(line_nature_indicator.text) if line_nature_indicator is not None else None,
        line_description=XR.get_child_text(element, 'lineDescription', NAMESPACE_DATA),
        quantity=XR.get_child_float(element, 'quantity', NAMESPACE_DATA),
        unit_of_measure=UnitOfMeasure(unit_of_measure.text) if unit_of_measure is not None else None,
        unit_of_measure_own=XR.get_child_text(element, 'unitOfMeasureOwn', NAMESPACE_DATA),
        unit_price=XR.get_child_float(element, 'unitPrice', NAMESPACE_DATA),
        unit_price_huf=XR.get_child_float(element, 'unitPriceHUF', NAMESPACE_DATA),
        line_discount_data=deserialize_discount_data(XR.find_child(element, 'lineDiscountData', NAMESPACE_DATA)),
        line_amounts=_get_line_amounts(element),
        intermediated_service=XR.get_child_bool(element, 'intermediatedService', NAMESPACE_DATA, False),
        aggregate_invoice_line_data=deserialize_aggregate_invoice_line_data(
            XR.find_child(element, 'aggregateInvoiceLineData', NAMESPACE_DATA)),
        new_transport_mean=deserialize_new_transport_mean(XR.find_child(element, 'newTransportMean', NAMESPACE_DATA)),
        deposit_indicator=XR.get_child_bool(element, 'depositIndicator', NAMESPACE_DATA),
        margin_scheme_indicator=MarginScheme(margin_scheme) if margin_scheme is not None else None,
        ekaer_ids=deserialize_ekaer_ids(XR.find_child(element, 'ekaerIds', NAMESPACE_DATA)),
        obligated_for_product_fee=XR.get_child_bool(element, 'obligatedForProductFee', NAMESPACE_DATA, False),
        gpc_excise=XR.get_child_float(element, 'GPCExcise', NAMESPACE_DATA),
        diesel_oil_purchase=deserialize_diesel_oil_purchase(
            XR.find_child(element, 'dieselOilPurchase', NAMESPACE_DATA)),
        neta_declaration=XR.get_child_bool(element, 'netaDeclaration', NAMESPACE_DATA, False),
        product_fee_clause=deserialize_product_fee_clause(XR.find_child(element, 'productFeeClause', NAMESPACE_DATA)),
        line_product_fee_content=[deserialize_product_fee_data(el) for el in
                                  XR.find_all_child(element, 'lineProductFeeContent', NAMESPACE_DATA)],
        additional_line_data=[deserialize_additional_data(el) for el in
                              XR.find_all_child(element, 'additionalLineData', NAMESPACE_DATA)]

    )

    return result


def deserialize_invoice_lines(element: ET.Element) -> Union[Lines, None]:
    if element is None:
        return None

    result = Lines(
        items=[_deserialize_invoice_line(el) for el in XR.find_all_child(element, 'line', NAMESPACE_DATA)]
    )

    return result
