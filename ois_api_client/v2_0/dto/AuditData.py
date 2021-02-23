from typing import Optional
from datetime import datetime
from dataclasses import dataclass
from .OriginalRequestVersion import OriginalRequestVersion
from .Source import Source


@dataclass
class AuditData:
    """Invoice audit data

    :param insdate: Insert date in UTC time
    :param ins_cus_user: Inserting technical user name
    :param source: Data exchange source
    :param transaction_id: Transaction ID of the invoice if it was exchanged via M2M interface
    :param index: Sequence number of the invoice within the request
    :param batch_index: Sequence number of the modification document within the batch
    :param original_request_version: None
    """

    insdate: datetime
    ins_cus_user: str
    source: Source
    transaction_id: Optional[str]
    index: Optional[int]
    batch_index: Optional[int]
    original_request_version: OriginalRequestVersion
