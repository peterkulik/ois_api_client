from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.DetailedAddress import DetailedAddress


def deserialize_detailed_address(element: ET.Element) -> Optional[DetailedAddress]:
    if element is None:
        return None

    result = DetailedAddress(
        country_code=XR.get_child_text(element, 'countryCode', DATA),
        region=XR.get_child_text(element, 'region', DATA),
        postal_code=XR.get_child_text(element, 'postalCode', DATA),
        city=XR.get_child_text(element, 'city', DATA),
        street_name=XR.get_child_text(element, 'streetName', DATA),
        public_place_category=XR.get_child_text(element, 'publicPlaceCategory', DATA),
        number=XR.get_child_text(element, 'number', DATA),
        building=XR.get_child_text(element, 'building', DATA),
        staircase=XR.get_child_text(element, 'staircase', DATA),
        floor=XR.get_child_text(element, 'floor', DATA),
        door=XR.get_child_text(element, 'door', DATA),
        lot_number=XR.get_child_text(element, 'lotNumber', DATA),
    )

    return result
