import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from ..LineVatData import LineVatData
from ...constants import NAMESPACE_DATA


def deserialize_line_vat_data(element: ET.Element) -> Union[LineVatData, None]:
    if element is None:
        return None

    result = LineVatData(
        line_vat_amount=XR.get_child_float(element, 'lineVatAmount', NAMESPACE_DATA),
        line_vat_amount_huf=XR.get_child_float(element, 'lineVatAmountHUF', NAMESPACE_DATA)
    )

    return result


