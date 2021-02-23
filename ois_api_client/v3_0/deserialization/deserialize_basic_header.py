from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..dto.BasicHeader import BasicHeader


def deserialize_basic_header(element: ET.Element) -> Optional[BasicHeader]:
    if element is None:
        return None

    result = BasicHeader(
        request_id=XR.get_child_text(element, 'requestId', COMMON),
        timestamp=XR.get_child_datetime(element, 'timestamp', COMMON),
        request_version=XR.get_child_text(element, 'requestVersion', COMMON),
        header_version=XR.get_child_text(element, 'headerVersion', COMMON),
    )

    return result
