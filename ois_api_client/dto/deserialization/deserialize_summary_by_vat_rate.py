import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from .deserialize_vat_rate import deserialize_vat_rate
from .deserialize_vat_rate_gross_data import deserialize_vat_rate_gross_data
from .deserialize_vat_rate_net_data import deserialize_vat_rate_net_data
from .deserialize_vat_rate_vat_data import deserialize_vat_rate_vat_data
from ..SummaryByVatRate import SummaryByVatRate
from ...constants import NAMESPACE_DATA


def deserialize_summary_by_vat_rate(element: ET.Element) -> Union[SummaryByVatRate, None]:
    if element is None:
        return None

    result = SummaryByVatRate(
        vat_rate=deserialize_vat_rate(XR.find_child(element, 'vatRate', NAMESPACE_DATA)),
        vat_rate_net_data=deserialize_vat_rate_net_data(XR.find_child(element, 'vatRateNetData', NAMESPACE_DATA)),
        vat_rate_vat_data=deserialize_vat_rate_vat_data(XR.find_child(element, 'vatRateVatData', NAMESPACE_DATA)),
        vat_rate_gross_data=deserialize_vat_rate_gross_data(XR.find_child(element, 'vatRateGrossData', NAMESPACE_DATA))
    )

    return result
