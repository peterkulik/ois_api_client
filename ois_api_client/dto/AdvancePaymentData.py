from datetime import date


class AdvancePaymentData:
    """Advance payment related data

    :param advance_original_invoice: Invoice number containing the advance payment
    :param advance_payment_date: Payment date of the advance
    :param advance_exchange_rate: Applied exchange rate of the advance
    """
    def __init__(self,
                 advance_original_invoice: str,
                 advance_payment_date: date,
                 advance_exchange_rate: float
                 ):
        self.advance_original_invoice = advance_original_invoice
        self.advance_payment_date = advance_payment_date
        self.advance_exchange_rate = advance_exchange_rate
