class TechnicalValidationResult:
    """Technical validation response type

    :param validation_result_code: Validation result
    :param validation_error_code: Validation error code
    :param message: Processing message
    """

    def __init__(self, validation_result_code: str, validation_error_code: str, message: str):
        self.validation_result_code = validation_result_code
        self.validation_error_code = validation_error_code
        self.message = message
