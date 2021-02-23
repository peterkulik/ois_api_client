from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import BASE
from ..namespaces import DATA
from ..dto.LineNetAmountData import LineNetAmountData


def deserialize_line_net_amount_data(element: ET.Element) -> Optional[LineNetAmountData]:
    if element is None:
        return None

    result = LineNetAmountData(
        line_net_amount=XR.get_child_float(element, 'lineNetAmount', DATA),
        line_net_amount_huf=XR.get_child_float(element, 'lineNetAmountHUF', DATA),
    )

    return result
