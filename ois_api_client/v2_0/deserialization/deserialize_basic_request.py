from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..dto.BasicRequest import BasicRequest
from .deserialize_basic_header import deserialize_basic_header
from .deserialize_software import deserialize_software
from .deserialize_user_header import deserialize_user_header


def deserialize_basic_request(element: ET.Element) -> Optional[BasicRequest]:
    if element is None:
        return None

    result = BasicRequest(
        header=deserialize_basic_header(
            XR.find_child(element, 'header', API)
        ),
        user=deserialize_user_header(
            XR.find_child(element, 'user', API)
        ),
        software=deserialize_software(
            XR.find_child(element, 'software', API)
        ),
    )

    return result
