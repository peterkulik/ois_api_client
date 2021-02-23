from enum import Enum


class Source(Enum):
    """Data exchange source"""
    WEB = 'WEB'
    """Web exchange"""
    XML = 'XML'
    """Manual XML upload"""
    MGM = 'MGM'
    """Machine-to-machine exchange"""
    OPG = 'OPG'
    """Online cash register exchange"""
    OSZ = 'OSZ'
    """NTCA online invoicing"""
