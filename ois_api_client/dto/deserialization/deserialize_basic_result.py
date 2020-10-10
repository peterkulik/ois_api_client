import xml.etree.ElementTree as ET
from .XmlReader import XmlReader as XR
from ..BasicResult import BasicResult


def deserialize_basic_result(parent: ET.Element):
    if parent is None:
        return None

    if (res_el := XR.find_child(parent, 'result')) is None:
        return None

    result = BasicResult(
        func_code=XR.get_child_text(res_el, 'funcCode'),
        message=XR.get_child_text(res_el, 'message'),
        error_code=XR.get_child_text(res_el, 'errorCode'),
        notifications=[]
    )

    return result
