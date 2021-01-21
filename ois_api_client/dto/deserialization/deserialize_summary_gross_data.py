import xml.etree.ElementTree as ET
from typing import Optional

from .XmlReader import XmlReader as XR
from ..SummaryGrossData import SummaryGrossData
from ...constants import NAMESPACE_DATA


def deserialize_summary_gross_data(element: ET.Element) -> Optional[SummaryGrossData]:
    if element is None:
        return None

    result = SummaryGrossData(
        invoice_gross_amount=XR.get_child_float(element, 'invoiceGrossAmount', NAMESPACE_DATA),
        invoice_gross_amount_huf=XR.get_child_float(element, 'invoiceGrossAmountHUF', NAMESPACE_DATA)
    )

    return result
