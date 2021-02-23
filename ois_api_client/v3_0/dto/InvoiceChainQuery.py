from typing import Optional
from dataclasses import dataclass
from .InvoiceDirection import InvoiceDirection


@dataclass
class InvoiceChainQuery:
    """Invoice number param of the invoice chain digest query

    :param invoice_number: Sequential number of the original or modification invoice
    :param invoice_direction: Inbound or outbound invoice query parameter
    :param tax_number: Tax number of the supplier or the customer of the invoice (the search criteria depends on the value of the invoiceDirection tag)
    """

    invoice_number: str
    invoice_direction: InvoiceDirection
    tax_number: Optional[str]
