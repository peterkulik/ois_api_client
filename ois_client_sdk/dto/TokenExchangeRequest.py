from dataclasses import dataclass
from .BasicRequest import BasicRequest
from .Header import Header
from .Software import Software
from .User import User


@dataclass
class TokenExchangeRequest(BasicRequest):
    def __init__(self, header: Header, user: User, software: Software):
        super().__init__(header, user, software)
