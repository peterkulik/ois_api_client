from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import BASE
from ..namespaces import API
from ..dto.DateTimeIntervalParam import DateTimeIntervalParam


def deserialize_date_time_interval_param(element: ET.Element) -> Optional[DateTimeIntervalParam]:
    if element is None:
        return None

    result = DateTimeIntervalParam(
        date_time_from=XR.get_child_datetime(element, 'dateTimeFrom', API),
        date_time_to=XR.get_child_datetime(element, 'dateTimeTo', API),
    )

    return result
