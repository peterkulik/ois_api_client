from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..dto.InvoiceChainElement import InvoiceChainElement
from .deserialize_invoice_chain_digest import deserialize_invoice_chain_digest
from .deserialize_invoice_lines import deserialize_invoice_lines
from .deserialize_invoice_reference_data import deserialize_invoice_reference_data


def deserialize_invoice_chain_element(element: ET.Element) -> Optional[InvoiceChainElement]:
    if element is None:
        return None

    result = InvoiceChainElement(
        invoice_chain_digest=deserialize_invoice_chain_digest(
            XR.find_child(element, 'invoiceChainDigest', API)
        ),
        invoice_lines=deserialize_invoice_lines(
            XR.find_child(element, 'invoiceLines', API)
        ),
        invoice_reference_data=deserialize_invoice_reference_data(
            XR.find_child(element, 'invoiceReferenceData', API)
        ),
    )

    return result
