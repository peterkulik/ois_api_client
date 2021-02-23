from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.ProductCodes import ProductCodes
from .deserialize_product_code import deserialize_product_code


def deserialize_product_codes(element: ET.Element) -> Optional[ProductCodes]:
    if element is None:
        return None

    result = ProductCodes(
        product_code=[deserialize_product_code(e) for e in XR.find_all_child(element, 'productCode', DATA)],
    )

    return result
