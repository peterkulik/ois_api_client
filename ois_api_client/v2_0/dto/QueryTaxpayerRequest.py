from dataclasses import dataclass
from .BasicRequest import BasicRequest


@dataclass
class QueryTaxpayerRequest(BasicRequest):
    """Request type of the POST /queryTaxpayer REST operation

    :param tax_number: Tax number of the queried taxpayer
    """

    tax_number: str
