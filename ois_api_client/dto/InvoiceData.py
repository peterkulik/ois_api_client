from datetime import date

from .InvoiceMain import InvoiceMain


class InvoiceData:
    """Invoice exchange data

    :param invoice_number: Sequential number of the original invoice or modifiation document - section 169 (b) or section 170 (1) b) of the VAT law
    :param invoice_issue_date: Date of issue of the invoice or the modification document - section 169 (a) of the VAT law, section 170 (1) a) of the VAT law
    :param invoice_main: A common type to describe invoice information
    """

    def __init__(self, invoice_number: str, invoice_issue_date: date, invoice_main: InvoiceMain):
        self.invoiceNumber = invoice_number
        self.invoiceIssueDate = invoice_issue_date
        self.invoiceMain = invoice_main
