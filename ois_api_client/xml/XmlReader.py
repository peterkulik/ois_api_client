import xml.etree.ElementTree as ET
from datetime import datetime, date, timezone
from typing import Optional, List
from .get_full_tag import get_full_tag


class XmlReader:
    @staticmethod
    def get_child_text(
            parent: ET.Element,
            tag_name: str,
            namespace: str,
            default: str = None) -> Optional[str]:
        child = parent.find(get_full_tag(namespace, tag_name))
        return default if child is None else child.text

    @staticmethod
    def get_child_int(
            parent: ET.Element,
            tag_name: str,
            namespace: str) -> Optional[int]:
        text = XmlReader.get_child_text(parent, tag_name, namespace)
        return None if text is None else int(text)

    @staticmethod
    def get_child_bool(
            parent: ET.Element,
            tag_name: str,
            namespace: str,
            default: Optional[bool] = None) -> Optional[bool]:
        text = XmlReader.get_child_text(parent, tag_name, namespace)
        return default if text is None else text.lower() == 'true'

    @staticmethod
    def get_child_float(
            parent: ET.Element,
            tag_name: str,
            namespace: str) -> Optional[float]:
        text = XmlReader.get_child_text(parent, tag_name, namespace)
        return None if text is None else float(text)

    @staticmethod
    def get_child_date(
            parent: ET.Element,
            tag_name: str,
            namespace: str) -> Optional[date]:
        text = XmlReader.get_child_text(parent, tag_name, namespace)
        return None if text is None else datetime.strptime(text, '%Y-%m-%d')

    @staticmethod
    def get_child_datetime(
            parent: ET.Element,
            tag_name: str,
            namespace: str) -> Optional[datetime]:
        text = XmlReader.get_child_text(parent, tag_name, namespace)
        return None if text is None else datetime.strptime(text, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=timezone.utc)

    @staticmethod
    def find_child(
            parent: ET.Element,
            tag_name: str,
            namespace: str) -> ET.Element:
        return parent.find(get_full_tag(namespace, tag_name))

    @staticmethod
    def find_all_child(
            parent: ET.Element,
            tag_name: str,
            namespace: str) -> List[ET.Element]:
        return parent.findall(get_full_tag(namespace, tag_name))

    @staticmethod
    def get_child_datetime_tz_offset(parent: ET.Element, tag_name: str, namespace: str) -> datetime:
        text = XmlReader.get_child_text(parent, tag_name)
        element = parent.find(get_full_tag(namespace, tag_name))
        return None if text is None else datetime.strptime(element.text, '%Y-%m-%dT%H:%M:%S.%f%z')
