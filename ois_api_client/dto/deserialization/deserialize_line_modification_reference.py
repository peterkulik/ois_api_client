import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from ..LineModificationReference import LineModificationReference
from ..LineOperation import LineOperation
from ...constants import NAMESPACE_DATA


def deserialize_line_modification_reference(element: ET.Element) -> Union[LineModificationReference, None]:
    if element is None:
        return None

    line_operation = XR.find_child(element, 'lineOperation', NAMESPACE_DATA)

    result = LineModificationReference(
        line_number_reference=XR.get_child_int(element, 'lineNumberReference', NAMESPACE_DATA),
        line_operation=LineOperation(line_operation) if line_operation is not None else None
    )

    return result
