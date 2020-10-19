from .BatchInvoice import BatchInvoice
from .Invoice import Invoice


class InvoiceMain:
    """A common type to describe invoice information

    :param invoice: Data of a single invoice or modification document
    :param batch_invoice: Data of a batch of modification documents
    """

    def __init__(self, invoice: Invoice, batch_invoice: BatchInvoice):
        self.invoice = invoice
        self.batch_invoice = batch_invoice
