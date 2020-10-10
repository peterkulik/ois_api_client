from .BasicHeader import BasicHeader
from .BasicOnlineInvoiceRequest import BasicOnlineInvoiceRequest
from .InvoiceNumberQuery import InvoiceNumberQuery
from .Software import Software
from .UserHeader import UserHeader


class QueryInvoiceDataRequest(BasicOnlineInvoiceRequest):
    """Request type of the POST /queryInvoiceData REST operation

    :param invoice_number_query: Invoice number param of the Invoice query
    """

    def __init__(self, header: BasicHeader, user: UserHeader, software: Software, invoice_number_query: InvoiceNumberQuery):
        super().__init__(header, user, software)
        self.invoice_number_query = invoice_number_query
