from enum import Enum


class TechnicalResultCode(Enum):
    """Technical result code type"""
    CRITICAL = 'CRITICAL'
    """Critical error"""
    ERROR = 'ERROR'
    """Error"""
