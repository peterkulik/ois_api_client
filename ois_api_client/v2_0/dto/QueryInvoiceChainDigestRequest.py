from dataclasses import dataclass
from .InvoiceChainQuery import InvoiceChainQuery
from .BasicRequest import BasicRequest


@dataclass
class QueryInvoiceChainDigestRequest(BasicRequest):
    """Request type of the POST /queryInvoiceChainDigest REST operation

    :param page: The queried page count
    :param invoice_chain_query: Invoice number param of the invoice chain digest query
    """

    page: int
    invoice_chain_query: InvoiceChainQuery
