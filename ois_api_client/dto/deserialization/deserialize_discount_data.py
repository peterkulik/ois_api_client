import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from ..DiscountData import DiscountData
from ...constants import NAMESPACE_DATA


def deserialize_discount_data(element: ET.Element) -> Union[DiscountData, None]:
    if element is None:
        return None

    result = DiscountData(
        discount_description=XR.get_child_text(element, 'discountDescription', NAMESPACE_DATA),
        discount_value=XR.get_child_float(element, 'discountValue', NAMESPACE_DATA),
        discount_rate=XR.get_child_float(element, 'discountRate', NAMESPACE_DATA)
    )

    return result


