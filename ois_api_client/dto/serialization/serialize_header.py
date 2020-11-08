import xml.etree.ElementTree as ET
from datetime import timezone

from .. import BasicHeader
from .serialize_element import serialize_text_element
from ..xml.get_full_tag import get_full_tag
from ...constants import NAMESPACE_COMMON


def serialize_header(data: BasicHeader) -> ET.Element:
    result = ET.Element(get_full_tag(NAMESPACE_COMMON, 'header'))

    serialize_text_element(result, 'requestId', data.request_id, NAMESPACE_COMMON)
    serialize_text_element(result, 'timestamp',
                           f'{data.timestamp.astimezone(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]}Z',
                           NAMESPACE_COMMON)
    serialize_text_element(result, 'requestVersion', data.request_version, NAMESPACE_COMMON)
    serialize_text_element(result, 'headerVersion', data.header_version, NAMESPACE_COMMON)

    return result
