from typing import Optional
from dataclasses import dataclass
from .BusinessResultCode import BusinessResultCode
from .Pointer import Pointer


@dataclass
class BusinessValidationResult:
    """Business validation response type

    :param validation_result_code: Validation result
    :param validation_error_code: Validation error code
    :param message: Processing message
    :param pointer: Processing cursor data
    """

    validation_result_code: BusinessResultCode
    validation_error_code: Optional[str]
    message: Optional[str]
    pointer: Optional[Pointer]
