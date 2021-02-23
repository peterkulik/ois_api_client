from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..dto.GeneralErrorHeaderResponse import GeneralErrorHeaderResponse
from .deserialize_basic_header import deserialize_basic_header
from .deserialize_basic_result import deserialize_basic_result


def deserialize_general_error_header_response(element: ET.Element) -> Optional[GeneralErrorHeaderResponse]:
    if element is None:
        return None

    result = GeneralErrorHeaderResponse(
        header=deserialize_basic_header(
            XR.find_child(element, 'header', COMMON)
        ),
        result=deserialize_basic_result(
            XR.find_child(element, 'result', COMMON)
        ),
    )

    return result
