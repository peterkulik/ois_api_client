from typing import Union
from xml.etree import ElementTree as ET

from ois_api_client.constants import NAMESPACE_DATA
from ois_api_client.dto.SimpleAddress import SimpleAddress
from ois_api_client.dto.deserialization.XmlReader import XmlReader as XR


def deserialize_simple_address(element: ET.Element) -> Union[SimpleAddress, None]:
    if element is None:
        return None

    result = SimpleAddress(
        postal_code=XR.get_child_text(element, 'postalCode', NAMESPACE_DATA),
        city=XR.get_child_text(element, 'city', NAMESPACE_DATA),
        additional_address_detail=XR.get_child_text(element, 'additionalAddressDetail', NAMESPACE_DATA),
        country_code=XR.get_child_text(element, 'countryCode', NAMESPACE_DATA, 'HU'),
        region=XR.get_child_text(element, 'region', NAMESPACE_DATA)
    )

    return result