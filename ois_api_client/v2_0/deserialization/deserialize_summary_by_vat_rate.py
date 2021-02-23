from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.SummaryByVatRate import SummaryByVatRate
from .deserialize_vat_rate import deserialize_vat_rate
from .deserialize_vat_rate_gross_data import deserialize_vat_rate_gross_data
from .deserialize_vat_rate_net_data import deserialize_vat_rate_net_data
from .deserialize_vat_rate_vat_data import deserialize_vat_rate_vat_data


def deserialize_summary_by_vat_rate(element: ET.Element) -> Optional[SummaryByVatRate]:
    if element is None:
        return None

    result = SummaryByVatRate(
        vat_rate=deserialize_vat_rate(
            XR.find_child(element, 'vatRate', DATA)
        ),
        vat_rate_net_data=deserialize_vat_rate_net_data(
            XR.find_child(element, 'vatRateNetData', DATA)
        ),
        vat_rate_vat_data=deserialize_vat_rate_vat_data(
            XR.find_child(element, 'vatRateVatData', DATA)
        ),
        vat_rate_gross_data=deserialize_vat_rate_gross_data(
            XR.find_child(element, 'vatRateGrossData', DATA)
        ),
    )

    return result
