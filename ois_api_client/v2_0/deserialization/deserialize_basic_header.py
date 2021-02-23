from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..namespaces import DATA
from ...deserialization.create_enum import create_enum
from ..dto.BasicHeader import BasicHeader
from ..dto.RequestVersion import RequestVersion
from ..dto.HeaderVersion import HeaderVersion


def deserialize_basic_header(element: ET.Element) -> Optional[BasicHeader]:
    if element is None:
        return None

    result = BasicHeader(
        request_id=XR.get_child_text(element, 'requestId', API),
        timestamp=XR.get_child_datetime(element, 'timestamp', API),
        request_version=create_enum(RequestVersion, XR.get_child_text(element, 'requestVersion', API)),
        header_version=create_enum(HeaderVersion, XR.get_child_text(element, 'headerVersion', API)),
    )

    return result
