from enum import Enum


class ProductFeeOperation(Enum):
    """Product fee summary type"""
    REFUND = 'REFUND'
    """Refund"""
    DEPOSIT = 'DEPOSIT'
    """Deposit"""
