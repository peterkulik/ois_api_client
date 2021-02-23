from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..namespaces import API
from ..dto.QueryInvoiceCheckResponse import QueryInvoiceCheckResponse
from .deserialize_basic_header import deserialize_basic_header
from .deserialize_basic_result import deserialize_basic_result
from .deserialize_software import deserialize_software


def deserialize_query_invoice_check_response(element: ET.Element) -> Optional[QueryInvoiceCheckResponse]:
    if element is None:
        return None

    result = QueryInvoiceCheckResponse(
        header=deserialize_basic_header(
            XR.find_child(element, 'header', COMMON)
        ),
        result=deserialize_basic_result(
            XR.find_child(element, 'result', COMMON)
        ),
        software=deserialize_software(
            XR.find_child(element, 'software', API)
        ),
        invoice_check_result=XR.get_child_bool(element, 'invoiceCheckResult', API),
    )

    return result
