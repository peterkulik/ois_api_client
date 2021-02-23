from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..dto.TaxpayerAddressList import TaxpayerAddressList
from .deserialize_taxpayer_address_item import deserialize_taxpayer_address_item


def deserialize_taxpayer_address_list(element: ET.Element) -> Optional[TaxpayerAddressList]:
    if element is None:
        return None

    result = TaxpayerAddressList(
        taxpayer_address_item=[deserialize_taxpayer_address_item(e) for e in XR.find_all_child(element, 'taxpayerAddressItem', API)],
    )

    return result
