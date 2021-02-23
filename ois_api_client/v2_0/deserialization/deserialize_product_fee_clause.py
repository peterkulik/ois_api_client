from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.ProductFeeClause import ProductFeeClause
from .deserialize_customer_declaration import deserialize_customer_declaration
from .deserialize_product_fee_takeover_data import deserialize_product_fee_takeover_data


def deserialize_product_fee_clause(element: ET.Element) -> Optional[ProductFeeClause]:
    if element is None:
        return None

    result = ProductFeeClause(
        product_fee_takeover_data=deserialize_product_fee_takeover_data(
            XR.find_child(element, 'productFeeTakeoverData', DATA)
        ),
        customer_declaration=deserialize_customer_declaration(
            XR.find_child(element, 'customerDeclaration', DATA)
        ),
    )

    return result
