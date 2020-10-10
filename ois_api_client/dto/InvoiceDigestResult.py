from typing import List
from .InvoiceDigest import InvoiceDigest


class InvoiceDigestResult:
    """Invoice query results

    :param current_page: The currently queried page count
    :param available_page: The highest available page count matching the query
    :param invoice_digest: Invoice digest query result
    """

    def __init__(self, current_page: int, available_page: int, invoice_digest: List[InvoiceDigest]):
        self.current_page = current_page
        self.available_page = available_page
        self.invoice_digest = invoice_digest
