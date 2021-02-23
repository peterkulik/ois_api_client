from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..namespaces import DATA
from ..dto.UserHeader import UserHeader


def deserialize_user_header(element: ET.Element) -> Optional[UserHeader]:
    if element is None:
        return None

    result = UserHeader(
        login=XR.get_child_text(element, 'login', API),
        password_hash=XR.get_child_text(element, 'passwordHash', API),
        tax_number=XR.get_child_text(element, 'taxNumber', API),
        request_signature=XR.get_child_text(element, 'requestSignature', API),
    )

    return result
