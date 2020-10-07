from enum import Enum


class InvoiceDirection(Enum):
    """Inbound or outbound invoice query parameter"""
    INBOUND = 'INBOUND'
    OUTBOUND = 'OUTBOUND'
