from typing import List, Union

from .BatchInvoice import BatchInvoice
from .Invoice import Invoice


class InvoiceMain:
    """A common type to describe invoice information

    :param data: invoice or batch_invoice:
    invoice: Data of a single invoice or modification document
    , batch_invoice: Data of a batch of modification documents
    """

    def __init__(self, data: Union[Invoice, List[BatchInvoice]]):
        if isinstance(data, Invoice):
            self.invoice = data
        elif isinstance(data, list):
            self.batch_invoice = data
