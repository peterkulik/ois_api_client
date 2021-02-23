from dataclasses import dataclass
from .InvoiceNumberQuery import InvoiceNumberQuery
from .BasicRequest import BasicRequest


@dataclass
class QueryInvoiceDataRequest(BasicRequest):
    """Request type of the POST /queryInvoiceData REST operation

    :param invoice_number_query: Invoice number param of the Invoice query
    """

    invoice_number_query: InvoiceNumberQuery
