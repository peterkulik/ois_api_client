from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ...deserialization.create_enum import create_enum
from ..dto.ProductCode import ProductCode
from ..dto.ProductCodeCategory import ProductCodeCategory


def deserialize_product_code(element: ET.Element) -> Optional[ProductCode]:
    if element is None:
        return None

    result = ProductCode(
        product_code_category=create_enum(ProductCodeCategory, XR.get_child_text(element, 'productCodeCategory', DATA)),
        product_code_value=XR.get_child_text(element, 'productCodeValue', DATA),
        product_code_own_value=XR.get_child_text(element, 'productCodeOwnValue', DATA),
    )

    return result
