from enum import Enum


class LineNatureIndicator(Enum):
    """Indication of the nature of the supply of goods or services on a given line"""
    PRODUCT = 'PRODUCT'
    """Supply of goods"""
    SERVICE = 'SERVICE'
    """Supply of services"""
    OTHER = 'OTHER'
    """Other, non-qualifiable"""
