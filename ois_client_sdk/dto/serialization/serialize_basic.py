import xml.etree.ElementTree as ET

from .serialize_header import serialize_header
from .serialize_user import serialize_user
from .serialize_software import serialize_software
from ...constants import NAMESPACE
from ..BasicRequest import BasicRequest


def serialize_basic(data: BasicRequest, root_element: str, request_signature: str, password_hash: str) -> ET.Element:
    root = ET.Element(f'{{{NAMESPACE}}}{root_element}')
    root.append(serialize_header(data.header))
    root.append(serialize_user(data.user, password_hash, request_signature))
    root.append(serialize_software(data.software))

    return root
