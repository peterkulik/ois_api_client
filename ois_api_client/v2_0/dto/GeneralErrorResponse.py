from typing import Optional
from typing import List
from dataclasses import dataclass
from .TechnicalValidationResult import TechnicalValidationResult
from .BasicResponse import BasicResponse


@dataclass
class GeneralErrorResponse(BasicResponse):
    """Generic fault type for every REST operation

    :param technical_validation_messages: Technical validation messages
    """

    technical_validation_messages: Optional[List[TechnicalValidationResult]]
