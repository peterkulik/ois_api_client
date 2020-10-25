import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from .deserialize_summary_gross_data import deserialize_summary_gross_data
from .deserialize_summary_normal import deserialize_summary_normal
from ..Summary import Summary
from ..SummarySimplified import SummarySimplified
from ...constants import NAMESPACE_DATA


def deserialize_invoice_summary(element: ET.Element) -> Union[Summary, None]:
    if element is None:
        return None

    summary_normal_el = XR.find_child(element, 'summaryNormal', NAMESPACE_DATA)

    if summary_normal_el is not None:
        data = deserialize_summary_normal(summary_normal_el)
    else:
        summary_simplified_el_list = XR.find_all_child(element, 'summarySimplified', NAMESPACE_DATA)
        data = [SummarySimplified(summary_simplified_el) for summary_simplified_el in summary_simplified_el_list]

    result = Summary(
        data=data,
        summary_gross_data=deserialize_summary_gross_data(XR.find_child(element, 'summaryGrossData', NAMESPACE_DATA))
    )

    return result
