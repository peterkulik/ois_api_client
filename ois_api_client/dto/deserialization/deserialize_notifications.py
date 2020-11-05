import xml.etree.ElementTree as ET

from .XmlReader import XmlReader as XR
from ..Notification import Notification
from ...constants import NAMESPACE_COMMON


def _deserialize_notification(el: ET.Element) -> Notification:
    return Notification(
        notification_code=XR.get_child_text(el, 'notificationCode', NAMESPACE_COMMON),
        notification_text=XR.get_child_text(el, 'notificationText', NAMESPACE_COMMON)
    )


def deserialize_notifications(parent: ET.Element):
    if parent is None:
        return None

    result = [_deserialize_notification(el) for el in XR.find_all_child(parent, 'notification', NAMESPACE_COMMON)]
    return result
