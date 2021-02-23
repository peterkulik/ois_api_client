from enum import Enum


class ProductStream(Enum):
    """Product stream"""
    BATTERY = 'BATTERY'
    """Battery"""
    PACKAGING = 'PACKAGING'
    """Packaging products"""
    OTHER_PETROL = 'OTHER_PETROL'
    """Other petroleum product"""
    ELECTRONIC = 'ELECTRONIC'
    """The electric appliance, electronic equipment"""
    TIRE = 'TIRE'
    """Tire"""
    COMMERCIAL = 'COMMERCIAL'
    """Commercial printing paper"""
    PLASTIC = 'PLASTIC'
    """Other plastic product"""
    OTHER_CHEMICAL = 'OTHER_CHEMICAL'
    """Other chemical product"""
    PAPER = 'PAPER'
    """Paper stationery"""
