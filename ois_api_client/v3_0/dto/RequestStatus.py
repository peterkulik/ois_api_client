from enum import Enum


class RequestStatus(Enum):
    """Processing status of the request"""
    RECEIVED = 'RECEIVED'
    """Received"""
    PROCESSING = 'PROCESSING'
    """Processing"""
    SAVED = 'SAVED'
    """Saved"""
    FINISHED = 'FINISHED'
    """Finished processing"""
    NOTIFIED = 'NOTIFIED'
    """Notified"""
