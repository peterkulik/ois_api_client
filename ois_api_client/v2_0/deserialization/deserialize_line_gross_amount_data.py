from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.LineGrossAmountData import LineGrossAmountData


def deserialize_line_gross_amount_data(element: ET.Element) -> Optional[LineGrossAmountData]:
    if element is None:
        return None

    result = LineGrossAmountData(
        line_gross_amount_normal=XR.get_child_float(element, 'lineGrossAmountNormal', DATA),
        line_gross_amount_normal_huf=XR.get_child_float(element, 'lineGrossAmountNormalHUF', DATA),
    )

    return result
