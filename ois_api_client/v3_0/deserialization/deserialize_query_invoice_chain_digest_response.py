from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..namespaces import API
from ..dto.QueryInvoiceChainDigestResponse import QueryInvoiceChainDigestResponse
from .deserialize_basic_header import deserialize_basic_header
from .deserialize_basic_result import deserialize_basic_result
from .deserialize_invoice_chain_digest_result import deserialize_invoice_chain_digest_result
from .deserialize_software import deserialize_software


def deserialize_query_invoice_chain_digest_response(element: ET.Element) -> Optional[QueryInvoiceChainDigestResponse]:
    if element is None:
        return None

    result = QueryInvoiceChainDigestResponse(
        header=deserialize_basic_header(
            XR.find_child(element, 'header', COMMON)
        ),
        result=deserialize_basic_result(
            XR.find_child(element, 'result', COMMON)
        ),
        software=deserialize_software(
            XR.find_child(element, 'software', API)
        ),
        invoice_chain_digest_result=deserialize_invoice_chain_digest_result(
            XR.find_child(element, 'invoiceChainDigestResult', API)
        ),
    )

    return result
