import xml.etree.ElementTree as ET
from typing import Optional

from .XmlReader import XmlReader as XR
from ..EkaerIds import EkaerIds
from ...constants import NAMESPACE_DATA


def deserialize_ekaer_ids(element: ET.Element) -> Optional[EkaerIds]:
    if element is None:
        return None

    result = EkaerIds(
        items=[el.text for el in XR.find_all_child(element, 'ekaerId', NAMESPACE_DATA)]
    )

    return result
