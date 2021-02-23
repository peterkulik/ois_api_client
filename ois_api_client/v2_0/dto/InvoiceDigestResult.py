from typing import Optional
from typing import List
from dataclasses import dataclass
from .InvoiceDigest import InvoiceDigest


@dataclass
class InvoiceDigestResult:
    """Invoice query results

    :param current_page: The currently queried page count
    :param available_page: The highest available page count matching the query
    :param invoice_digest: Invoice digest query result
    """

    current_page: int
    available_page: int
    invoice_digest: Optional[List[InvoiceDigest]]
