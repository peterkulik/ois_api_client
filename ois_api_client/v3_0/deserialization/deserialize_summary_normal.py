from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import BASE
from ..namespaces import DATA
from ..dto.SummaryNormal import SummaryNormal
from .deserialize_summary_by_vat_rate import deserialize_summary_by_vat_rate


def deserialize_summary_normal(element: ET.Element) -> Optional[SummaryNormal]:
    if element is None:
        return None

    result = SummaryNormal(
        summary_by_vat_rate=[deserialize_summary_by_vat_rate(e) for e in XR.find_all_child(element, 'summaryByVatRate', DATA)],
        invoice_net_amount=XR.get_child_float(element, 'invoiceNetAmount', DATA),
        invoice_net_amount_huf=XR.get_child_float(element, 'invoiceNetAmountHUF', DATA),
        invoice_vat_amount=XR.get_child_float(element, 'invoiceVatAmount', DATA),
        invoice_vat_amount_huf=XR.get_child_float(element, 'invoiceVatAmountHUF', DATA),
    )

    return result
