from datetime import date
from dataclasses import dataclass
from .InvoiceMain import InvoiceMain


@dataclass
class InvoiceData:
    """Invoice exchange data

    :param invoice_number: Sequential number of the original invoice or modification document - section 169 (b) or section 170 (1) b) of the VAT law
    :param invoice_issue_date: Date of issue of the invoice or the modification document - section 169 (a) of the VAT law, section 170 (1) a) of the VAT law
    :param completeness_indicator: Indicates whether the data exchange is identical with the invoice (the invoice does not contain any more data)
    :param invoice_main: A common type to describe invoice information
    """

    invoice_number: str
    invoice_issue_date: date
    completeness_indicator: bool
    invoice_main: InvoiceMain
