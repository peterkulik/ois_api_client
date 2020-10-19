from enum import Enum


class LineOperation(Enum):
    """Invoice line modification type"""
    CREATE = 'CREATE'
    MODIFY = 'MODIFY'
