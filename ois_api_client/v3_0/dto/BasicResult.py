from typing import Optional
from dataclasses import dataclass
from .FunctionCode import FunctionCode
from .Notifications import Notifications


@dataclass
class BasicResult:
    """Basic result data

    :param func_code: Processing result
    :param error_code: Processing error code
    :param message: Processing message
    :param notifications: Miscellaneous notifications
    """

    func_code: FunctionCode
    error_code: Optional[str]
    message: Optional[str]
    notifications: Optional[Notifications]
