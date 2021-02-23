from typing import Optional
from typing import List
from dataclasses import dataclass
from .Software import Software
from .TechnicalValidationResult import TechnicalValidationResult
from .GeneralErrorHeaderResponse import GeneralErrorHeaderResponse


@dataclass
class GeneralErrorResponse(GeneralErrorHeaderResponse):
    """Online Invoice specific general error response type

    :param software: Billing software data
    :param technical_validation_messages: Technical validation messages
    """

    software: Software
    technical_validation_messages: Optional[List[TechnicalValidationResult]]
