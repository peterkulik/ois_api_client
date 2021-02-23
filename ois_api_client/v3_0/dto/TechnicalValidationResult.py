from typing import Optional
from dataclasses import dataclass
from .TechnicalResultCode import TechnicalResultCode


@dataclass
class TechnicalValidationResult:
    """Technical validation response type

    :param validation_result_code: Validation result
    :param validation_error_code: Validation error code
    :param message: Processing message
    """

    validation_result_code: TechnicalResultCode
    validation_error_code: Optional[str]
    message: Optional[str]
