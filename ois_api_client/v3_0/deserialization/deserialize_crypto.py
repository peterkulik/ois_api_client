from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..dto.Crypto import Crypto


def deserialize_crypto(element: ET.Element) -> Optional[Crypto]:
    if element is None:
        return None

    result = Crypto(
        value=element.text,
        crypto_type=element.attrib['cryptoType']
    )

    return result
