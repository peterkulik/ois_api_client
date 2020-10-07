from dataclasses import dataclass
from datetime import datetime
from .BasicResponse import BasicResponse


@dataclass
class TokenExchangeResponse(BasicResponse):
    encoded_exchange_token: str
    token_validity_from: datetime
    token_validity_to: datetime
