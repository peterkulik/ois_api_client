from typing import Optional
from dataclasses import dataclass
from .AdvancePaymentData import AdvancePaymentData


@dataclass
class AdvanceData:
    """Advance related data

    :param advance_indicator: The value is true if the invoice item is a kind of advance charge
    :param advance_payment_data: Advance payment related data
    """

    advance_indicator: bool
    advance_payment_data: Optional[AdvancePaymentData]
