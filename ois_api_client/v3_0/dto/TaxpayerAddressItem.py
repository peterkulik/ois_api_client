from dataclasses import dataclass
from .DetailedAddress import DetailedAddress
from .TaxpayerAddressType import TaxpayerAddressType


@dataclass
class TaxpayerAddressItem:
    """Taxpayer address item

    :param taxpayer_address_type: Taxpayer address type
    :param taxpayer_address: Address data of the taxpayer
    """

    taxpayer_address_type: TaxpayerAddressType
    taxpayer_address: DetailedAddress
