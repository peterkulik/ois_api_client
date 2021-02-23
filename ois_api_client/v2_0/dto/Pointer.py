from typing import Optional
from dataclasses import dataclass


@dataclass
class Pointer:
    """Processing cursor data

    :param tag: Tag reference
    :param value: Value reference
    :param line: Line reference
    :param original_invoice_number: In case of a batch operation, the sequence number of the original invoice, on which the modification occurs
    """

    tag: Optional[str]
    value: Optional[str]
    line: Optional[int]
    original_invoice_number: Optional[str]
