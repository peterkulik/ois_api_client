import xml.etree.ElementTree as ET

from ois_api_client.dto.xml.get_full_tag import get_full_tag


def validate_element(element: ET.Element, namespace: str, tag_name: str, expected_value: str):
    assert element.tag == get_full_tag(namespace, tag_name)
    assert expected_value == element.text
