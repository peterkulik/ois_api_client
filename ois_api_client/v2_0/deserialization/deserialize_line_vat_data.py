from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.LineVatData import LineVatData


def deserialize_line_vat_data(element: ET.Element) -> Optional[LineVatData]:
    if element is None:
        return None

    result = LineVatData(
        line_vat_amount=XR.get_child_float(element, 'lineVatAmount', DATA),
        line_vat_amount_huf=XR.get_child_float(element, 'lineVatAmountHUF', DATA),
    )

    return result
