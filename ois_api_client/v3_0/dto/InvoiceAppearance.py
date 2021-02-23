from enum import Enum


class InvoiceAppearance(Enum):
    """Form of appearance of the invoice type"""
    PAPER = 'PAPER'
    """Invoice issued on paper"""
    ELECTRONIC = 'ELECTRONIC'
    """Electronic invoice (non-EDI)"""
    EDI = 'EDI'
    """EDI invoice"""
    UNKNOWN = 'UNKNOWN'
    """The software cannot be identify the form of appearance of the invoice or it is unknown at the time of issue"""
