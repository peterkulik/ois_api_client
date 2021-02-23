from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..dto.UserHeader import UserHeader
from .deserialize_crypto import deserialize_crypto


def deserialize_user_header(element: ET.Element) -> Optional[UserHeader]:
    if element is None:
        return None

    result = UserHeader(
        login=XR.get_child_text(element, 'login', COMMON),
        password_hash=deserialize_crypto(
            XR.find_child(element, 'passwordHash', COMMON)
        ),
        tax_number=XR.get_child_text(element, 'taxNumber', COMMON),
        request_signature=deserialize_crypto(
            XR.find_child(element, 'requestSignature', COMMON)
        ),
    )

    return result
