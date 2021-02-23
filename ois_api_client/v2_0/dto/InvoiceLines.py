from typing import Optional
from typing import List
from dataclasses import dataclass
from .NewCreatedLines import NewCreatedLines


@dataclass
class InvoiceLines:
    """Product/service digest data appearing on the invoice or the modification document

    :param max_line_number: The highest line number value the invoice contains
    :param new_created_lines: New invoice lines created by the modification document
    """

    max_line_number: int
    new_created_lines: Optional[List[NewCreatedLines]]
