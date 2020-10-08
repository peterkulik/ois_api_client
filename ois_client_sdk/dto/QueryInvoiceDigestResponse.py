from .BasicResponse import BasicResponse
from .BasicResult import BasicResult
from .InvoiceDigestResult import InvoiceDigestResult


class QueryInvoiceDigestResponse(BasicResponse):
    """Response type of the POST /queryInvoiceDigest REST operation

    :param invoice_digest_result: Invoice digest query results
    """

    def __init__(self, result: BasicResult, invoice_digest_result: InvoiceDigestResult):
        super().__init__(result)
        self.invoice_digest_result = invoice_digest_result
