from dataclasses import dataclass


@dataclass
class Notification:
    """Notification

    :param notification_code: Notification code
    :param notification_text: Notification text
    """

    notification_code: str
    notification_text: str
