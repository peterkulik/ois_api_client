from typing import List
from ois_client_sdk.dto.BasicResponse import BasicResponse


class GeneralErrorResponse(BasicResponse):
    class TechnicalValidationMessage:
        validation_result_code: str
        validation_error_code: str
        message: str

    technical_validation_messages: List[TechnicalValidationMessage]

    def __init__(self):
        self.technical_validation_messages = []
