from typing import List

from .BasicResponse import BasicResponse
from .BasicResult import BasicResult
from .TechnicalValidationResult import TechnicalValidationResult


class GeneralErrorResponse(BasicResponse):
    """Generic fault type for every REST operation

    :param result: Basic result data
    :param technical_validation_messages: Technical validation messages
    """

    def __init__(self, result: BasicResult, technical_validation_messages: List[TechnicalValidationResult] = None):
        super().__init__(result=result)
        if technical_validation_messages is None:
            technical_validation_messages = []
        self.technical_validation_messages = technical_validation_messages
