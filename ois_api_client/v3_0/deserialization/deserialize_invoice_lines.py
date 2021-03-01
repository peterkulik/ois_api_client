from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import BASE
from ..namespaces import API
from ..dto.InvoiceLines import InvoiceLines
from .deserialize_new_created_lines import deserialize_new_created_lines


def deserialize_invoice_lines(element: ET.Element) -> Optional[InvoiceLines]:
    if element is None:
        return None

    result = InvoiceLines(
        max_line_number=XR.get_child_int(element, 'maxLineNumber', API),
        new_created_lines=[deserialize_new_created_lines(e) for e in XR.find_all_child(element, 'newCreatedLines', API)],
    )

    return result
