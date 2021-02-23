from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..namespaces import API
from ..dto.QueryInvoiceDigestResponse import QueryInvoiceDigestResponse
from .deserialize_basic_header import deserialize_basic_header
from .deserialize_basic_result import deserialize_basic_result
from .deserialize_invoice_digest_result import deserialize_invoice_digest_result
from .deserialize_software import deserialize_software


def deserialize_query_invoice_digest_response(element: ET.Element) -> Optional[QueryInvoiceDigestResponse]:
    if element is None:
        return None

    result = QueryInvoiceDigestResponse(
        header=deserialize_basic_header(
            XR.find_child(element, 'header', COMMON)
        ),
        result=deserialize_basic_result(
            XR.find_child(element, 'result', COMMON)
        ),
        software=deserialize_software(
            XR.find_child(element, 'software', API)
        ),
        invoice_digest_result=deserialize_invoice_digest_result(
            XR.find_child(element, 'invoiceDigestResult', API)
        ),
    )

    return result
