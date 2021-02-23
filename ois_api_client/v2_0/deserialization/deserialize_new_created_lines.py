from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..namespaces import DATA
from ..dto.NewCreatedLines import NewCreatedLines


def deserialize_new_created_lines(element: ET.Element) -> Optional[NewCreatedLines]:
    if element is None:
        return None

    result = NewCreatedLines(
        line_number_interval_start=XR.get_child_int(element, 'lineNumberIntervalStart', API),
        line_number_interval_end=XR.get_child_int(element, 'lineNumberIntervalEnd', API),
    )

    return result
