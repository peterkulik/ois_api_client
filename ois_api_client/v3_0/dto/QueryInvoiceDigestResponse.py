from dataclasses import dataclass
from .InvoiceDigestResult import InvoiceDigestResult
from .BasicOnlineInvoiceResponse import BasicOnlineInvoiceResponse


@dataclass
class QueryInvoiceDigestResponse(BasicOnlineInvoiceResponse):
    """Response type of the POST /queryInvoiceDigest REST operation

    :param invoice_digest_result: Invoice digest query results
    """

    invoice_digest_result: InvoiceDigestResult
