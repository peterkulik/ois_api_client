from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import BASE
from ..namespaces import COMMON
from ..namespaces import API
from ..dto.Pointer import Pointer


def deserialize_pointer(element: ET.Element) -> Optional[Pointer]:
    if element is None:
        return None

    result = Pointer(
        tag=XR.get_child_text(element, 'tag', API),
        value=XR.get_child_text(element, 'value', API),
        line=XR.get_child_int(element, 'line', API),
        original_invoice_number=XR.get_child_text(element, 'originalInvoiceNumber', API),
    )

    return result
