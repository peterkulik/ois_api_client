from typing import Union
from .BasicOnlineInvoiceResponse import BasicOnlineInvoiceResponse
from .BasicResult import BasicResult
from .InvoiceDataResult import InvoiceDataResult


class QueryInvoiceDataResponse(BasicOnlineInvoiceResponse):
    """Response type of the POST /queryInvoiceData REST operation

    :param invoice_data_result: Invoice data query result
    """

    def __init__(self, result: BasicResult, invoice_data_result: Union[InvoiceDataResult, None]):
        super().__init__(result)
        self.invoice_data_result = invoice_data_result
