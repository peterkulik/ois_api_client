import xml.etree.ElementTree as ET
from typing import Optional

from .XmlReader import XmlReader as XR
from ..ReferencesToOtherLines import ReferencesToOtherLines
from ...constants import NAMESPACE_DATA


def deserialize_references_to_other_lines(element: ET.Element) -> Optional[ReferencesToOtherLines]:
    if element is None:
        return None

    result = ReferencesToOtherLines(
        items=[int(el.text) for el in XR.find_all_child(element, 'referenceToOtherLine', NAMESPACE_DATA)]
    )

    return result
