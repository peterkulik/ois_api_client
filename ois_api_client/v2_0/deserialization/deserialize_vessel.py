from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.Vessel import Vessel


def deserialize_vessel(element: ET.Element) -> Optional[Vessel]:
    if element is None:
        return None

    result = Vessel(
        length=XR.get_child_float(element, 'length', DATA),
        activity_referred=XR.get_child_bool(element, 'activityReferred', DATA),
        sailed_hours=XR.get_child_float(element, 'sailedHours', DATA),
    )

    return result
