from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..namespaces import DATA
from ...deserialization.create_enum import create_enum
from ..dto.InvoiceOperation import InvoiceOperation
from ..dto.ManageInvoiceOperation import ManageInvoiceOperation


def deserialize_invoice_operation(element: ET.Element) -> Optional[InvoiceOperation]:
    if element is None:
        return None

    result = InvoiceOperation(
        index=XR.get_child_int(element, 'index', API),
        invoice_operation=create_enum(ManageInvoiceOperation, XR.get_child_text(element, 'invoiceOperation', API)),
        invoice_data=XR.get_child_text(element, 'invoiceData', API),
    )

    return result
