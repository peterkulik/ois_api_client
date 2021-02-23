from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..namespaces import DATA
from ...deserialization.create_enum import create_enum
from ..dto.InvoiceNumberQuery import InvoiceNumberQuery
from ..dto.InvoiceDirection import InvoiceDirection


def deserialize_invoice_number_query(element: ET.Element) -> Optional[InvoiceNumberQuery]:
    if element is None:
        return None

    result = InvoiceNumberQuery(
        invoice_number=XR.get_child_text(element, 'invoiceNumber', API),
        invoice_direction=create_enum(InvoiceDirection, XR.get_child_text(element, 'invoiceDirection', API)),
        batch_index=XR.get_child_int(element, 'batchIndex', API),
        supplier_tax_number=XR.get_child_text(element, 'supplierTaxNumber', API),
    )

    return result
