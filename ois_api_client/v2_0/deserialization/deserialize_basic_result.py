from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..namespaces import DATA
from ...deserialization.create_enum import create_enum
from ..dto.BasicResult import BasicResult
from ..dto.FunctionCode import FunctionCode


def deserialize_basic_result(element: ET.Element) -> Optional[BasicResult]:
    if element is None:
        return None

    result = BasicResult(
        func_code=create_enum(FunctionCode, XR.get_child_text(element, 'funcCode', API)),
        error_code=XR.get_child_text(element, 'errorCode', API),
        message=XR.get_child_text(element, 'message', API),
    )

    return result
