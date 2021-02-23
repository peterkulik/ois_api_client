from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..namespaces import DATA
from ..dto.GlnNumbers import GlnNumbers


def deserialize_gln_numbers(element: ET.Element) -> Optional[GlnNumbers]:
    if element is None:
        return None

    result = GlnNumbers(
        gln_number=[e.text for e in XR.find_all_child(element, 'glnNumber', DATA)],
    )

    return result
