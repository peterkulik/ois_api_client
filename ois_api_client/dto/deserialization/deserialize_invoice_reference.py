import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from ..InvoiceReference import InvoiceReference
from ...constants import NAMESPACE_DATA


def deserialize_invoice_reference(element: ET.Element) -> Union[InvoiceReference, None]:
    if element is None:
        return None

    result = InvoiceReference(
        original_invoice_number=XR.get_child_text(element, 'originalInvoiceNumber', NAMESPACE_DATA),
        modification_index=XR.get_child_int(element, 'modificationIndex', NAMESPACE_DATA),
        modify_without_master=XR.get_child_bool(element, 'modifyWithoutMaster', NAMESPACE_DATA, False)
    )

    return result
