from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.SimpleAddress import SimpleAddress


def deserialize_simple_address(element: ET.Element) -> Optional[SimpleAddress]:
    if element is None:
        return None

    result = SimpleAddress(
        country_code=XR.get_child_text(element, 'countryCode', DATA),
        region=XR.get_child_text(element, 'region', DATA),
        postal_code=XR.get_child_text(element, 'postalCode', DATA),
        city=XR.get_child_text(element, 'city', DATA),
        additional_address_detail=XR.get_child_text(element, 'additionalAddressDetail', DATA),
    )

    return result
