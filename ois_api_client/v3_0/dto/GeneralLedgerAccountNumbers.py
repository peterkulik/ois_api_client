from typing import List
from dataclasses import dataclass


@dataclass
class GeneralLedgerAccountNumbers:
    """General ledger account numbers

    :param general_ledger_account_number: General ledger account number
    """

    general_ledger_account_number: List[str]
