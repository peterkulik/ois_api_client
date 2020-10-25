import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from ..VatRateVatData import VatRateVatData
from ...constants import NAMESPACE_DATA


def deserialize_vat_rate_vat_data(element: ET.Element) -> Union[VatRateVatData, None]:
    if element is None:
        return None

    result = VatRateVatData(
        vat_rate_vat_amount=XR.get_child_float(element, 'vatRateVatAmount', NAMESPACE_DATA),
        vat_rate_vat_amount_huf=XR.get_child_float(element, 'vatRateVatAmountHUF', NAMESPACE_DATA),
    )

    return result
