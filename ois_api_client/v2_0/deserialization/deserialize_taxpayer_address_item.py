from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..namespaces import DATA
from ...deserialization.create_enum import create_enum
from ..dto.TaxpayerAddressItem import TaxpayerAddressItem
from ..dto.TaxpayerAddressType import TaxpayerAddressType
from .deserialize_detailed_address import deserialize_detailed_address


def deserialize_taxpayer_address_item(element: ET.Element) -> Optional[TaxpayerAddressItem]:
    if element is None:
        return None

    result = TaxpayerAddressItem(
        taxpayer_address_type=create_enum(TaxpayerAddressType, XR.get_child_text(element, 'taxpayerAddressType', API)),
        taxpayer_address=deserialize_detailed_address(
            XR.find_child(element, 'taxpayerAddress', API)
        ),
    )

    return result
