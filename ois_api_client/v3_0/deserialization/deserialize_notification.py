from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..dto.Notification import Notification


def deserialize_notification(element: ET.Element) -> Optional[Notification]:
    if element is None:
        return None

    result = Notification(
        notification_code=XR.get_child_text(element, 'notificationCode', COMMON),
        notification_text=XR.get_child_text(element, 'notificationText', COMMON),
    )

    return result
