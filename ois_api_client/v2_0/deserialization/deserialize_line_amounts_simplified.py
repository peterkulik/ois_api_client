from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.LineAmountsSimplified import LineAmountsSimplified


def deserialize_line_amounts_simplified(element: ET.Element) -> Optional[LineAmountsSimplified]:
    if element is None:
        return None

    result = LineAmountsSimplified(
        line_vat_content=XR.get_child_float(element, 'lineVatContent', DATA),
        line_gross_amount_simplified=XR.get_child_float(element, 'lineGrossAmountSimplified', DATA),
        line_gross_amount_simplified_huf=XR.get_child_float(element, 'lineGrossAmountSimplifiedHUF', DATA),
    )

    return result
