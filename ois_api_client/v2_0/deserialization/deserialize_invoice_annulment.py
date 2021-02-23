from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import ANNUL
from ..namespaces import DATA
from ...deserialization.create_enum import create_enum
from ..dto.InvoiceAnnulment import InvoiceAnnulment
from ..dto.AnnulmentCode import AnnulmentCode


def deserialize_invoice_annulment(element: ET.Element) -> Optional[InvoiceAnnulment]:
    if element is None:
        return None

    result = InvoiceAnnulment(
        annulment_reference=XR.get_child_text(element, 'annulmentReference', ANNUL),
        annulment_timestamp=XR.get_child_datetime(element, 'annulmentTimestamp', ANNUL),
        annulment_code=create_enum(AnnulmentCode, XR.get_child_text(element, 'annulmentCode', ANNUL)),
        annulment_reason=XR.get_child_text(element, 'annulmentReason', ANNUL),
    )

    return result
