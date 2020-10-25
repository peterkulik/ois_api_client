import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from ..Vehicle import Vehicle
from ...constants import NAMESPACE_DATA


def deserialize_vehicle(element: ET.Element) -> Union[Vehicle, None]:
    if element is None:
        return None

    result = Vehicle(
        engine_capacity=XR.get_child_float(element, 'engineCapacity', NAMESPACE_DATA),
        engine_power=XR.get_child_float(element, 'enginePower', NAMESPACE_DATA),
        kms=XR.get_child_float(element, 'kms', NAMESPACE_DATA)
    )

    return result



