from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..namespaces import DATA
from ..dto.ShippingDates import ShippingDates


def deserialize_shipping_dates(element: ET.Element) -> Optional[ShippingDates]:
    if element is None:
        return None

    result = ShippingDates(
        shipping_date=[e.text for e in XR.find_all_child(element, 'shippingDate', DATA)],
    )

    return result
