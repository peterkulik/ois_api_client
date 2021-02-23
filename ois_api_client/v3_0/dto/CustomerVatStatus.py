from enum import Enum


class CustomerVatStatus(Enum):
    """Customers status type by VAT"""
    DOMESTIC = 'DOMESTIC'
    """Domestic VAT subject"""
    OTHER = 'OTHER'
    """Other (domestic non-VAT subject, non-natural person, foreign VAT subject and foreign non-VAT subject, non-natural person)"""
    PRIVATE_PERSON = 'PRIVATE_PERSON'
    """Non-VAT subject (domestic or foreign) natural person"""
