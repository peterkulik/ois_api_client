from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..dto.InvoiceChainDigestResult import InvoiceChainDigestResult
from .deserialize_invoice_chain_element import deserialize_invoice_chain_element


def deserialize_invoice_chain_digest_result(element: ET.Element) -> Optional[InvoiceChainDigestResult]:
    if element is None:
        return None

    result = InvoiceChainDigestResult(
        current_page=XR.get_child_int(element, 'currentPage', API),
        available_page=XR.get_child_int(element, 'availablePage', API),
        invoice_chain_element=[deserialize_invoice_chain_element(e) for e in XR.find_all_child(element, 'invoiceChainElement', API)],
    )

    return result
