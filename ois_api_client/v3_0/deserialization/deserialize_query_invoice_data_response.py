from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..namespaces import API
from ..dto.QueryInvoiceDataResponse import QueryInvoiceDataResponse
from .deserialize_basic_header import deserialize_basic_header
from .deserialize_basic_result import deserialize_basic_result
from .deserialize_invoice_data_result import deserialize_invoice_data_result
from .deserialize_software import deserialize_software


def deserialize_query_invoice_data_response(element: ET.Element) -> Optional[QueryInvoiceDataResponse]:
    if element is None:
        return None

    result = QueryInvoiceDataResponse(
        header=deserialize_basic_header(
            XR.find_child(element, 'header', COMMON)
        ),
        result=deserialize_basic_result(
            XR.find_child(element, 'result', COMMON)
        ),
        software=deserialize_software(
            XR.find_child(element, 'software', API)
        ),
        invoice_data_result=deserialize_invoice_data_result(
            XR.find_child(element, 'invoiceDataResult', API)
        ),
    )

    return result
