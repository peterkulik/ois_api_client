from enum import Enum


class PaymentMethod(Enum):
    """Method of payment"""
    TRANSFER = 'TRANSFER'
    """Bank transfer"""
    CASH = 'CASH'
    """Cash"""
    CARD = 'CARD'
    """Debit card, credit card, other cash-substitute payment instrument"""
    VOUCHER = 'VOUCHER'
    """Voucher,  bill of exchange, other non-cash payment instrument"""
    OTHER = 'OTHER'
    """Other"""
