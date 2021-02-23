from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.LineAmountsNormal import LineAmountsNormal
from .deserialize_line_gross_amount_data import deserialize_line_gross_amount_data
from .deserialize_line_net_amount_data import deserialize_line_net_amount_data
from .deserialize_line_vat_data import deserialize_line_vat_data
from .deserialize_vat_rate import deserialize_vat_rate


def deserialize_line_amounts_normal(element: ET.Element) -> Optional[LineAmountsNormal]:
    if element is None:
        return None

    result = LineAmountsNormal(
        line_net_amount_data=deserialize_line_net_amount_data(
            XR.find_child(element, 'lineNetAmountData', DATA)
        ),
        line_vat_rate=deserialize_vat_rate(
            XR.find_child(element, 'lineVatRate', DATA)
        ),
        line_vat_data=deserialize_line_vat_data(
            XR.find_child(element, 'lineVatData', DATA)
        ),
        line_gross_amount_data=deserialize_line_gross_amount_data(
            XR.find_child(element, 'lineGrossAmountData', DATA)
        ),
    )

    return result
