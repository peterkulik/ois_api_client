from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..namespaces import DATA
from ..dto.ProjectNumbers import ProjectNumbers


def deserialize_project_numbers(element: ET.Element) -> Optional[ProjectNumbers]:
    if element is None:
        return None

    result = ProjectNumbers(
        project_number=[e.text for e in XR.find_all_child(element, 'projectNumber', DATA)],
    )

    return result
