from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..dto.BasicRequest import BasicRequest
from .deserialize_basic_header import deserialize_basic_header
from .deserialize_user_header import deserialize_user_header


def deserialize_basic_request(element: ET.Element) -> Optional[BasicRequest]:
    if element is None:
        return None

    result = BasicRequest(
        header=deserialize_basic_header(
            XR.find_child(element, 'header', COMMON)
        ),
        user=deserialize_user_header(
            XR.find_child(element, 'user', COMMON)
        ),
    )

    return result
