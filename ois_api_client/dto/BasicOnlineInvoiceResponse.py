from .BasicResponse import BasicResponse
from .BasicResult import BasicResult


class BasicOnlineInvoiceResponse(BasicResponse):
    """Online Invoice specific basic response data

    :param result: Basic result data
    """

    def __init__(self,
                 # header: BasicHeader,
                 result: BasicResult,
                 # software: Software
                 ):
        super().__init__(result)
        # self.software = software
