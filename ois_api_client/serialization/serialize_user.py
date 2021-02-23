import xml.etree.ElementTree as ET

from ..v3_0 import dto, namespaces as ns
from .serialize_element import serialize_text_element
from ois_api_client.xml.get_full_tag import get_full_tag


# def serialize_user(data: dto.UserHeader, password_hash: str, request_signature: str) -> ET.Element:
def serialize_user(data: dto.UserHeader) -> ET.Element:
    result = ET.Element(get_full_tag(ns.COMMON, 'user'))

    serialize_text_element(result, 'login', data.login, ns.COMMON)
    serialize_text_element(result, 'passwordHash', data.password_hash.value, ns.COMMON,
                           {'cryptoType': data.password_hash.crypto_type})
    serialize_text_element(result, 'taxNumber', data.tax_number, ns.COMMON)
    serialize_text_element(result, 'requestSignature', data.request_signature.value, ns.COMMON,
                           {'cryptoType': data.request_signature.crypto_type})

    return result
