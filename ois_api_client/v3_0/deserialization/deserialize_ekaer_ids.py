from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.EkaerIds import EkaerIds


def deserialize_ekaer_ids(element: ET.Element) -> Optional[EkaerIds]:
    if element is None:
        return None

    result = EkaerIds(
        ekaer_id=[e.text for e in XR.find_all_child(element, 'ekaerId', DATA)],
    )

    return result
