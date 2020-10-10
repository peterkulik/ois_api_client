from datetime import datetime

from .Source import Source
from .OriginalRequestVersion import OriginalRequestVersion


class AuditData:
    """Invoice audit data

    :param ins_date: Insert date in UTC time
    :param ins_cus_user: Inserting technical user name
    :param source: Data exchange source
    :param transaction_id: Transaction ID of the invoice if it was exchanged via M2M interface
    :param index: Sequence number of the invoice within the request
    :param batch_index: Sequence number of the modification document within the batch
    :param original_request_version: requestVersion value of the invoice exchange
    """

    def __init__(self, ins_date: datetime, ins_cus_user: str, source: Source, transaction_id: str, index: int,
                 batch_index: int, original_request_version: OriginalRequestVersion):
        self.ins_date = ins_date
        self.ins_cus_user = ins_cus_user
        self.source = source
        self.transaction_id = transaction_id
        self.index = index
        self.batch_index = batch_index
        self.original_request_version = original_request_version
