import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from ..TaxNumber import TaxNumber
from ...constants import NAMESPACE_DATA


def deserialize_tax_number(element: ET.Element) -> Union[TaxNumber, None]:
    if element is None:
        return None

    result = TaxNumber(
        taxpayer_id=XR.get_child_text(element, 'taxpayerId', NAMESPACE_DATA),
        vat_code=XR.get_child_text(element, 'vatCode', NAMESPACE_DATA),
        county_code=XR.get_child_text(element, 'countyCode', NAMESPACE_DATA)
    )

    return result
