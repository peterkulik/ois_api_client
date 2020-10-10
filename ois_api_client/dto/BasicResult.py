from typing import Union, List
from .Notification import Notification


class BasicResult:
    """Basic result data

    :param func_code: Processing result
    :param error_code: Processing error code
    :param message: Processing message
    :param notifications: Miscellaneous notifications
    """

    def __init__(self, func_code: str, error_code: Union[str, None], message: Union[str, None],
                 notifications: List[Notification]):
        self.func_code = func_code
        self.error_code = error_code
        self.message = message
        self.notifications = notifications
