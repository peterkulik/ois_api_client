from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import BASE
from ..namespaces import DATA
from ...deserialization.create_enum import create_enum
from ..dto.LineModificationReference import LineModificationReference
from ..dto.LineOperation import LineOperation


def deserialize_line_modification_reference(element: ET.Element) -> Optional[LineModificationReference]:
    if element is None:
        return None

    result = LineModificationReference(
        line_number_reference=XR.get_child_int(element, 'lineNumberReference', DATA),
        line_operation=create_enum(LineOperation, XR.get_child_text(element, 'lineOperation', DATA)),
    )

    return result
