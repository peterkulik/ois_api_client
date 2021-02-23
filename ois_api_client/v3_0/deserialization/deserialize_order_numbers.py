from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..namespaces import DATA
from ..dto.OrderNumbers import OrderNumbers


def deserialize_order_numbers(element: ET.Element) -> Optional[OrderNumbers]:
    if element is None:
        return None

    result = OrderNumbers(
        order_number=[e.text for e in XR.find_all_child(element, 'orderNumber', DATA)],
    )

    return result
