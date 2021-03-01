from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import BASE
from ..namespaces import API
from ..dto.DateIntervalParam import DateIntervalParam


def deserialize_date_interval_param(element: ET.Element) -> Optional[DateIntervalParam]:
    if element is None:
        return None

    result = DateIntervalParam(
        date_from=XR.get_child_date(element, 'dateFrom', API),
        date_to=XR.get_child_date(element, 'dateTo', API),
    )

    return result
