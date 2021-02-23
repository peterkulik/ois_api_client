from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..namespaces import DATA
from ..dto.DealerCodes import DealerCodes


def deserialize_dealer_codes(element: ET.Element) -> Optional[DealerCodes]:
    if element is None:
        return None

    result = DealerCodes(
        dealer_code=[e.text for e in XR.find_all_child(element, 'dealerCode', DATA)],
    )

    return result
