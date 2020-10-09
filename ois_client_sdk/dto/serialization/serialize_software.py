import xml.etree.ElementTree as ET

from .. import Software
from .serialize_element import serialize_text_element


def serialize_software(data: Software) -> ET.Element:
    result = ET.Element('software')

    serialize_text_element(result, 'softwareId', data.id)
    serialize_text_element(result, 'softwareName', data.name)
    serialize_text_element(result, 'softwareOperation', data.operation)
    serialize_text_element(result, 'softwareMainVersion', data.main_version)
    serialize_text_element(result, 'softwareDevName', data.dev_name)
    serialize_text_element(result, 'softwareDevContact', data.dev_contact)
    serialize_text_element(result, 'softwareDevCountryCode', data.dev_country_code)
    serialize_text_element(result, 'softwareDevTaxNumber', data.dev_tax_number)

    return result
