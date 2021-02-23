from typing import List
from dataclasses import dataclass


@dataclass
class GlnNumbers:
    """Global location numbers

    :param gln_number: Global location number
    """

    gln_number: List[str]
