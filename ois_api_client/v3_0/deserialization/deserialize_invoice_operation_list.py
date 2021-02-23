from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..dto.InvoiceOperationList import InvoiceOperationList
from .deserialize_invoice_operation import deserialize_invoice_operation


def deserialize_invoice_operation_list(element: ET.Element) -> Optional[InvoiceOperationList]:
    if element is None:
        return None

    result = InvoiceOperationList(
        compressed_content=XR.get_child_bool(element, 'compressedContent', API),
        invoice_operation=[deserialize_invoice_operation(e) for e in XR.find_all_child(element, 'invoiceOperation', API)],
    )

    return result
