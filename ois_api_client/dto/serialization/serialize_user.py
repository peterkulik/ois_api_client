import xml.etree.ElementTree as ET

from ..UserHeader import UserHeader
from .serialize_element import serialize_text_element
from ..xml.get_full_tag import get_full_tag
from ...constants import NAMESPACE_COMMON


def serialize_user(data: UserHeader, password_hash: str, request_signature: str) -> ET.Element:
    result = ET.Element(get_full_tag(NAMESPACE_COMMON, 'user'))

    serialize_text_element(result, 'login', data.login, NAMESPACE_COMMON)
    serialize_text_element(result, 'passwordHash', password_hash, NAMESPACE_COMMON, {'cryptoType': 'SHA-512'})
    serialize_text_element(result, 'taxNumber', data.tax_number, NAMESPACE_COMMON)
    serialize_text_element(result, 'requestSignature', request_signature, NAMESPACE_COMMON, {'cryptoType': 'SHA3-512'})

    return result
