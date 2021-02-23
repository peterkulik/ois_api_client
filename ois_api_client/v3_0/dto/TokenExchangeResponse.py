from datetime import datetime
from dataclasses import dataclass
from .BasicOnlineInvoiceResponse import BasicOnlineInvoiceResponse


@dataclass
class TokenExchangeResponse(BasicOnlineInvoiceResponse):
    """Response type of the POST /tokenExchange REST operation

    :param encoded_exchange_token: The issued exchange token in AES-128 ECB encoded form
    :param token_validity_from: Validity start of the issued exchange token
    :param token_validity_to: Validity end of the issued exchange token
    """

    encoded_exchange_token: str
    token_validity_from: datetime
    token_validity_to: datetime
