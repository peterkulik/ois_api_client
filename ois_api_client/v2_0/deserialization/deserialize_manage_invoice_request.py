from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..namespaces import DATA
from ..dto.ManageInvoiceRequest import ManageInvoiceRequest
from .deserialize_basic_header import deserialize_basic_header
from .deserialize_invoice_operation_list import deserialize_invoice_operation_list
from .deserialize_software import deserialize_software
from .deserialize_user_header import deserialize_user_header


def deserialize_manage_invoice_request(element: ET.Element) -> Optional[ManageInvoiceRequest]:
    if element is None:
        return None

    result = ManageInvoiceRequest(
        header=deserialize_basic_header(
            XR.find_child(element, 'header', API)
        ),
        user=deserialize_user_header(
            XR.find_child(element, 'user', API)
        ),
        software=deserialize_software(
            XR.find_child(element, 'software', API)
        ),
        exchange_token=XR.get_child_text(element, 'exchangeToken', API),
        invoice_operations=deserialize_invoice_operation_list(
            XR.find_child(element, 'invoiceOperations', API)
        ),
    )

    return result
