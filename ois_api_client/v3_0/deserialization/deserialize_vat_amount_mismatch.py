from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..namespaces import DATA
from ..dto.VatAmountMismatch import VatAmountMismatch


def deserialize_vat_amount_mismatch(element: ET.Element) -> Optional[VatAmountMismatch]:
    if element is None:
        return None

    result = VatAmountMismatch(
        vat_rate=XR.get_child_float(element, 'vatRate', DATA),
        case=XR.get_child_text(element, 'case', DATA),
    )

    return result
