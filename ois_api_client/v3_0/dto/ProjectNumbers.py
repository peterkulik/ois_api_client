from typing import List
from dataclasses import dataclass


@dataclass
class ProjectNumbers:
    """Project numbers

    :param project_number: Project number
    """

    project_number: List[str]
