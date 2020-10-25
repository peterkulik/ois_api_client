from decimal import Decimal
import xml.etree.ElementTree as ET
from datetime import datetime, date, timezone
from typing import List, Union

from ...constants import NAMESPACE_API


class XmlReader:
    @staticmethod
    def get_child_text(parent: ET.Element, tag_name: str, namespace: str = NAMESPACE_API,
                       default: str = None) -> Union[str, None]:
        child = parent.find(f'{{{namespace}}}{tag_name}')
        return default if child is None else child.text

    @staticmethod
    def get_child_int(parent: ET.Element, tag_name: str, namespace: str = NAMESPACE_API) -> Union[int, None]:
        text = XmlReader.get_child_text(parent, tag_name, namespace)
        return None if text is None else int(text)

    @staticmethod
    def get_child_bool(parent: ET.Element, tag_name: str, namespace: str = NAMESPACE_API,
                       default: Union[bool, None] = None) -> Union[bool, None]:
        text = XmlReader.get_child_text(parent, tag_name, namespace)
        return default if text is None else text.lower() == 'true'

    @staticmethod
    def get_child_float(parent: ET.Element, tag_name: str, namespace: str = NAMESPACE_API) -> Union[float, None]:
        text = XmlReader.get_child_text(parent, tag_name, namespace)
        return None if text is None else float(text)

    @staticmethod
    def get_child_date(parent: ET.Element, tag_name: str, namespace: str = NAMESPACE_API) -> Union[date, None]:
        text = XmlReader.get_child_text(parent, tag_name, namespace)
        return None if text is None else datetime.strptime(text, '%Y-%m-%d')

    @staticmethod
    def get_child_utc_datetime(parent: ET.Element, tag_name: str) -> Union[datetime, None]:
        text = XmlReader.get_child_text(parent, tag_name)
        return None if text is None else datetime.strptime(text, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=timezone.utc)

    @staticmethod
    def find_child(parent: ET.Element, tag_name: str, namespace: str = NAMESPACE_API) -> ET.Element:
        return parent.find(f'{{{namespace}}}{tag_name}')

    @staticmethod
    def find_all_child(parent: ET.Element, tag_name: str, namespace: str = NAMESPACE_API) -> List[ET.Element]:
        return parent.findall(f'{{{namespace}}}{tag_name}')

    @staticmethod
    def get_child_datetime_tz_offset(parent: ET.Element, tag_name: str) -> datetime:
        text = XmlReader.get_child_text(parent, tag_name)
        element = parent.find(f'{{{NAMESPACE_API}}}{tag_name}')
        return None if text is None else datetime.strptime(element.text, '%Y-%m-%dT%H:%M:%S.%f%z')
