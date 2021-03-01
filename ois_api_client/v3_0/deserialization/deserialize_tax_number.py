from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import BASE
from ..namespaces import COMMON
from ..dto.TaxNumber import TaxNumber


def deserialize_tax_number(element: ET.Element) -> Optional[TaxNumber]:
    if element is None:
        return None

    result = TaxNumber(
        taxpayer_id=XR.get_child_text(element, 'taxpayerId', BASE),
        vat_code=XR.get_child_text(element, 'vatCode', BASE),
        county_code=XR.get_child_text(element, 'countyCode', BASE),
    )

    return result
