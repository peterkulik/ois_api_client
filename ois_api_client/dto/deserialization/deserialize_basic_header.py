import xml.etree.ElementTree as ET
from .XmlReader import XmlReader as XR
from ..BasicHeader import BasicHeader
from ...constants import NAMESPACE_COMMON


def deserialize_basic_header(parent: ET.Element):
    if parent is None:
        return None

    res_el = XR.find_child(parent, 'header', NAMESPACE_COMMON)

    if res_el is None:
        return None

    result = BasicHeader(
        request_id=XR.get_child_text(res_el, 'requestId', NAMESPACE_COMMON),
        timestamp=XR.get_child_utc_datetime(res_el, 'timestamp', NAMESPACE_COMMON),
        request_version=XR.get_child_text(res_el, 'requestVersion', NAMESPACE_COMMON),
        header_version=XR.get_child_text(res_el, 'headerVersion', NAMESPACE_COMMON)
    )

    return result
