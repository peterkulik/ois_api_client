from datetime import datetime
from dataclasses import dataclass
from .AnnulmentCode import AnnulmentCode


@dataclass
class InvoiceAnnulment:
    """Data of technical annulment concerning previous data exchange

    :param annulment_reference: Sequential number of the invoice or modification document to be annuled
    :param annulment_timestamp: Timestamp of the technical annulment in UTC time
    :param annulment_code: Technical annulment code
    :param annulment_reason: Technical annulment reason
    """

    annulment_reference: str
    annulment_timestamp: datetime
    annulment_code: AnnulmentCode
    annulment_reason: str
