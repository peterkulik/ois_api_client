from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import BASE
from ..namespaces import COMMON
from ..namespaces import API
from ..dto.InvoiceReferenceData import InvoiceReferenceData


def deserialize_invoice_reference_data(element: ET.Element) -> Optional[InvoiceReferenceData]:
    if element is None:
        return None

    result = InvoiceReferenceData(
        original_invoice_number=XR.get_child_text(element, 'originalInvoiceNumber', API),
        modify_without_master=XR.get_child_bool(element, 'modifyWithoutMaster', API),
        modification_timestamp=XR.get_child_datetime(element, 'modificationTimestamp', API),
        modification_index=XR.get_child_int(element, 'modificationIndex', API),
    )

    return result
