from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import BASE
from ..namespaces import COMMON
from ..dto.DetailedAddress import DetailedAddress


def deserialize_detailed_address(element: ET.Element) -> Optional[DetailedAddress]:
    if element is None:
        return None

    result = DetailedAddress(
        country_code=XR.get_child_text(element, 'countryCode', BASE),
        region=XR.get_child_text(element, 'region', BASE),
        postal_code=XR.get_child_text(element, 'postalCode', BASE),
        city=XR.get_child_text(element, 'city', BASE),
        street_name=XR.get_child_text(element, 'streetName', BASE),
        public_place_category=XR.get_child_text(element, 'publicPlaceCategory', BASE),
        number=XR.get_child_text(element, 'number', BASE),
        building=XR.get_child_text(element, 'building', BASE),
        staircase=XR.get_child_text(element, 'staircase', BASE),
        floor=XR.get_child_text(element, 'floor', BASE),
        door=XR.get_child_text(element, 'door', BASE),
        lot_number=XR.get_child_text(element, 'lotNumber', BASE),
    )

    return result
