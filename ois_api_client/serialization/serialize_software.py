import xml.etree.ElementTree as ET

from ..v3_0 import dto, namespaces as ns
from .serialize_element import serialize_text_element
from ois_api_client.xml.get_full_tag import get_full_tag


def serialize_software(data: dto.Software) -> ET.Element:
    result = ET.Element(get_full_tag(ns.API, 'software'))

    serialize_text_element(result, 'softwareId', data and data.software_id, ns.API)
    serialize_text_element(result, 'softwareName', data and data.software_name, ns.API)
    serialize_text_element(result, 'softwareOperation',
                           data and data.software_operation and data.software_operation.value, ns.API)
    serialize_text_element(result, 'softwareMainVersion', data and data.software_main_version, ns.API)
    serialize_text_element(result, 'softwareDevName', data and data.software_dev_name, ns.API)
    serialize_text_element(result, 'softwareDevContact', data and data.software_dev_contact, ns.API)
    serialize_text_element(result, 'softwareDevCountryCode', data and data.software_dev_country_code, ns.API)
    serialize_text_element(result, 'softwareDevTaxNumber', data and data.software_dev_tax_number, ns.API)

    return result
