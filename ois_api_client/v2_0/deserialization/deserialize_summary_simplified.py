from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.SummarySimplified import SummarySimplified


def deserialize_summary_simplified(element: ET.Element) -> Optional[SummarySimplified]:
    if element is None:
        return None

    result = SummarySimplified(
        vat_content=XR.get_child_float(element, 'vatContent', DATA),
        vat_content_gross_amount=XR.get_child_float(element, 'vatContentGrossAmount', DATA),
        vat_content_gross_amount_huf=XR.get_child_float(element, 'vatContentGrossAmountHUF', DATA),
    )

    return result
