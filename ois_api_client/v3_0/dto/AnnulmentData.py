from typing import Optional
from datetime import datetime
from dataclasses import dataclass
from .AnnulmentVerificationStatus import AnnulmentVerificationStatus


@dataclass
class AnnulmentData:
    """Status data of technical annulment

    :param annulment_verification_status: Verification status of technical annulment requests
    :param annulment_decision_date: Date of verification or rejection of the technical annulment in UTC time
    :param annulment_decision_user: Login name of the user deciding over the technical annulment's verification or rejection
    """

    annulment_verification_status: AnnulmentVerificationStatus
    annulment_decision_date: Optional[datetime]
    annulment_decision_user: Optional[str]
