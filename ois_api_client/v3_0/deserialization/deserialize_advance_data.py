from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.AdvanceData import AdvanceData
from .deserialize_advance_payment_data import deserialize_advance_payment_data


def deserialize_advance_data(element: ET.Element) -> Optional[AdvanceData]:
    if element is None:
        return None

    result = AdvanceData(
        advance_indicator=XR.get_child_bool(element, 'advanceIndicator', DATA),
        advance_payment_data=deserialize_advance_payment_data(
            XR.find_child(element, 'advancePaymentData', DATA)
        ),
    )

    return result
