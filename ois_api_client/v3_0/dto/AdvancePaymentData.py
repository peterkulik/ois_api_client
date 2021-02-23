from datetime import date
from dataclasses import dataclass


@dataclass
class AdvancePaymentData:
    """Advance payment related data

    :param advance_original_invoice: Invoice number containing the advance payment
    :param advance_payment_date: Payment date of the advance
    :param advance_exchange_rate: Applied exchange rate of the advance
    """

    advance_original_invoice: str
    advance_payment_date: date
    advance_exchange_rate: float
