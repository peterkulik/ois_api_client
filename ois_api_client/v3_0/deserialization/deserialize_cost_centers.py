from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..namespaces import DATA
from ..dto.CostCenters import CostCenters


def deserialize_cost_centers(element: ET.Element) -> Optional[CostCenters]:
    if element is None:
        return None

    result = CostCenters(
        cost_center=[e.text for e in XR.find_all_child(element, 'costCenter', DATA)],
    )

    return result
