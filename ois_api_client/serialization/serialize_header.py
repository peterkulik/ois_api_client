import xml.etree.ElementTree as ET
from datetime import timezone

from ..v3_0 import dto, namespaces as ns
from .serialize_element import serialize_text_element
from ois_api_client.xml.get_full_tag import get_full_tag


def serialize_header(data: dto.BasicHeader) -> ET.Element:
    result = ET.Element(get_full_tag(ns.COMMON, 'header'))

    serialize_text_element(result, 'requestId', data.request_id, ns.COMMON)
    serialize_text_element(result, 'timestamp',
                           f'{data.timestamp.astimezone(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]}Z',
                           ns.COMMON)
    serialize_text_element(result, 'requestVersion', data.request_version, ns.COMMON)
    serialize_text_element(result, 'headerVersion', data.header_version, ns.COMMON)

    return result
