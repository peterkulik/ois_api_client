from dataclasses import dataclass
from .BasicOnlineInvoiceRequest import BasicOnlineInvoiceRequest


@dataclass
class QueryTaxpayerRequest(BasicOnlineInvoiceRequest):
    """Request type of the POST /queryTaxpayer REST operation

    :param tax_number: Tax number of the queried taxpayer
    """

    tax_number: str
