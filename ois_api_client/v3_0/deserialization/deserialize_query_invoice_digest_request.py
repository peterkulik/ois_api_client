from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..namespaces import API
from ...deserialization.create_enum import create_enum
from ..dto.QueryInvoiceDigestRequest import QueryInvoiceDigestRequest
from ..dto.InvoiceDirection import InvoiceDirection
from .deserialize_basic_header import deserialize_basic_header
from .deserialize_invoice_query_params import deserialize_invoice_query_params
from .deserialize_software import deserialize_software
from .deserialize_user_header import deserialize_user_header


def deserialize_query_invoice_digest_request(element: ET.Element) -> Optional[QueryInvoiceDigestRequest]:
    if element is None:
        return None

    result = QueryInvoiceDigestRequest(
        header=deserialize_basic_header(
            XR.find_child(element, 'header', COMMON)
        ),
        user=deserialize_user_header(
            XR.find_child(element, 'user', COMMON)
        ),
        software=deserialize_software(
            XR.find_child(element, 'software', API)
        ),
        page=XR.get_child_int(element, 'page', API),
        invoice_direction=create_enum(InvoiceDirection, XR.get_child_text(element, 'invoiceDirection', API)),
        invoice_query_params=deserialize_invoice_query_params(
            XR.find_child(element, 'invoiceQueryParams', API)
        ),
    )

    return result
