from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..namespaces import DATA
from ..dto.CustomerVatData import CustomerVatData
from .deserialize_customer_tax_number import deserialize_customer_tax_number


def deserialize_customer_vat_data(element: ET.Element) -> Optional[CustomerVatData]:
    if element is None:
        return None

    result = CustomerVatData(
        customer_tax_number=deserialize_customer_tax_number(
            XR.find_child(element, 'customerTaxNumber', DATA)
        ),
        community_vat_number=XR.get_child_text(element, 'communityVatNumber', DATA),
        third_state_tax_id=XR.get_child_text(element, 'thirdStateTaxId', DATA),
    )

    return result
