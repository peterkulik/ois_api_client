from typing import List
from dataclasses import dataclass
from .Notification import Notification


@dataclass
class Notifications:
    """Miscellaneous notifications

    :param notification: Notification
    """

    notification: List[Notification]
