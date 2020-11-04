import xml.etree.ElementTree as ET

from .. import Software
from .serialize_element import serialize_text_element
from ..xml.get_full_tag import get_full_tag
from ... import NAMESPACE_API


def serialize_software(data: Software) -> ET.Element:
    result = ET.Element(get_full_tag(NAMESPACE_API, 'software'))

    serialize_text_element(result, 'softwareId', data and data.id, NAMESPACE_API)
    serialize_text_element(result, 'softwareName', data and data.name, NAMESPACE_API)
    serialize_text_element(result, 'softwareOperation', data and data.operation and data.operation.value, NAMESPACE_API)
    serialize_text_element(result, 'softwareMainVersion', data and data.main_version, NAMESPACE_API)
    serialize_text_element(result, 'softwareDevName', data and data.dev_name, NAMESPACE_API)
    serialize_text_element(result, 'softwareDevContact', data and data.dev_contact, NAMESPACE_API)
    serialize_text_element(result, 'softwareDevCountryCode', data and data.dev_country_code, NAMESPACE_API)
    serialize_text_element(result, 'softwareDevTaxNumber', data and data.dev_tax_number, NAMESPACE_API)

    return result
