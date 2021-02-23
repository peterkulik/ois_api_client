from typing import Optional
from dataclasses import dataclass
from .DetailedAddress import DetailedAddress
from .SimpleAddress import SimpleAddress


@dataclass
class Address:
    """Format of address that includes either a simple or a detailed address

    :param simple_address: Simple address
    :param detailed_address: Detailed address
    """

    simple_address: Optional[SimpleAddress]
    detailed_address: Optional[DetailedAddress]
