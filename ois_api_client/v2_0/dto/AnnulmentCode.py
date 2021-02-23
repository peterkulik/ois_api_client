from enum import Enum


class AnnulmentCode(Enum):
    """Technical annulment  code type"""
    ERRATIC_DATA = 'ERRATIC_DATA'
    """Technical annulment due to erratic data content"""
    ERRATIC_INVOICE_NUMBER = 'ERRATIC_INVOICE_NUMBER'
    """Technical annulment due to erratic invoice number"""
    ERRATIC_INVOICE_ISSUE_DATE = 'ERRATIC_INVOICE_ISSUE_DATE'
    """Technical annulment due to erratic invoice issue date"""
