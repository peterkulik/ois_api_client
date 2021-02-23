from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..dto.BasicResponse import BasicResponse
from .deserialize_basic_header import deserialize_basic_header
from .deserialize_basic_result import deserialize_basic_result
from .deserialize_software import deserialize_software


def deserialize_basic_response(element: ET.Element) -> Optional[BasicResponse]:
    if element is None:
        return None

    result = BasicResponse(
        header=deserialize_basic_header(
            XR.find_child(element, 'header', API)
        ),
        result=deserialize_basic_result(
            XR.find_child(element, 'result', API)
        ),
        software=deserialize_software(
            XR.find_child(element, 'software', API)
        ),
    )

    return result
