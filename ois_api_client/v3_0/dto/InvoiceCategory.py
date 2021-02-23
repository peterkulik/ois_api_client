from enum import Enum


class InvoiceCategory(Enum):
    """Type of invoice"""
    NORMAL = 'NORMAL'
    """Normal (not simplified and not aggregate) invoice"""
    SIMPLIFIED = 'SIMPLIFIED'
    """Simplified invoice"""
    AGGREGATE = 'AGGREGATE'
    """Aggregate invoice"""
