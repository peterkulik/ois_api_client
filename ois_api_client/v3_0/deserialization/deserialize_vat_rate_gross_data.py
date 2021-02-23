from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import BASE
from ..namespaces import DATA
from ..dto.VatRateGrossData import VatRateGrossData


def deserialize_vat_rate_gross_data(element: ET.Element) -> Optional[VatRateGrossData]:
    if element is None:
        return None

    result = VatRateGrossData(
        vat_rate_gross_amount=XR.get_child_float(element, 'vatRateGrossAmount', DATA),
        vat_rate_gross_amount_huf=XR.get_child_float(element, 'vatRateGrossAmountHUF', DATA),
    )

    return result
