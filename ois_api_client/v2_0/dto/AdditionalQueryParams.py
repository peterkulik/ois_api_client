from typing import Optional
from dataclasses import dataclass
from .InvoiceAppearance import InvoiceAppearance
from .InvoiceCategory import InvoiceCategory
from .PaymentMethod import PaymentMethod
from .Source import Source


@dataclass
class AdditionalQueryParams:
    """Additional params of the invoice query

    :param tax_number: Tax number of the supplier or the customer of the invoice (the search criteria depends on the value of the invoiceDirection tag)
    :param group_member_tax_number: Tax number of group member of the supplier or the customer of the invoice (the search criteria depends on the value of the invoiceDirection tag)
    :param name: Query param of the supplier or the customer of the invoice for leading match pattern (the search criteria depends on the value of the invoiceDirection tag)
    :param invoice_category: Type of invoice
    :param payment_method: Method of payment
    :param invoice_appearance: Form of appearance of the invoice
    :param source: Data exchange source
    :param currency: Currency of the invoice
    """

    tax_number: Optional[str]
    group_member_tax_number: Optional[str]
    name: Optional[str]
    invoice_category: Optional[InvoiceCategory]
    payment_method: Optional[PaymentMethod]
    invoice_appearance: Optional[InvoiceAppearance]
    source: Optional[Source]
    currency: Optional[str]
