import xml.etree.ElementTree as ET
from datetime import date, datetime
from typing import Optional, Dict
from ois_api_client.xml.get_full_tag import get_full_tag


def serialize_text_element(parent: ET.Element, tag: str, text: Optional[str], namespace: str,
                           attribs: Dict = None) -> Optional[ET.Element]:
    if text is None:
        return None

    result = ET.SubElement(parent, get_full_tag(namespace, tag), attribs if attribs else {})
    result.text = text
    return result


def serialize_int_element(parent: ET.Element, tag: str, value: Optional[int], namespace: str) -> Optional[ET.Element]:
    return serialize_text_element(parent, tag, str(value), namespace)


def format_float(value: float, decimal_digits: int) -> str:
    return format(float(value), f'.{decimal_digits}f')


def serialize_float_element(parent: ET.Element, tag: str, value: float, decimal_digits: int,
                            namespace: str) -> ET.Element:
    return serialize_text_element(parent, tag, format_float(value, decimal_digits), namespace)


def serialize_date_element(parent: ET.Element, tag: str, value: date) -> ET.Element:
    result = ET.SubElement(parent, tag)
    result.text = value.strftime('%Y-%m-%d')
    return result


def serialize_datetime_element(parent: ET.Element, tag: str, value: datetime) -> ET.Element:
    result = ET.SubElement(parent, tag)
    result.text = value.strftime('%Y-%m-%dT%H:%M:%SZ')
    return result


def serialize_date_interval(parent: ET.Element, tag: str, date_from: date, date_to: date) -> ET.Element:
    result = ET.SubElement(parent, tag)
    serialize_date_element(result, 'dateFrom', date_from)
    serialize_date_element(result, 'dateTo', date_to)
    return result


def serialize_datetime_interval(parent: ET.Element, tag: str, datetime_from: datetime,
                                datetime_to: datetime) -> ET.Element:
    result = ET.SubElement(parent, tag)
    serialize_datetime_element(result, 'dateTimeFrom', datetime_from)
    serialize_datetime_element(result, 'dateTimeTo', datetime_to)
    return result
