from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..namespaces import API
from ..dto.QueryInvoiceDataRequest import QueryInvoiceDataRequest
from .deserialize_basic_header import deserialize_basic_header
from .deserialize_invoice_number_query import deserialize_invoice_number_query
from .deserialize_software import deserialize_software
from .deserialize_user_header import deserialize_user_header


def deserialize_query_invoice_data_request(element: ET.Element) -> Optional[QueryInvoiceDataRequest]:
    if element is None:
        return None

    result = QueryInvoiceDataRequest(
        header=deserialize_basic_header(
            XR.find_child(element, 'header', COMMON)
        ),
        user=deserialize_user_header(
            XR.find_child(element, 'user', COMMON)
        ),
        software=deserialize_software(
            XR.find_child(element, 'software', API)
        ),
        invoice_number_query=deserialize_invoice_number_query(
            XR.find_child(element, 'invoiceNumberQuery', API)
        ),
    )

    return result
