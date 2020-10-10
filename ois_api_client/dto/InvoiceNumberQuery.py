from typing import Union
from .InvoiceDirection import InvoiceDirection


class InvoiceNumberQuery:
    """Invoice number param of the Invoice query

    :param invoice_number: Sequential number of the original or modifiation invoice
    :param invoice_direction: Inbound or outbound invoice query parameter
    :param batch_index: Sequence number of the modification document within the batch
    :param supplier_tax_number: The supplier's tax number in case of querying as customer, if the query result found more than one valid invoices with the same invoice number
    """

    def __init__(self, invoice_number: str, invoice_direction: InvoiceDirection, batch_index: Union[int, None],
                 supplier_tax_number: Union[str, None]):
        self.invoice_number = invoice_number
        self.invoice_direction = invoice_direction
        self.batch_index = batch_index
        self.supplier_tax_number = supplier_tax_number
