from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..namespaces import DATA
from ..dto.AdditionalData import AdditionalData


def deserialize_additional_data(element: ET.Element) -> Optional[AdditionalData]:
    if element is None:
        return None

    result = AdditionalData(
        data_name=XR.get_child_text(element, 'dataName', DATA),
        data_description=XR.get_child_text(element, 'dataDescription', DATA),
        data_value=XR.get_child_text(element, 'dataValue', DATA),
    )

    return result
