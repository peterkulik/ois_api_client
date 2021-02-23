from dataclasses import dataclass
from .ManageInvoiceOperation import ManageInvoiceOperation


@dataclass
class InvoiceOperation:
    """Invoice operation of the request

    :param index: Sequence number of the invoice within the request
    :param invoice_operation: Type of the desired invoice operation
    :param invoice_data: Invoice data in BASE64 encoded form
    """

    index: int
    invoice_operation: ManageInvoiceOperation
    invoice_data: str
