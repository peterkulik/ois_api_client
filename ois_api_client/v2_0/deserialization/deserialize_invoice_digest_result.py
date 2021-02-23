from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..dto.InvoiceDigestResult import InvoiceDigestResult
from .deserialize_invoice_digest import deserialize_invoice_digest


def deserialize_invoice_digest_result(element: ET.Element) -> Optional[InvoiceDigestResult]:
    if element is None:
        return None

    result = InvoiceDigestResult(
        current_page=XR.get_child_int(element, 'currentPage', API),
        available_page=XR.get_child_int(element, 'availablePage', API),
        invoice_digest=[deserialize_invoice_digest(e) for e in XR.find_all_child(element, 'invoiceDigest', API)],
    )

    return result
