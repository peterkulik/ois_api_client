from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.SummaryGrossData import SummaryGrossData


def deserialize_summary_gross_data(element: ET.Element) -> Optional[SummaryGrossData]:
    if element is None:
        return None

    result = SummaryGrossData(
        invoice_gross_amount=XR.get_child_float(element, 'invoiceGrossAmount', DATA),
        invoice_gross_amount_huf=XR.get_child_float(element, 'invoiceGrossAmountHUF', DATA),
    )

    return result
