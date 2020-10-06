class GeneralError(Exception):
    def __init__(self, general_error_response: str):
        self.message = 'A GeneralErrorResponse sent by the Online Invoice System.'
        self.general_error_response = general_error_response


def __str__(self):
    return f'{self.message}: {self.general_error_response}'
