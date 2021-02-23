from dataclasses import dataclass
from .InvoiceChainQuery import InvoiceChainQuery
from .BasicOnlineInvoiceRequest import BasicOnlineInvoiceRequest


@dataclass
class QueryInvoiceChainDigestRequest(BasicOnlineInvoiceRequest):
    """Request type of the POST /queryInvoiceChainDigest REST operation

    :param page: The queried page count
    :param invoice_chain_query: Invoice number param of the invoice chain digest query
    """

    page: int
    invoice_chain_query: InvoiceChainQuery
