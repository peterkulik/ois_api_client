from typing import Optional
from typing import List
from dataclasses import dataclass
from .InvoiceChainElement import InvoiceChainElement


@dataclass
class InvoiceChainDigestResult:
    """Invoice chain digest query result

    :param current_page: The currently queried page count
    :param available_page: The highest available page count matching the query
    :param invoice_chain_element: Invoice chain element
    """

    current_page: int
    available_page: int
    invoice_chain_element: Optional[List[InvoiceChainElement]]
