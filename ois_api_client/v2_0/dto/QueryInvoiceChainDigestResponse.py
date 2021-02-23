from dataclasses import dataclass
from .InvoiceChainDigestResult import InvoiceChainDigestResult
from .BasicResponse import BasicResponse


@dataclass
class QueryInvoiceChainDigestResponse(BasicResponse):
    """Response type of the POST /queryInvoiceChainDigest REST operation

    :param invoice_chain_digest_result: Invoice chain digest query result
    """

    invoice_chain_digest_result: InvoiceChainDigestResult
