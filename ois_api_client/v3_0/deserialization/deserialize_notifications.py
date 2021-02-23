from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..dto.Notifications import Notifications
from .deserialize_notification import deserialize_notification


def deserialize_notifications(element: ET.Element) -> Optional[Notifications]:
    if element is None:
        return None

    result = Notifications(
        notification=[deserialize_notification(e) for e in XR.find_all_child(element, 'notification', COMMON)],
    )

    return result
