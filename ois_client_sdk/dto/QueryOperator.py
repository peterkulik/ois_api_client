from enum import Enum


class QueryOperator(Enum):
    """Relational operator type"""
    EQ = 'EQ'
    """Equals"""
    GT = 'GT'
    """Greater than relation"""
    GTE = 'GTE'
    """Greater or equals relation"""
    LT = 'LT'
    """Less than relation"""
    LTE = 'LTE'
    """Less or equals relation"""
