from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.Lines import Lines
from .deserialize_line import deserialize_line


def deserialize_lines(element: ET.Element) -> Optional[Lines]:
    if element is None:
        return None

    result = Lines(
        line=[deserialize_line(e) for e in XR.find_all_child(element, 'line', DATA)],
    )

    return result
