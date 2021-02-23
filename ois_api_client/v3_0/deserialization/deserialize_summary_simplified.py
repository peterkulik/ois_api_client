from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import BASE
from ..namespaces import DATA
from ..dto.SummarySimplified import SummarySimplified
from .deserialize_vat_rate import deserialize_vat_rate


def deserialize_summary_simplified(element: ET.Element) -> Optional[SummarySimplified]:
    if element is None:
        return None

    result = SummarySimplified(
        vat_rate=deserialize_vat_rate(
            XR.find_child(element, 'vatRate', DATA)
        ),
        vat_content_gross_amount=XR.get_child_float(element, 'vatContentGrossAmount', DATA),
        vat_content_gross_amount_huf=XR.get_child_float(element, 'vatContentGrossAmountHUF', DATA),
    )

    return result
