from typing import Union
from .DateIntervalParam import DateIntervalParam
from .DateTimeIntervalParam import DateTimeIntervalParam


class MandatoryQueryParams:
    """Mandatory params of the invoice query

    :param parameter: One of the three available options: InvoiceIssueDate, InsDate, OriginalInvoiceNumber
    """

    class InvoiceIssueDate:
        """InvoiceIssueDate parameter

        :param invoice_issue_date: Date range of the invoice issue date
        """

        def __init__(self, invoice_issue_date: DateIntervalParam):
            self.invoice_issue_date = invoice_issue_date

    class InsDate:
        """InsDate parameter

        :param ins_date: Datetime range of processing data exchange in UTC time
        """

        def __init__(self, ins_date: DateTimeIntervalParam):
            self.ins_date = ins_date

    class OriginalInvoiceNumber:
        """OriginalInvoiceNumber parameter

        :param original_invoice_number: Sequence number of the original invoice, on which the modification occurs
        """

        def __init__(self, original_invoice_number: str):
            self.original_invoice_number = original_invoice_number

    def __init__(self, parameter: Union[InvoiceIssueDate, InsDate, OriginalInvoiceNumber]):
        self.parameter = parameter
