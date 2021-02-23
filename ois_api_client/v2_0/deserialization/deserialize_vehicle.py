from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.Vehicle import Vehicle


def deserialize_vehicle(element: ET.Element) -> Optional[Vehicle]:
    if element is None:
        return None

    result = Vehicle(
        engine_capacity=XR.get_child_float(element, 'engineCapacity', DATA),
        engine_power=XR.get_child_float(element, 'enginePower', DATA),
        kms=XR.get_child_float(element, 'kms', DATA),
    )

    return result
