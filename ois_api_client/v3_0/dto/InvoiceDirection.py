from enum import Enum


class InvoiceDirection(Enum):
    """Inbound or outbound invoice query parameter"""
    INBOUND = 'INBOUND'
    """Inbound (customer side) invoice query parameter"""
    OUTBOUND = 'OUTBOUND'
    """Outbound (supplier side) invoice query parameter"""
