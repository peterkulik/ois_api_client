from .BasicResult import BasicResult
from .BasicHeader import BasicHeader


class BasicResponse:
    """Basic response data

    :param header: Transactional data of the response
    :param result: Basic result data
    """

    def __init__(self,
                 header: BasicHeader,
                 result: BasicResult):
        self.header = header
        self.result = result
