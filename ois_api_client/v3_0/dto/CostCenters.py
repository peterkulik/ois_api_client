from typing import List
from dataclasses import dataclass


@dataclass
class CostCenters:
    """Cost centers

    :param cost_center: Cost center
    """

    cost_center: List[str]
