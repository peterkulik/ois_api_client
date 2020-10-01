import xml.etree.ElementTree as ET
from dataclasses import dataclass

from ois_client_sdk.common.parameter.builders.serialize_text_element import serialize_text_element


@dataclass
class User:
    login: str
    tax_number: str

    def serialize(self, parent: ET.Element, password_hash: str, request_signature: str) -> ET.Element:
        result = ET.SubElement(parent, 'user')

        serialize_text_element(result, 'login', self.login)
        serialize_text_element(result, 'passwordHash', password_hash)
        serialize_text_element(result, 'taxNumber', self.tax_number)
        serialize_text_element(result, 'requestSignature', request_signature)

        return result
