import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from .deserialize_gross_amount_data import deserialize_gross_amount_data
from .deserialize_line_net_amount_data import deserialize_line_net_amount_data
from .deserialize_line_vat_data import deserialize_line_vat_data
from .deserialize_vat_rate import deserialize_vat_rate
from ..LineAmountsNormal import LineAmountsNormal
from ...constants import NAMESPACE_DATA


def deserialize_line_amounts_normal(element: ET.Element) -> Union[LineAmountsNormal, None]:
    if element is None:
        return None

    result = LineAmountsNormal(
        line_net_amount_data=deserialize_line_net_amount_data(
            XR.find_child(element, 'lineNetAmountData', NAMESPACE_DATA)),
        line_vat_rate=deserialize_vat_rate(XR.find_child(element, 'lineVatRate', NAMESPACE_DATA)),
        line_vat_data=deserialize_line_vat_data(XR.find_child(element, 'lineVatData', NAMESPACE_DATA)),
        line_gross_amount_data=deserialize_gross_amount_data(
            XR.find_child(element, 'lineGrossAmountData', NAMESPACE_DATA))
    )

    return result
