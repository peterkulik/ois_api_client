import xml.etree.ElementTree as ET
from datetime import date, datetime
from typing import Union


def serialize_text_element(parent: ET.Element, tag: str, text: Union[str, None]) -> Union[ET.Element, None]:
    if text is None:
        return None

    result = ET.SubElement(parent, tag)
    result.text = text
    return result


def serialize_int_element(parent: ET.Element, tag: str, value: Union[int, None]) -> Union[ET.Element, None]:
    if value is None:
        return None

    result = ET.SubElement(parent, tag)
    result.text = str(value)
    return result


def format_float(value: float, decimal_digits: int) -> str:
    return format(float(value), f'.{decimal_digits}f')


def serialize_float_element(parent: ET.Element, tag: str, value: float, decimal_digits: int) -> ET.Element:
    return serialize_text_element(parent, tag, format_float(value, decimal_digits))


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
