import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from ..Aircraft import Aircraft
from ...constants import NAMESPACE_DATA


def deserialize_aircraft(element: ET.Element) -> Union[Aircraft, None]:
    if element is None:
        return None

    result = Aircraft(
        take_off_weight=XR.get_child_float(element, 'takeOffWeight', NAMESPACE_DATA),
        air_cargo=XR.get_child_bool(element, 'airCargo', NAMESPACE_DATA, False),
        operation_hours=XR.get_child_float(element, 'operationHours', NAMESPACE_DATA)
    )

    return result
