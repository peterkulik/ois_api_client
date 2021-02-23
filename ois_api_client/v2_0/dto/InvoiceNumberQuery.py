from typing import Optional
from dataclasses import dataclass
from .InvoiceDirection import InvoiceDirection


@dataclass
class InvoiceNumberQuery:
    """Invoice number param of the Invoice query

    :param invoice_number: Sequential number of the original or modifiation invoice
    :param invoice_direction: Inbound or outbound invoice query parameter
    :param batch_index: Sequence number of the modification document within the batch
    :param supplier_tax_number: The supplier's tax number in case of querying as customer, if the query result found more than one valid invoices with the same invoice number
    """

    invoice_number: str
    invoice_direction: InvoiceDirection
    batch_index: Optional[int]
    supplier_tax_number: Optional[str]
