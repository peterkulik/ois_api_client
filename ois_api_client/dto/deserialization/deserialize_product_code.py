import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from ..ProductCode import ProductCode
from ..ProductCodeCategory import ProductCodeCategory
from ...constants import NAMESPACE_DATA


def deserialize_product_code(element: ET.Element) -> Union[ProductCode, None]:
    if element is None:
        return None

    product_code_category = XR.find_child(element, 'productCodeCategory', NAMESPACE_DATA)

    result = ProductCode(
        product_code_category=ProductCodeCategory(product_code_category) if product_code_category is not None else None,
        product_code_value=XR.get_child_text(element, 'productCodeValue', NAMESPACE_DATA),
        product_code_own_value=XR.get_child_text(element, 'productCodeOwnValue', NAMESPACE_DATA)
    )

    return result
