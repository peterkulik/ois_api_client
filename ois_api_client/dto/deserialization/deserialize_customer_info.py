import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from .deserialize_address import deserialize_address
from .deserialize_tax_number import deserialize_tax_number
from ..CustomerInfo import CustomerInfo
from ...constants import NAMESPACE_DATA


def deserialize_customer_info(element: ET.Element) -> Union[CustomerInfo, None]:
    if element is None:
        return None

    result = CustomerInfo(
        customer_name=XR.get_child_text(element, 'customerName', NAMESPACE_DATA),
        customer_address=deserialize_address(XR.find_child(element, 'customerAddress', NAMESPACE_DATA)),
        customer_tax_number=deserialize_tax_number(XR.find_child(element, 'customerTaxNumber', NAMESPACE_DATA)),
        group_member_tax_number=deserialize_tax_number(XR.find_child(element, 'groupMemberTaxNumber', NAMESPACE_DATA)),
        community_vat_number=XR.get_child_text(element, 'communityVatNumber', NAMESPACE_DATA),
        third_state_tax_id=XR.get_child_text(element, 'thirdStateTaxId', NAMESPACE_DATA),
        customer_bank_account_number=XR.get_child_text(element, 'customerBankAccountNumber', NAMESPACE_DATA)
    )

    return result
