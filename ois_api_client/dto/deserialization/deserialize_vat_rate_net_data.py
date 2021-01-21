import xml.etree.ElementTree as ET
from typing import Optional

from .XmlReader import XmlReader as XR
from ..VatRateNetData import VatRateNetData
from ...constants import NAMESPACE_DATA


def deserialize_vat_rate_net_data(element: ET.Element) -> Optional[VatRateNetData]:
    if element is None:
        return None

    result = VatRateNetData(
        vat_rate_net_amount=XR.get_child_float(element, 'vatRateNetAmount', NAMESPACE_DATA),
        vat_rate_net_amount_huf=XR.get_child_float(element, 'vatRateNetAmountHUF', NAMESPACE_DATA),
    )

    return result
