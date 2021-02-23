from dataclasses import dataclass
from .Invoice import Invoice


@dataclass
class BatchInvoice:
    """Data of a batch of modification documents

    :param batch_index: Sequence number of the modification document within the batch
    :param invoice: Data of a single invoice or modification document
    """

    batch_index: int
    invoice: Invoice
