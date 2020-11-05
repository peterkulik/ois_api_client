from enum import Enum


class SoftwareOperation(Enum):
    """Billing operation type (local program or online billing service)"""
    LOCAL_SOFTWARE = 'LOCAL_SOFTWARE'
    """Local program"""
    ONLINE_SERVICE = 'ONLINE_SERVICE'
    """Online billing service"""
