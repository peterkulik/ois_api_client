from dataclasses import dataclass
from .BasicOnlineInvoiceResponse import BasicOnlineInvoiceResponse


@dataclass
class QueryInvoiceCheckResponse(BasicOnlineInvoiceResponse):
    """Response type of the POST /queryInvoiceCheck REST operation

    :param invoice_check_result: Indicates whether the queried invoice number exists in the system as a valid invoice, if the tax number of the querying entity is present on the invoice either as supplier or customer
    """

    invoice_check_result: bool
