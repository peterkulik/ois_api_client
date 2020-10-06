from dataclasses import dataclass
from datetime import datetime


@dataclass
class Header:
    request_id: str
    timestamp: datetime
