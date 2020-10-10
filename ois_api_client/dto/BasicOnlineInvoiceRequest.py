from .BasicHeader import BasicHeader
from .BasicRequest import BasicRequest
from .Software import Software
from .UserHeader import UserHeader


class BasicOnlineInvoiceRequest(BasicRequest):
    """Online Invoice specific basic request data

    :param header: Transactional data of the request
    :param user: Authentication data of the request
    :param software: Billing software data
    """

    def __init__(self, header: BasicHeader, user: UserHeader, software: Software):
        super().__init__(header, user)
        self.software = software
