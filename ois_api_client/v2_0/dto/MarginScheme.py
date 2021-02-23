from enum import Enum


class MarginScheme(Enum):
    """Field type for inputting margin-scheme taxation"""
    TRAVEL_AGENCY = 'TRAVEL_AGENCY'
    """Travel agencies"""
    SECOND_HAND = 'SECOND_HAND'
    """Second-hand goods"""
    ARTWORK = 'ARTWORK'
    """Works of art"""
    ANTIQUES = 'ANTIQUES'
    """Collector’s items and antiques"""
