from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import BASE
from ..namespaces import DATA
from ..namespaces import COMMON
from ..dto.InvoiceReference import InvoiceReference


def deserialize_invoice_reference(element: ET.Element) -> Optional[InvoiceReference]:
    if element is None:
        return None

    result = InvoiceReference(
        original_invoice_number=XR.get_child_text(element, 'originalInvoiceNumber', DATA),
        modify_without_master=XR.get_child_bool(element, 'modifyWithoutMaster', DATA),
        modification_index=XR.get_child_int(element, 'modificationIndex', DATA),
    )

    return result
