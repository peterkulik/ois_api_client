from .Invoice import Invoice


class BatchInvoice:
    """Data of a batch of modification documents

    :param batch_index: Sequence number of the modification document within the batch
    :param invoice: Data of a single invoice or modification document
    """

    def __init__(self, batch_index: int, invoice: Invoice):
        self.batch_index = batch_index
        self.invoice = invoice
