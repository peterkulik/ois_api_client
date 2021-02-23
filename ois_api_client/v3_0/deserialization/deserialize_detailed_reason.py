from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..namespaces import DATA
from ..dto.DetailedReason import DetailedReason


def deserialize_detailed_reason(element: ET.Element) -> Optional[DetailedReason]:
    if element is None:
        return None

    result = DetailedReason(
        case=XR.get_child_text(element, 'case', DATA),
        reason=XR.get_child_text(element, 'reason', DATA),
    )

    return result
