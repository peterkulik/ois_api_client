import xml.etree.ElementTree as ET
from .XmlReader import XmlReader as XR
from .deserialize_notifications import deserialize_notifications
from ..BasicResult import BasicResult
from ...constants import NAMESPACE_COMMON


def deserialize_basic_result(parent: ET.Element):
    if parent is None:
        return None

    res_el = XR.find_child(parent, 'result', NAMESPACE_COMMON)

    if res_el is None:
        return None

    result = BasicResult(
        func_code=XR.get_child_text(res_el, 'funcCode', NAMESPACE_COMMON),
        message=XR.get_child_text(res_el, 'message', NAMESPACE_COMMON),
        error_code=XR.get_child_text(res_el, 'errorCode', NAMESPACE_COMMON),
        notifications=deserialize_notifications(XR.find_child(res_el, 'notifications', NAMESPACE_COMMON))
    )

    return result
