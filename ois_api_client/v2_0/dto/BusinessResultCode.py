from enum import Enum


class BusinessResultCode(Enum):
    """Business result code type"""
    ERROR = 'ERROR'
    """Error"""
    WARN = 'WARN'
    """Warn"""
    INFO = 'INFO'
    """Information"""
