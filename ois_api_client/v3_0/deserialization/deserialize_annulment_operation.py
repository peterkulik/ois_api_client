from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import BASE
from ..namespaces import API
from ...deserialization.create_enum import create_enum
from ..dto.AnnulmentOperation import AnnulmentOperation
from ..dto.ManageAnnulmentOperation import ManageAnnulmentOperation


def deserialize_annulment_operation(element: ET.Element) -> Optional[AnnulmentOperation]:
    if element is None:
        return None

    result = AnnulmentOperation(
        index=XR.get_child_int(element, 'index', API),
        annulment_operation=create_enum(ManageAnnulmentOperation, XR.get_child_text(element, 'annulmentOperation', API)),
        invoice_annulment=XR.get_child_text(element, 'invoiceAnnulment', API),
    )

    return result
