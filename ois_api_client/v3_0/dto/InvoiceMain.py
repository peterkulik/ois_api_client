from typing import Optional
from typing import List
from dataclasses import dataclass
from .BatchInvoice import BatchInvoice
from .Invoice import Invoice


@dataclass
class InvoiceMain:
    """A common type to describe invoice information

    :param invoice: Data of a single invoice or modification document
    :param batch_invoice: Data of a batch of modification documents
    """

    invoice: Optional[Invoice]
    batch_invoice: Optional[List[BatchInvoice]]
