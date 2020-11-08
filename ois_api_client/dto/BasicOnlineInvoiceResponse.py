from .BasicResponse import BasicResponse
from .BasicResult import BasicResult
from .BasicHeader import BasicHeader
from .Software import Software


class BasicOnlineInvoiceResponse(BasicResponse):
    """Online Invoice specific basic response data

    :param header: Transactional data of the response
    :param result: Basic result data
    :param software: Billing software data
    """

    def __init__(self,
                 header: BasicHeader,
                 result: BasicResult,
                 software: Software
                 ):
        super().__init__(header, result)
        self.software = software
