from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.VatRateVatData import VatRateVatData


def deserialize_vat_rate_vat_data(element: ET.Element) -> Optional[VatRateVatData]:
    if element is None:
        return None

    result = VatRateVatData(
        vat_rate_vat_amount=XR.get_child_float(element, 'vatRateVatAmount', DATA),
        vat_rate_vat_amount_huf=XR.get_child_float(element, 'vatRateVatAmountHUF', DATA),
    )

    return result
