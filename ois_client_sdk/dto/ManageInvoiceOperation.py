from enum import Enum


class ManageInvoiceOperation(Enum):
    """Invoice operation type"""
    CREATE = 'CREATE'  # Original invoice exchange
    MODIFY = 'MODIFY'  # Modification invoice exchange
    STORNO = 'STORNO'  # Exchange concerning invoice invalidation
