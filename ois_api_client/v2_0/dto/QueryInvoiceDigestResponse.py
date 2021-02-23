from dataclasses import dataclass
from .InvoiceDigestResult import InvoiceDigestResult
from .BasicResponse import BasicResponse


@dataclass
class QueryInvoiceDigestResponse(BasicResponse):
    """Response type of the POST /queryInvoiceDigest REST operation

    :param invoice_digest_result: Invoice digest query results
    """

    invoice_digest_result: InvoiceDigestResult
