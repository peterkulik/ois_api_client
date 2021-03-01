from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import BASE
from ..namespaces import COMMON
from ..namespaces import DATA
from ...deserialization.create_enum import create_enum
from ..dto.Line import Line
from ..dto.LineNatureIndicator import LineNatureIndicator
from ..dto.UnitOfMeasure import UnitOfMeasure
from .deserialize_additional_data import deserialize_additional_data
from .deserialize_advance_data import deserialize_advance_data
from .deserialize_aggregate_invoice_line_data import deserialize_aggregate_invoice_line_data
from .deserialize_conventional_invoice_info import deserialize_conventional_invoice_info
from .deserialize_diesel_oil_purchase import deserialize_diesel_oil_purchase
from .deserialize_discount_data import deserialize_discount_data
from .deserialize_line_amounts_normal import deserialize_line_amounts_normal
from .deserialize_line_amounts_simplified import deserialize_line_amounts_simplified
from .deserialize_line_modification_reference import deserialize_line_modification_reference
from .deserialize_new_transport_mean import deserialize_new_transport_mean
from .deserialize_product_codes import deserialize_product_codes
from .deserialize_product_fee_clause import deserialize_product_fee_clause
from .deserialize_product_fee_data import deserialize_product_fee_data
from .deserialize_references_to_other_lines import deserialize_references_to_other_lines


def deserialize_line(element: ET.Element) -> Optional[Line]:
    if element is None:
        return None

    result = Line(
        line_number=XR.get_child_int(element, 'lineNumber', DATA),
        line_modification_reference=deserialize_line_modification_reference(
            XR.find_child(element, 'lineModificationReference', DATA)
        ),
        references_to_other_lines=deserialize_references_to_other_lines(
            XR.find_child(element, 'referencesToOtherLines', DATA)
        ),
        advance_data=deserialize_advance_data(
            XR.find_child(element, 'advanceData', DATA)
        ),
        product_codes=deserialize_product_codes(
            XR.find_child(element, 'productCodes', DATA)
        ),
        line_expression_indicator=XR.get_child_bool(element, 'lineExpressionIndicator', DATA),
        line_nature_indicator=create_enum(LineNatureIndicator, XR.get_child_text(element, 'lineNatureIndicator', DATA)),
        line_description=XR.get_child_text(element, 'lineDescription', DATA),
        quantity=XR.get_child_float(element, 'quantity', DATA),
        unit_of_measure=create_enum(UnitOfMeasure, XR.get_child_text(element, 'unitOfMeasure', DATA)),
        unit_of_measure_own=XR.get_child_text(element, 'unitOfMeasureOwn', DATA),
        unit_price=XR.get_child_float(element, 'unitPrice', DATA),
        unit_price_huf=XR.get_child_float(element, 'unitPriceHUF', DATA),
        line_discount_data=deserialize_discount_data(
            XR.find_child(element, 'lineDiscountData', DATA)
        ),
        line_amounts_normal=deserialize_line_amounts_normal(
            XR.find_child(element, 'lineAmountsNormal', DATA)
        ),
        line_amounts_simplified=deserialize_line_amounts_simplified(
            XR.find_child(element, 'lineAmountsSimplified', DATA)
        ),
        intermediated_service=XR.get_child_bool(element, 'intermediatedService', DATA),
        aggregate_invoice_line_data=deserialize_aggregate_invoice_line_data(
            XR.find_child(element, 'aggregateInvoiceLineData', DATA)
        ),
        new_transport_mean=deserialize_new_transport_mean(
            XR.find_child(element, 'newTransportMean', DATA)
        ),
        deposit_indicator=XR.get_child_bool(element, 'depositIndicator', DATA),
        obligated_for_product_fee=XR.get_child_bool(element, 'obligatedForProductFee', DATA),
        gpc_excise=XR.get_child_float(element, 'GPCExcise', DATA),
        diesel_oil_purchase=deserialize_diesel_oil_purchase(
            XR.find_child(element, 'dieselOilPurchase', DATA)
        ),
        neta_declaration=XR.get_child_bool(element, 'netaDeclaration', DATA),
        product_fee_clause=deserialize_product_fee_clause(
            XR.find_child(element, 'productFeeClause', DATA)
        ),
        line_product_fee_content=[deserialize_product_fee_data(e) for e in XR.find_all_child(element, 'lineProductFeeContent', DATA)],
        conventional_line_info=deserialize_conventional_invoice_info(
            XR.find_child(element, 'conventionalLineInfo', DATA)
        ),
        additional_line_data=[deserialize_additional_data(e) for e in XR.find_all_child(element, 'additionalLineData', DATA)],
    )

    return result
