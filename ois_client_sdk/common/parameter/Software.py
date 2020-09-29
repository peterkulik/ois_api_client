import xml.etree.ElementTree as ET
from dataclasses import dataclass

from ois_client_sdk.common.parameter.builders.serialize_text_element import serialize_text_element


@dataclass
class Software:
    id: str
    name: str
    operation: str
    main_version: str
    dev_name: str
    dev_contact: str
    dev_country_code: str
    dev_tax_number: str

    def serialize(self, parent: ET.Element) -> ET.Element:
        result = ET.SubElement(parent, 'software')

        serialize_text_element(result, 'softwareId', self.id)
        serialize_text_element(result, 'softwareName', self.name)
        serialize_text_element(result, 'softwareOperation', self.operation)
        serialize_text_element(result, 'softwareMainVersion', self.main_version)
        serialize_text_element(result, 'softwareDevName', self.dev_name)
        serialize_text_element(result, 'softwareDevContact', self.dev_contact)
        serialize_text_element(result, 'softwareDevCountryCode', self.dev_country_code)
        serialize_text_element(result, 'softwareDevTaxNumber', self.dev_tax_number)

        return result
