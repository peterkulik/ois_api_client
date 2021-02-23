from typing import List
from dataclasses import dataclass
from .TaxpayerAddressItem import TaxpayerAddressItem


@dataclass
class TaxpayerAddressList:
    """Taxpayer address list type

    :param taxpayer_address_item: Taxpayer address item
    """

    taxpayer_address_item: List[TaxpayerAddressItem]
