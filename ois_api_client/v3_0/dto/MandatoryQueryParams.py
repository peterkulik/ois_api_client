from typing import Optional
from dataclasses import dataclass
from .DateIntervalParam import DateIntervalParam
from .DateTimeIntervalParam import DateTimeIntervalParam


@dataclass
class MandatoryQueryParams:
    """Mandatory params of the invoice query

    :param invoice_issue_date: Date range of the invoice issue date
    :param ins_date: Datetime range of processing data exchange in UTC time
    :param original_invoice_number: Sequence number of the original invoice, on which the modification occurs
    """

    invoice_issue_date: Optional[DateIntervalParam]
    ins_date: Optional[DateTimeIntervalParam]
    original_invoice_number: Optional[str]
