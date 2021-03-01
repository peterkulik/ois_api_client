from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import BASE
from ..namespaces import COMMON
from ..namespaces import DATA
from ...deserialization.create_enum import create_enum
from ..dto.CustomerInfo import CustomerInfo
from ..dto.CustomerVatStatus import CustomerVatStatus
from .deserialize_address import deserialize_address
from .deserialize_customer_vat_data import deserialize_customer_vat_data


def deserialize_customer_info(element: ET.Element) -> Optional[CustomerInfo]:
    if element is None:
        return None

    result = CustomerInfo(
        customer_vat_status=create_enum(CustomerVatStatus, XR.get_child_text(element, 'customerVatStatus', DATA)),
        customer_vat_data=deserialize_customer_vat_data(
            XR.find_child(element, 'customerVatData', DATA)
        ),
        customer_name=XR.get_child_text(element, 'customerName', DATA),
        customer_address=deserialize_address(
            XR.find_child(element, 'customerAddress', DATA)
        ),
        customer_bank_account_number=XR.get_child_text(element, 'customerBankAccountNumber', DATA),
    )

    return result
