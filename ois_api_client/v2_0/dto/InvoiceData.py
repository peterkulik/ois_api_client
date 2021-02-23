from datetime import date
from dataclasses import dataclass
from .InvoiceMain import InvoiceMain


@dataclass
class InvoiceData:
    """Invoice exchange data

    :param invoice_number: Sequential number of the original invoice or modifiation document - section 169 (b) or section 170 (1) b) of the VAT law
    :param invoice_issue_date: Date of issue of the invoice or the modification document - section 169 (a) of the VAT law, section 170 (1) a) of the VAT law
    :param invoice_main: None
    """

    invoice_number: str
    invoice_issue_date: date
    invoice_main: InvoiceMain
