from enum import Enum


class AnnulmentVerificationStatus(Enum):
    """Verification status of technial annulment requests"""
    NOT_VERIFIABLE = 'NOT_VERIFIABLE'
    """The technical annulment is not verifiable due to client error"""
    VERIFICATION_PENDING = 'VERIFICATION_PENDING'
    """The technical annulment is awaiting verification"""
    VERIFICATION_DONE = 'VERIFICATION_DONE'
    """The technical annulment has been verified"""
    VERIFICATION_REJECTED = 'VERIFICATION_REJECTED'
    """The technical annulment has been rejected"""
