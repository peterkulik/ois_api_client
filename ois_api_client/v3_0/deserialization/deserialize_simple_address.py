from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import BASE
from ..namespaces import COMMON
from ..dto.SimpleAddress import SimpleAddress


def deserialize_simple_address(element: ET.Element) -> Optional[SimpleAddress]:
    if element is None:
        return None

    result = SimpleAddress(
        country_code=XR.get_child_text(element, 'countryCode', BASE),
        region=XR.get_child_text(element, 'region', BASE),
        postal_code=XR.get_child_text(element, 'postalCode', BASE),
        city=XR.get_child_text(element, 'city', BASE),
        additional_address_detail=XR.get_child_text(element, 'additionalAddressDetail', BASE),
    )

    return result
