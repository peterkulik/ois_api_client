from typing import List
from dataclasses import dataclass


@dataclass
class ReferencesToOtherLines:
    """References to connected items if it is necessary according to VAT law

    :param reference_to_other_line: References to connected items if it is necessary according to VAT law
    """

    reference_to_other_line: List[int]
