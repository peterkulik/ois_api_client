from typing import List
from dataclasses import dataclass
from .AnnulmentOperation import AnnulmentOperation


@dataclass
class AnnulmentOperationList:
    """Batch technical annulment operations of the request

    :param annulment_operation: Technial annulment operation of the request
    """

    annulment_operation: List[AnnulmentOperation]
