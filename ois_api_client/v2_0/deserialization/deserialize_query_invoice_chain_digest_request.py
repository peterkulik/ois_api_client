from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..dto.QueryInvoiceChainDigestRequest import QueryInvoiceChainDigestRequest
from .deserialize_basic_header import deserialize_basic_header
from .deserialize_invoice_chain_query import deserialize_invoice_chain_query
from .deserialize_software import deserialize_software
from .deserialize_user_header import deserialize_user_header


def deserialize_query_invoice_chain_digest_request(element: ET.Element) -> Optional[QueryInvoiceChainDigestRequest]:
    if element is None:
        return None

    result = QueryInvoiceChainDigestRequest(
        header=deserialize_basic_header(
            XR.find_child(element, 'header', API)
        ),
        user=deserialize_user_header(
            XR.find_child(element, 'user', API)
        ),
        software=deserialize_software(
            XR.find_child(element, 'software', API)
        ),
        page=XR.get_child_int(element, 'page', API),
        invoice_chain_query=deserialize_invoice_chain_query(
            XR.find_child(element, 'invoiceChainQuery', API)
        ),
    )

    return result
