import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from ..SummarySimplified import SummarySimplified
from ...constants import NAMESPACE_DATA


def deserialize_summary_simplified(element: ET.Element) -> Union[SummarySimplified, None]:
    if element is None:
        return None

    result = SummarySimplified(
        vat_content=XR.get_child_float(element, 'vatContent', NAMESPACE_DATA),
        vat_content_gross_amount=XR.get_child_float(element, 'vatContentGrossAmount', NAMESPACE_DATA),
        vat_content_gross_amount_huf=XR.get_child_float(element, 'vatContentGrossAmountHUF', NAMESPACE_DATA)
    )

    return result
