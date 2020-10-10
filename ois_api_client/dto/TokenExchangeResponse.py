from datetime import datetime
from .BasicOnlineInvoiceResponse import BasicOnlineInvoiceResponse
from .BasicResult import BasicResult


class TokenExchangeResponse(BasicOnlineInvoiceResponse):
    """Response type of the POST /tokenExchange REST operation

    :param result: Basic result data
    :param encoded_exchange_token: The issued exchange token in AES-128 ECB encoded form
    :param token_validity_from: Validity start of the issued exchange token
    :param token_validity_to: Validity end of the issued exchange token
    """

    def __init__(self,  # header: BasicHeader,
                 result: BasicResult,
                 # software: Software,
                 encoded_exchange_token: str,
                 token_validity_from: datetime,
                 token_validity_to: datetime):
        super().__init__(result)
        self.encoded_exchange_token = encoded_exchange_token
        self.token_validity_from = token_validity_from
        self.token_validity_to = token_validity_to
