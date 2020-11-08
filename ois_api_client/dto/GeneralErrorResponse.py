from typing import List

from .BasicHeader import BasicHeader
from .BasicResponse import BasicResponse
from .BasicResult import BasicResult
from .TechnicalValidationResult import TechnicalValidationResult
from .Software import Software


class GeneralErrorResponse(BasicResponse):
    """Generic fault type for every REST operation

    :param result: Basic result data
    :param technical_validation_messages: Technical validation messages
    """

    def __init__(self, header: BasicHeader, result: BasicResult, software: Software,
                 technical_validation_messages: List[TechnicalValidationResult] = None):
        super().__init__(header=header, result=result)

        self.software = software
        if technical_validation_messages is None:
            technical_validation_messages = []
        self.technical_validation_messages = technical_validation_messages
