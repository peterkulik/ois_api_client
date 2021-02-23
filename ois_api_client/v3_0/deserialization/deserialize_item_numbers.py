from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..namespaces import DATA
from ..dto.ItemNumbers import ItemNumbers


def deserialize_item_numbers(element: ET.Element) -> Optional[ItemNumbers]:
    if element is None:
        return None

    result = ItemNumbers(
        item_number=[e.text for e in XR.find_all_child(element, 'itemNumber', DATA)],
    )

    return result
