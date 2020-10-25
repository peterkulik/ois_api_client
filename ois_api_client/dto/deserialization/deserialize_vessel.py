import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from ..Vessel import Vessel
from ...constants import NAMESPACE_DATA


def deserialize_vessel(element: ET.Element) -> Union[Vessel, None]:
    if element is None:
        return None

    result = Vessel(
        length=XR.get_child_float(element, 'length', NAMESPACE_DATA),
        sailed_hours=XR.get_child_float(element, 'sailedHours', NAMESPACE_DATA),
        activity_referred=XR.get_child_bool(element, 'activityReferred', NAMESPACE_DATA, False)
    )

    return result
