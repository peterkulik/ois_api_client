from typing import List, Optional
from .Notification import Notification


class BasicResult:
    """Basic result data

    :param func_code: Processing result
    :param error_code: Processing error code
    :param message: Processing message
    :param notifications: Miscellaneous notifications
    """

    def __init__(self, func_code: str, error_code: Optional[str], message: Optional[str],
                 notifications: List[Notification]):
        self.func_code = func_code
        self.error_code = error_code
        self.message = message
        self.notifications = notifications
