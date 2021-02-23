from typing import List
from dataclasses import dataclass


@dataclass
class MaterialNumbers:
    """Material numbers

    :param material_number: Material number
    """

    material_number: List[str]
