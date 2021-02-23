from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..namespaces import DATA
from ..dto.MaterialNumbers import MaterialNumbers


def deserialize_material_numbers(element: ET.Element) -> Optional[MaterialNumbers]:
    if element is None:
        return None

    result = MaterialNumbers(
        material_number=[e.text for e in XR.find_all_child(element, 'materialNumber', DATA)],
    )

    return result
