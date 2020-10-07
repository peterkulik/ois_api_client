class Notification:
    """Notification

    :param notification_code:
    :param notification_text:
    """

    def __init__(self, notification_code: str, notification_text: str):
        self.notification_code = notification_code
        self.notification_text = notification_text
