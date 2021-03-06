from dataclasses import dataclass
from .InvoiceDirection import InvoiceDirection
from .InvoiceQueryParams import InvoiceQueryParams
from .BasicOnlineInvoiceRequest import BasicOnlineInvoiceRequest


@dataclass
class QueryInvoiceDigestRequest(BasicOnlineInvoiceRequest):
    """Request type of the POST /queryInvoiceDigest REST operation

    :param page: The queried page count
    :param invoice_direction: Inbound or outbound invoice query parameter
    :param invoice_query_params: Invoice query parameters
    """

    page: int
    invoice_direction: InvoiceDirection
    invoice_query_params: InvoiceQueryParams
