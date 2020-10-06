import xml.etree.ElementTree as ET

from ..User import User
from .serialize_text_element import serialize_text_element


def serialize_user(data: User, password_hash: str, request_signature: str) -> ET.Element:
    result = ET.Element('user')

    serialize_text_element(result, 'login', data.login)
    serialize_text_element(result, 'passwordHash', password_hash)
    serialize_text_element(result, 'taxNumber', data.tax_number)
    serialize_text_element(result, 'requestSignature', request_signature)

    return result
