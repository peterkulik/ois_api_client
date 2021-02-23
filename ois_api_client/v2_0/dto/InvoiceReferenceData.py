from datetime import datetime
from dataclasses import dataclass


@dataclass
class InvoiceReferenceData:
    """Modification or cancellation data

    :param original_invoice_number: Sequence number of the original invoice, on which the modification occurs - section 170 (1) c) of the VAT law
    :param modify_without_master: Indicates whether the modification references to an original invoice which is not and will not be exchanged
    :param modification_timestamp: Creation date timestamp of the modification document in UTC time
    :param modification_index: The unique sequence number referring to the original invoice
    """

    original_invoice_number: str
    modify_without_master: bool
    modification_timestamp: datetime
    modification_index: int
