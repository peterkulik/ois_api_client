from enum import Enum


class InvoiceStatus(Enum):
    """Processing status of the invoice"""
    RECEIVED = 'RECEIVED'
    """Received"""
    PROCESSING = 'PROCESSING'
    """Processing"""
    SAVED = 'SAVED'
    """Saved"""
    DONE = 'DONE'
    """Done"""
    ABORTED = 'ABORTED'
    """Aborted"""
