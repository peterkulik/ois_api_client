from typing import Optional
from dataclasses import dataclass
from .TaxNumber import TaxNumber
from .TaxpayerAddressList import TaxpayerAddressList


@dataclass
class TaxpayerData:
    """Response data of the taxpayer query

    :param taxpayer_name: Name of the taxpayer
    :param taxpayer_short_name: None
    :param tax_number_detail: Detailed data of the tax number
    :param vat_group_membership: VAT group membership of the taxpayer
    :param taxpayer_address_list: Taxpayer address list type
    """

    taxpayer_name: str
    taxpayer_short_name: Optional[str]
    tax_number_detail: TaxNumber
    vat_group_membership: Optional[str]
    taxpayer_address_list: Optional[TaxpayerAddressList]
