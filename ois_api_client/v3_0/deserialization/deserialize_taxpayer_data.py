from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import BASE
from ..namespaces import COMMON
from ..namespaces import API
from ...deserialization.create_enum import create_enum
from ..dto.TaxpayerData import TaxpayerData
from ..dto.Incorporation import Incorporation
from .deserialize_tax_number import deserialize_tax_number
from .deserialize_taxpayer_address_list import deserialize_taxpayer_address_list


def deserialize_taxpayer_data(element: ET.Element) -> Optional[TaxpayerData]:
    if element is None:
        return None

    result = TaxpayerData(
        taxpayer_name=XR.get_child_text(element, 'taxpayerName', API),
        taxpayer_short_name=XR.get_child_text(element, 'taxpayerShortName', API),
        tax_number_detail=deserialize_tax_number(
            XR.find_child(element, 'taxNumberDetail', API)
        ),
        incorporation=create_enum(Incorporation, XR.get_child_text(element, 'incorporation', API)),
        vat_group_membership=XR.get_child_text(element, 'vatGroupMembership', API),
        taxpayer_address_list=deserialize_taxpayer_address_list(
            XR.find_child(element, 'taxpayerAddressList', API)
        ),
    )

    return result
