import xml.etree.ElementTree as ET
from datetime import timezone

from .. import BasicHeader
from .serialize_element import serialize_text_element
from ...constants import REQUEST_VERSION, HEADER_VERSION


def serialize_header(data: BasicHeader) -> ET.Element:
    result = ET.Element('header')

    serialize_text_element(result, 'requestId', data.request_id)
    serialize_text_element(result, 'timestamp',
                           f'{data.timestamp.astimezone(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]}Z')
    serialize_text_element(result, 'requestVersion', REQUEST_VERSION)
    serialize_text_element(result, 'headerVersion', HEADER_VERSION)

    return result
