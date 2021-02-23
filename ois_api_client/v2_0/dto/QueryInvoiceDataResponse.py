from typing import Optional
from dataclasses import dataclass
from .InvoiceDataResult import InvoiceDataResult
from .BasicResponse import BasicResponse


@dataclass
class QueryInvoiceDataResponse(BasicResponse):
    """Response type of the POST /queryInvoiceData REST operation

    :param invoice_data_result: Invoice data query result
    """

    invoice_data_result: Optional[InvoiceDataResult]
