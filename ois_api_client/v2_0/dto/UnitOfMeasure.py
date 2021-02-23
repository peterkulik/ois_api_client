from enum import Enum


class UnitOfMeasure(Enum):
    """Unit of measure type"""
    PIECE = 'PIECE'
    """Piece"""
    KILOGRAM = 'KILOGRAM'
    """Kilogram"""
    TON = 'TON'
    """Metric ton"""
    KWH = 'KWH'
    """Kilowatt hour"""
    DAY = 'DAY'
    """Day"""
    HOUR = 'HOUR'
    """Hour"""
    MINUTE = 'MINUTE'
    """Minute"""
    MONTH = 'MONTH'
    """Month"""
    LITER = 'LITER'
    """Liter"""
    KILOMETER = 'KILOMETER'
    """Kilometer"""
    CUBIC_METER = 'CUBIC_METER'
    """Cubic meter"""
    METER = 'METER'
    """Meter"""
    LINEAR_METER = 'LINEAR_METER'
    """Linear meter"""
    CARTON = 'CARTON'
    """Carton"""
    PACK = 'PACK'
    """Pack"""
    OWN = 'OWN'
    """Own unit of measure"""
