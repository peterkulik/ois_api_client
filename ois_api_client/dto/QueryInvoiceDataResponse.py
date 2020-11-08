from typing import Union
from .BasicOnlineInvoiceResponse import BasicOnlineInvoiceResponse
from .BasicResult import BasicResult
from .InvoiceDataResult import InvoiceDataResult
from .BasicHeader import BasicHeader
from .Software import Software


class QueryInvoiceDataResponse(BasicOnlineInvoiceResponse):
    """Response type of the POST /queryInvoiceData REST operation

    :param header: Transactional data of the response
    :param result: Basic result data
    :param software: Billing software data
    :param invoice_data_result: Invoice data query result
    """

    def __init__(self,
                 header: BasicHeader,
                 result: BasicResult,
                 software: Software,
                 invoice_data_result: Union[InvoiceDataResult, None]):
        super().__init__(header, result, software)
        self.invoice_data_result = invoice_data_result
