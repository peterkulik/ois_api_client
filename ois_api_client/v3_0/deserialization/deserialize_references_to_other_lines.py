from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import BASE
from ..namespaces import DATA
from ..dto.ReferencesToOtherLines import ReferencesToOtherLines


def deserialize_references_to_other_lines(element: ET.Element) -> Optional[ReferencesToOtherLines]:
    if element is None:
        return None

    result = ReferencesToOtherLines(
        reference_to_other_line=[int(e.text) for e in XR.find_all_child(element, 'referenceToOtherLine', DATA)],
    )

    return result
