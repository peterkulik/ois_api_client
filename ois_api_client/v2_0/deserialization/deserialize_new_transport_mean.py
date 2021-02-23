from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.NewTransportMean import NewTransportMean
from .deserialize_aircraft import deserialize_aircraft
from .deserialize_vehicle import deserialize_vehicle
from .deserialize_vessel import deserialize_vessel


def deserialize_new_transport_mean(element: ET.Element) -> Optional[NewTransportMean]:
    if element is None:
        return None

    result = NewTransportMean(
        brand=XR.get_child_text(element, 'brand', DATA),
        serial_num=XR.get_child_text(element, 'serialNum', DATA),
        engine_num=XR.get_child_text(element, 'engineNum', DATA),
        first_entry_into_service=XR.get_child_date(element, 'firstEntryIntoService', DATA),
        vehicle=deserialize_vehicle(
            XR.find_child(element, 'vehicle', DATA)
        ),
        vessel=deserialize_vessel(
            XR.find_child(element, 'vessel', DATA)
        ),
        aircraft=deserialize_aircraft(
            XR.find_child(element, 'aircraft', DATA)
        ),
    )

    return result
