from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.Summary import Summary
from .deserialize_summary_gross_data import deserialize_summary_gross_data
from .deserialize_summary_normal import deserialize_summary_normal
from .deserialize_summary_simplified import deserialize_summary_simplified


def deserialize_summary(element: ET.Element) -> Optional[Summary]:
    if element is None:
        return None

    result = Summary(
        summary_normal=deserialize_summary_normal(
            XR.find_child(element, 'summaryNormal', DATA)
        ),
        summary_simplified=[deserialize_summary_simplified(e) for e in XR.find_all_child(element, 'summarySimplified', DATA)],
        summary_gross_data=deserialize_summary_gross_data(
            XR.find_child(element, 'summaryGrossData', DATA)
        ),
    )

    return result
