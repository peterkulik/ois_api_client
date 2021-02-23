from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import BASE
from ..dto.Address import Address
from .deserialize_detailed_address import deserialize_detailed_address
from .deserialize_simple_address import deserialize_simple_address


def deserialize_address(element: ET.Element) -> Optional[Address]:
    if element is None:
        return None

    result = Address(
        simple_address=deserialize_simple_address(
            XR.find_child(element, 'simpleAddress', BASE)
        ),
        detailed_address=deserialize_detailed_address(
            XR.find_child(element, 'detailedAddress', BASE)
        ),
    )

    return result
