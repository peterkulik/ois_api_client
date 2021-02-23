import xml.etree.ElementTree as ET

from ois_api_client.xml.get_full_tag import get_full_tag


def validate_tag_name(element: ET.Element, namespace: str, tag_name: str):
    assert get_full_tag(namespace, tag_name) == element.tag


def validate_element(element: ET.Element, namespace: str, tag_name: str, expected_value: str):
    validate_tag_name(element, namespace, tag_name)
    assert element.text == expected_value
