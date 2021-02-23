from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.VatRateNetData import VatRateNetData


def deserialize_vat_rate_net_data(element: ET.Element) -> Optional[VatRateNetData]:
    if element is None:
        return None

    result = VatRateNetData(
        vat_rate_net_amount=XR.get_child_float(element, 'vatRateNetAmount', DATA),
        vat_rate_net_amount_huf=XR.get_child_float(element, 'vatRateNetAmountHUF', DATA),
    )

    return result
