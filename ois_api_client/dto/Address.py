from typing import Union

from .DetailedAddress import DetailedAddress
from .SimpleAddress import SimpleAddress


class Address:
    """Format of address that includes either a simple or a detailed address
    :param address: simple_address: SimpleAddress or detailed_address: DetailedAddress
    """

    def __init__(self, address: Union[SimpleAddress, DetailedAddress]):
        if isinstance(address, SimpleAddress):
            self.simple_address = address
        elif isinstance(address, DetailedAddress):
            self.detailed_address = address
