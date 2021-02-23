from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..namespaces import API
from ..dto.GeneralErrorResponse import GeneralErrorResponse
from .deserialize_basic_header import deserialize_basic_header
from .deserialize_basic_result import deserialize_basic_result
from .deserialize_software import deserialize_software
from .deserialize_technical_validation_result import deserialize_technical_validation_result


def deserialize_general_error_response(element: ET.Element) -> Optional[GeneralErrorResponse]:
    if element is None:
        return None

    result = GeneralErrorResponse(
        header=deserialize_basic_header(
            XR.find_child(element, 'header', COMMON)
        ),
        result=deserialize_basic_result(
            XR.find_child(element, 'result', COMMON)
        ),
        software=deserialize_software(
            XR.find_child(element, 'software', API)
        ),
        technical_validation_messages=[deserialize_technical_validation_result(e) for e in XR.find_all_child(element, 'technicalValidationMessages', API)],
    )

    return result
