import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timezone

from ois_client_sdk.common.parameter.builders.serialize_text_element import serialize_text_element


@dataclass
class Header:
    request_id: str
    request_version: str
    header_version: str
    timestamp: datetime

    def serialize(self, parent: ET.Element) -> ET.Element:
        result = ET.SubElement(parent, 'header')

        serialize_text_element(result, 'requestId', self.request_id)
        serialize_text_element(result, 'timestamp',
                               self.timestamp.replace(tzinfo=timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%fZ'))
        serialize_text_element(result, 'requestVersion', self.request_version)
        serialize_text_element(result, 'headerVersion', self.header_version)

        return result
