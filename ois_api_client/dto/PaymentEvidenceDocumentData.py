from datetime import date

from .Address import Address
from .TaxNumber import TaxNumber


class PaymentEvidenceDocumentData:
    """Data of the document verifying the declaration submitted on the product fee according to the Paragraph (3),
    Section 13 and the Paragraph (3) Section 25 of the Act LXXXV of 2011

    :param evidence_document_no: Sequential number of the invoice, or other document considered as such
    :param evidence_document_date: Date of issue of the invoice
    :param obligated_name: Name of obligator
    :param obligated_address: Address of obligator
    :param obligated_tax_number: Tax number of obligated
    """

    def __init__(self,
                 evidence_document_no: str,
                 evidence_document_date: date,
                 obligated_name: str,
                 obligated_address: Address,
                 obligated_tax_number: TaxNumber):
        self.evidence_document_no = evidence_document_no
        self.evidence_document_date = evidence_document_date
        self.obligated_name = obligated_name
        self.obligated_address = obligated_address
        self.obligated_tax_number = obligated_tax_number
