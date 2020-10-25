import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from .deserialize_customer_declaration import deserialize_customer_declaration
from .deserialize_product_fee_takeover_data import deserialize_product_fee_takeover_data
from ..ProductFeeClause import ProductFeeClause
from ...constants import NAMESPACE_DATA


def _get_data(element: ET.Element):
    if element is None:
        return None

    product_fee_takeover_data = XR.find_child(element, 'productFeeTakeoverData', NAMESPACE_DATA)

    if product_fee_takeover_data is not None:
        return deserialize_product_fee_takeover_data(product_fee_takeover_data)

    customer_declaration = XR.find_child(element, 'customerDeclaration', NAMESPACE_DATA)

    if customer_declaration is not None:
        return deserialize_customer_declaration(customer_declaration)

    return None


def deserialize_product_fee_clause(element: ET.Element) -> Union[ProductFeeClause, None]:
    if element is None:
        return None

    result = ProductFeeClause(
        data=_get_data(element)
    )

    return result
