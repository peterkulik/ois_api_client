from enum import Enum


class TaxpayerAddressType(Enum):
    """Taxpayer address type"""
    HQ = 'HQ'
    """Headquarter"""
    SITE = 'SITE'
    """Site office"""
    BRANCH = 'BRANCH'
    """Branch office"""
