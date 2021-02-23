from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ...deserialization.create_enum import create_enum
from ..dto.BasicResult import BasicResult
from ..dto.FunctionCode import FunctionCode
from .deserialize_notifications import deserialize_notifications


def deserialize_basic_result(element: ET.Element) -> Optional[BasicResult]:
    if element is None:
        return None

    result = BasicResult(
        func_code=create_enum(FunctionCode, XR.get_child_text(element, 'funcCode', COMMON)),
        error_code=XR.get_child_text(element, 'errorCode', COMMON),
        message=XR.get_child_text(element, 'message', COMMON),
        notifications=deserialize_notifications(
            XR.find_child(element, 'notifications', COMMON)
        ),
    )

    return result
