from .BasicHeader import BasicHeader
from .BasicOnlineInvoiceResponse import BasicOnlineInvoiceResponse
from .BasicResult import BasicResult
from .InvoiceDigestResult import InvoiceDigestResult
from .Software import Software


class QueryInvoiceDigestResponse(BasicOnlineInvoiceResponse):
    """Response type of the POST /queryInvoiceDigest REST operation

    :param result: Basic result data
    :param invoice_digest_result: Invoice digest query results
    """

    def __init__(self,
                 header: BasicHeader,
                 result: BasicResult,
                 software: Software,
                 invoice_digest_result: InvoiceDigestResult):
        super().__init__(header, result, software)
        self.invoice_digest_result = invoice_digest_result
