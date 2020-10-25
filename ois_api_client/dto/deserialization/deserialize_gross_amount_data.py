import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from ..LineGrossAmountData import LineGrossAmountData
from ...constants import NAMESPACE_DATA


def deserialize_gross_amount_data(element: ET.Element) -> Union[LineGrossAmountData, None]:
    if element is None:
        return None

    result = LineGrossAmountData(
        line_gross_amount_normal=XR.get_child_float(element, 'lineGrossAmountNormal', NAMESPACE_DATA),
        line_gross_amount_normal_huf=XR.get_child_float(element, 'lineGrossAmountNormalHUF', NAMESPACE_DATA)
    )

    return result
