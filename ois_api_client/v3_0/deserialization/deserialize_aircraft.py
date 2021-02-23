from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.Aircraft import Aircraft


def deserialize_aircraft(element: ET.Element) -> Optional[Aircraft]:
    if element is None:
        return None

    result = Aircraft(
        take_off_weight=XR.get_child_float(element, 'takeOffWeight', DATA),
        air_cargo=XR.get_child_bool(element, 'airCargo', DATA),
        operation_hours=XR.get_child_float(element, 'operationHours', DATA),
    )

    return result
