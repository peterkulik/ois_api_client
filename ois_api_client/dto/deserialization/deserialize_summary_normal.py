import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from .deserialize_summary_by_vat_rate import deserialize_summary_by_vat_rate
from ..SummaryNormal import SummaryNormal
from ...constants import NAMESPACE_DATA


def deserialize_summary_normal(element: ET.Element) -> Union[SummaryNormal, None]:
    if element is None:
        return None

    result = SummaryNormal(
        summary_by_vat_rate=[deserialize_summary_by_vat_rate(el) for el in
                             XR.find_all_child(element, 'summaryByVatRate', NAMESPACE_DATA)],
        invoice_net_amount=XR.get_child_float(element, 'invoiceNetAmount', NAMESPACE_DATA),
        invoice_net_amount_huf=XR.get_child_float(element, 'invoiceNetAmountHUF', NAMESPACE_DATA),
        invoice_vat_amount=XR.get_child_float(element, 'invoiceVatAmount', NAMESPACE_DATA),
        invoice_vat_amount_huf=XR.get_child_float(element, 'invoiceVatAmountHUF', NAMESPACE_DATA)
    )

    return result
