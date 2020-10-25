import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from ..LineNetAmountData import LineNetAmountData
from ...constants import NAMESPACE_DATA


def deserialize_line_net_amount_data(element: ET.Element) -> Union[LineNetAmountData, None]:
    if element is None:
        return None

    result = LineNetAmountData(
        line_net_amount=XR.get_child_float(element, 'lineNetAmount', NAMESPACE_DATA),
        line_net_amount_huf=XR.get_child_float(element, 'lineNetAmountHUF', NAMESPACE_DATA)
    )

    return result




