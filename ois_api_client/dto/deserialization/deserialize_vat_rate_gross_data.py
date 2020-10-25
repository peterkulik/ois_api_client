import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from ..VatRateGrossData import VatRateGrossData
from ...constants import NAMESPACE_DATA


def deserialize_vat_rate_gross_data(element: ET.Element) -> Union[VatRateGrossData, None]:
    if element is None:
        return None

    result = VatRateGrossData(
        vat_rate_gross_amount=XR.get_child_float(element, 'vatRateGrossAmount', NAMESPACE_DATA),
        vat_rate_gross_amount_huf=XR.get_child_float(element, 'vatRateGrossAmountHUF', NAMESPACE_DATA),
    )

    return result

