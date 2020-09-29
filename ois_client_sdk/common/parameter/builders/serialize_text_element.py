import xml.etree.ElementTree as ET


def serialize_text_element(parent: ET.Element, tag: str, text: str) -> ET.Element:
    result = ET.SubElement(parent, tag)
    result.text = text
    return result
