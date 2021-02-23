from typing import Optional
from datetime import datetime
from dataclasses import dataclass
from .TaxpayerData import TaxpayerData
from .BasicOnlineInvoiceResponse import BasicOnlineInvoiceResponse


@dataclass
class QueryTaxpayerResponse(BasicOnlineInvoiceResponse):
    """Response type of the POST /queryTaxpayer REST operation

    :param info_date: Last date on which the data was changed
    :param taxpayer_validity: Indicates whether the queried taxpayer is existing and valid
    :param taxpayer_data: Response data of the taxpayer query
    """

    info_date: Optional[datetime]
    taxpayer_validity: Optional[bool]
    taxpayer_data: Optional[TaxpayerData]
