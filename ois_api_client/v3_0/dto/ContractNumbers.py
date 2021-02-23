from typing import List
from dataclasses import dataclass


@dataclass
class ContractNumbers:
    """Contract numbers

    :param contract_number: Contract number
    """

    contract_number: List[str]
