import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from .deserialize_simple_address import deserialize_simple_address
from ..Address import Address
from ..DetailedAddress import DetailedAddress
from ...constants import NAMESPACE_DATA


def _deserialize_detailed_address(element: ET.Element) -> Union[DetailedAddress, None]:
    if element is None:
        return None

    result = DetailedAddress(
        postal_code=XR.get_child_text(element, 'postalCode', NAMESPACE_DATA),
        city=XR.get_child_text(element, 'city', NAMESPACE_DATA),
        street_name=XR.get_child_text(element, 'streetName', NAMESPACE_DATA),
        public_place_category=XR.get_child_text(element, 'publicPlaceCategory', NAMESPACE_DATA),
        country_code=XR.get_child_text(element, 'countryCode', NAMESPACE_DATA, 'HU'),
        region=XR.get_child_text(element, 'region', NAMESPACE_DATA),
        number=XR.get_child_text(element, 'number', NAMESPACE_DATA),
        building=XR.get_child_text(element, 'building', NAMESPACE_DATA),
        staircase=XR.get_child_text(element, 'staircase', NAMESPACE_DATA),
        floor=XR.get_child_text(element, 'floor', NAMESPACE_DATA),
        door=XR.get_child_text(element, 'door', NAMESPACE_DATA),
        lot_number=XR.get_child_text(element, 'lotNumber', NAMESPACE_DATA),
    )

    return result


def deserialize_address(element: ET.Element) -> Union[Address, None]:
    if element is None:
        return None

    simple_address = XR.find_child(element, 'simpleAddress', NAMESPACE_DATA)

    if simple_address is not None:
        return Address(deserialize_simple_address(simple_address))

    detailed_address = XR.find_child(element, 'detailedAddress', NAMESPACE_DATA)

    if detailed_address is not None:
        return Address(_deserialize_detailed_address(detailed_address))

    return None
