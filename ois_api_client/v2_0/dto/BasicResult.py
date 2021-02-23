from typing import Optional
from dataclasses import dataclass
from .FunctionCode import FunctionCode


@dataclass
class BasicResult:
    """Basic result data

    :param func_code: Processing result
    :param error_code: Processing error code
    :param message: Processing message
    """

    func_code: FunctionCode
    error_code: Optional[str]
    message: Optional[str]
