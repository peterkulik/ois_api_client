from datetime import date
from dataclasses import dataclass
from .Address import Address
from .TaxNumber import TaxNumber


@dataclass
class PaymentEvidenceDocumentData:
    """Data of the document verifying the declaration submitted on the product fee according to the Paragraph (3), Section 13 and the Paragraph (3) Section 25 of the Act LXXXV of 2011

    :param evidence_document_no: Sequential number of the invoice, or other document considered as such
    :param evidence_document_date: Date of issue of the invoice
    :param obligated_name: Name of obligator
    :param obligated_address: Address of obligator
    :param obligated_tax_number: Tax number of obligated
    """

    evidence_document_no: str
    evidence_document_date: date
    obligated_name: str
    obligated_address: Address
    obligated_tax_number: TaxNumber
