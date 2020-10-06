from dataclasses import dataclass

from .Header import Header
from .User import User
from .Software import Software


@dataclass
class BasicRequest:
    header: Header
    user: User
    software: Software
