import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from ..LineAmountsSimplified import LineAmountsSimplified
from ...constants import NAMESPACE_DATA


def deserialize_line_amounts_simplified(element: ET.Element) -> Union[LineAmountsSimplified, None]:
    if element is None:
        return None

    result = LineAmountsSimplified(
        line_gross_amount_simplified=XR.get_child_float(element, 'lineGrossAmountSimplified', NAMESPACE_DATA),
        line_gross_amount_simplified_huf=XR.get_child_float(element, 'lineGrossAmountSimplifiedHUF', NAMESPACE_DATA),
        line_vat_content=XR.get_child_float(element, 'lineVatContent', NAMESPACE_DATA)
    )

    return result
