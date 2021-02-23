from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..namespaces import DATA
from ...deserialization.create_enum import create_enum
from ..dto.InvoiceChainQuery import InvoiceChainQuery
from ..dto.InvoiceDirection import InvoiceDirection


def deserialize_invoice_chain_query(element: ET.Element) -> Optional[InvoiceChainQuery]:
    if element is None:
        return None

    result = InvoiceChainQuery(
        invoice_number=XR.get_child_text(element, 'invoiceNumber', API),
        invoice_direction=create_enum(InvoiceDirection, XR.get_child_text(element, 'invoiceDirection', API)),
        tax_number=XR.get_child_text(element, 'taxNumber', API),
    )

    return result
