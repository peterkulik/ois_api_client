from .BasicOnlineInvoiceRequest import BasicOnlineInvoiceRequest
from .Header import Header
from .InvoiceDirection import InvoiceDirection
from .InvoiceQueryParams import InvoiceQueryParams
from .Software import Software
from .User import User


class QueryInvoiceDigestRequest(BasicOnlineInvoiceRequest):
    """Request type of the POST /queryInvoiceDigest REST operation

    :param page: The queried page count
    :param invoice_direction: Inbound or outbound invoice query parameter
    :param invoice_query_params: Invoice query parameters
    """

    def __init__(self, header: Header, user: User, software: Software, page: int, invoice_direction: InvoiceDirection,
                 invoice_query_params: InvoiceQueryParams):
        super().__init__(header, user, software)
        self.page = page
        self.invoice_direction = invoice_direction
        self.invoice_query_params = invoice_query_params
