from typing import Optional
from dataclasses import dataclass
from .VatRate import VatRate
from .VatRateGrossData import VatRateGrossData
from .VatRateNetData import VatRateNetData
from .VatRateVatData import VatRateVatData


@dataclass
class SummaryByVatRate:
    """Summary according to VAT rates

    :param vat_rate: Marking the tax rate or the fact of tax exemption
    :param vat_rate_net_data: Net data of given tax rate
    :param vat_rate_vat_data: VAT data of given tax rate
    :param vat_rate_gross_data: Gross data of given tax rate
    """

    vat_rate: VatRate
    vat_rate_net_data: VatRateNetData
    vat_rate_vat_data: VatRateVatData
    vat_rate_gross_data: Optional[VatRateGrossData]
