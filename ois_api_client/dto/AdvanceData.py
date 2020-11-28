from .AdvancePaymentData import AdvancePaymentData


class AdvanceData:
    """Advance related data

    :param advance_indicator: The value is true if the invoice item is a kind of advance charge
    :param advance_payment_data: Advance payment related data
    """

    def __init__(self,
                 advance_indicator: bool,
                 advance_payment_data: AdvancePaymentData):
        self.advance_indicator = advance_indicator
        self.advance_payment_data = advance_payment_data
