from decimal import Decimal
import xml.etree.ElementTree as ET
from datetime import datetime, date, timezone
from typing import List, Union

from ...constants import NAMESPACE


class XmlReader:
    @staticmethod
    def get_child_text(parent: ET.Element, tag_name: str) -> Union[str, None]:
        child = parent.find(f'{{{NAMESPACE}}}{tag_name}')
        return None if child is None else child.text

    @staticmethod
    def get_child_int(parent: ET.Element, tag_name: str) -> Union[int, None]:
        text = XmlReader.get_child_text(parent, tag_name)
        return None if text is None else int(text)

    @staticmethod
    def get_child_bool(parent: ET.Element, tag_name: str) -> Union[bool, None]:
        text = XmlReader.get_child_text(parent, tag_name)
        return None if text is None else text.lower() == 'true'

    @staticmethod
    def get_child_decimal(parent: ET.Element, tag_name: str) -> Union[Decimal, None]:
        text = XmlReader.get_child_text(parent, tag_name)
        return None if text is None else Decimal(text)

    @staticmethod
    def get_child_date(parent: ET.Element, tag_name: str) -> Union[date, None]:
        text = XmlReader.get_child_text(parent, tag_name)
        return None if text is None else datetime.strptime(text, '%Y-%m-%d')

    @staticmethod
    def get_child_utc_datetime(parent: ET.Element, tag_name: str) -> Union[datetime, None]:
        text = XmlReader.get_child_text(parent, tag_name)
        return None if text is None else datetime.strptime(text, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=timezone.utc)

    @staticmethod
    def find_child(parent: ET.Element, tag_name: str) -> ET.Element:
        return parent.find(f'{{{NAMESPACE}}}{tag_name}')

    @staticmethod
    def find_all_child(parent: ET.Element, tag_name: str) -> List[ET.Element]:
        return parent.findall(f'{{{NAMESPACE}}}{tag_name}')

    @staticmethod
    def get_child_datetime_tz_offset(parent: ET.Element, tag_name: str) -> datetime:
        text = XmlReader.get_child_text(parent, tag_name)
        element = parent.find(f'{{{NAMESPACE}}}{tag_name}')
        return None if text is None else datetime.strptime(element.text, '%Y-%m-%dT%H:%M:%S.%f%z')
