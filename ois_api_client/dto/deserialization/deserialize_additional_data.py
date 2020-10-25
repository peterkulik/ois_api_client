import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from ..AdditionalData import AdditionalData
from ...constants import NAMESPACE_DATA


def deserialize_additional_data(element: ET.Element) -> Union[AdditionalData, None]:
    if element is None:
        return None

    result = AdditionalData(
        data_name=XR.get_child_text(element, 'dataName', NAMESPACE_DATA),
        data_description=XR.get_child_text(element, 'dataDescription', NAMESPACE_DATA),
        data_value=XR.get_child_text(element, 'dataValue', NAMESPACE_DATA)
    )

    return result

