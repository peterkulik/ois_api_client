import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from .deserialize_product_code import deserialize_product_code
from ..ProductCodes import ProductCodes
from ...constants import NAMESPACE_DATA


def deserialize_product_codes(element: ET.Element) -> Union[ProductCodes, None]:
    if element is None:
        return None

    result = ProductCodes(
        items=[deserialize_product_code(el) for el in XR.find_all_child(element, 'productCode', NAMESPACE_DATA)]
    )

    return result
