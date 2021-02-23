from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..namespaces import BASE
from ..namespaces import DATA
from ..dto.CustomerTaxNumber import CustomerTaxNumber
from .deserialize_tax_number import deserialize_tax_number


def deserialize_customer_tax_number(element: ET.Element) -> Optional[CustomerTaxNumber]:
    if element is None:
        return None

    result = CustomerTaxNumber(
        taxpayer_id=XR.get_child_text(element, 'taxpayerId', DATA),
        vat_code=XR.get_child_text(element, 'vatCode', DATA),
        county_code=XR.get_child_text(element, 'countyCode', DATA),
        group_member_tax_number=deserialize_tax_number(
            XR.find_child(element, 'groupMemberTaxNumber', BASE)
        ),
    )

    return result
