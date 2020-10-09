from .BasicResult import BasicResult


class BasicResponse:
    """Basic response data

    :param result: Basic result data
    """

    def __init__(self,
                 # header: BasicHeader,
                 result: BasicResult):
        # self.header = header
        self.result = result
