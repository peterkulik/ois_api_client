from enum import Enum


class Incorporation(Enum):
    """Incorporation type"""
    ORGANIZATION = 'ORGANIZATION'
    """Economical company"""
    SELF_EMPLOYED = 'SELF_EMPLOYED'
    """Self employed private entrepreneur"""
    TAXABLE_PERSON = 'TAXABLE_PERSON'
    """Private person with tax number"""
