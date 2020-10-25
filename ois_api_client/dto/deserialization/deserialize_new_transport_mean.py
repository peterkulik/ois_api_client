import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from .deserialize_aircraft import deserialize_aircraft
from .deserialize_vehicle import deserialize_vehicle
from .deserialize_vessel import deserialize_vessel
from ..Aircraft import Aircraft
from ..NewTransportMean import NewTransportMean
from ..Vehicle import Vehicle
from ..Vessel import Vessel
from ...constants import NAMESPACE_DATA


def _get_data(element: ET.Element) -> Union[Vehicle, Vessel, Aircraft, None]:
    if element is None:
        return None

    vehicle = XR.find_child(element, 'vehicle', NAMESPACE_DATA)

    if vehicle is not None:
        return deserialize_vehicle(vehicle)

    vessel = XR.find_child(element, 'vessel', NAMESPACE_DATA)

    if vessel is not None:
        return deserialize_vessel(vessel)

    aircraft = XR.find_child(element, 'aircraft', NAMESPACE_DATA)

    if aircraft is not None:
        return deserialize_aircraft(aircraft)

    return None


def deserialize_new_transport_mean(element: ET.Element) -> Union[NewTransportMean, None]:
    if element is None:
        return None

    result = NewTransportMean(
        data=_get_data(element),
        brand=XR.get_child_text(element, 'brand', NAMESPACE_DATA),
        serial_num=XR.get_child_text(element, 'serialNum', NAMESPACE_DATA),
        engine_num=XR.get_child_text(element, 'engineNum', NAMESPACE_DATA),
        first_entry_into_service=XR.get_child_date(element, 'firstEntryIntoService', NAMESPACE_DATA)
    )

    return result
