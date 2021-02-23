from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.DiscountData import DiscountData


def deserialize_discount_data(element: ET.Element) -> Optional[DiscountData]:
    if element is None:
        return None

    result = DiscountData(
        discount_description=XR.get_child_text(element, 'discountDescription', DATA),
        discount_value=XR.get_child_float(element, 'discountValue', DATA),
        discount_rate=XR.get_child_float(element, 'discountRate', DATA),
    )

    return result
