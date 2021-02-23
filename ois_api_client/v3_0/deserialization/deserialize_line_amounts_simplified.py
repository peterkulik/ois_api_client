from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import BASE
from ..namespaces import DATA
from ..dto.LineAmountsSimplified import LineAmountsSimplified
from .deserialize_vat_rate import deserialize_vat_rate


def deserialize_line_amounts_simplified(element: ET.Element) -> Optional[LineAmountsSimplified]:
    if element is None:
        return None

    result = LineAmountsSimplified(
        line_vat_rate=deserialize_vat_rate(
            XR.find_child(element, 'lineVatRate', DATA)
        ),
        line_gross_amount_simplified=XR.get_child_float(element, 'lineGrossAmountSimplified', DATA),
        line_gross_amount_simplified_huf=XR.get_child_float(element, 'lineGrossAmountSimplifiedHUF', DATA),
    )

    return result
