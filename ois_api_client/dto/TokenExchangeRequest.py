from .BasicHeader import BasicHeader
from .BasicOnlineInvoiceRequest import BasicOnlineInvoiceRequest
from .Software import Software
from .UserHeader import UserHeader


class TokenExchangeRequest(BasicOnlineInvoiceRequest):
    """Response type of the POST /tokenExchange REST operation

    :param header: Transactional data of the request
    :param user: Authentication data of the request
    :param software: Billing software data
    """

    def __init__(self, header: BasicHeader, user: UserHeader, software: Software):
        super().__init__(header, user, software)
