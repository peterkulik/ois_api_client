from enum import Enum


class FunctionCode(Enum):
    """Function code type"""
    OK = 'OK'
    """Successful operation"""
    ERROR = 'ERROR'
    """Error"""
