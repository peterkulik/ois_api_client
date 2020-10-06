import xml.etree.ElementTree as ET
from datetime import datetime
from typing import List, Union

from ...constants import NAMESPACE


class XmlReader:
    @staticmethod
    def get_child_text(parent: ET.Element, tag_name: str) -> Union[str, None]:
        child = parent.find(f'{{{NAMESPACE}}}{tag_name}')

        if child is None:
            return None

        return child.text

    @staticmethod
    def find_child(parent: ET.Element, tag_name: str) -> ET.Element:
        return parent.find(f'{{{NAMESPACE}}}{tag_name}')

    @staticmethod
    def find_all_child(parent: ET.Element, tag_name: str) -> List[ET.Element]:
        return parent.findall(f'{{{NAMESPACE}}}{tag_name}')

    @staticmethod
    def find_child_as_datetime(parent: ET.Element, tag_name: str) -> datetime:
        element = parent.find(f'{{{NAMESPACE}}}{tag_name}')
        result = datetime.strptime(element.text, '%Y-%m-%dT%H:%M:%S.%f%z')
        return result
