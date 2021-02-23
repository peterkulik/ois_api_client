from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.CustomerInfo import CustomerInfo
from .deserialize_address import deserialize_address
from .deserialize_tax_number import deserialize_tax_number


def deserialize_customer_info(element: ET.Element) -> Optional[CustomerInfo]:
    if element is None:
        return None

    result = CustomerInfo(
        customer_tax_number=deserialize_tax_number(
            XR.find_child(element, 'customerTaxNumber', DATA)
        ),
        group_member_tax_number=deserialize_tax_number(
            XR.find_child(element, 'groupMemberTaxNumber', DATA)
        ),
        community_vat_number=XR.get_child_text(element, 'communityVatNumber', DATA),
        third_state_tax_id=XR.get_child_text(element, 'thirdStateTaxId', DATA),
        customer_name=XR.get_child_text(element, 'customerName', DATA),
        customer_address=deserialize_address(
            XR.find_child(element, 'customerAddress', DATA)
        ),
        customer_bank_account_number=XR.get_child_text(element, 'customerBankAccountNumber', DATA),
    )

    return result
