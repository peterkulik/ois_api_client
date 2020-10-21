from typing import Union

from .InvoiceCategory import InvoiceCategory
from .PaymentMethod import PaymentMethod
from .InvoiceAppearance import InvoiceAppearance
from .Source import Source


class AdditionalQueryParams:
    """Additional params of the invoice query

    :param tax_number: Tax number of the supplier or the customer of the invoice (the search criteria depends on the value of the invoiceDirection tag)
    :param group_member_tax_number:  Tax number of group member of the supplier or the customer of the invoice (the search criteria depends on the value of the invoiceDirection tag)
    :param name: Query param of the supplier or the customer of the invoice for leading match pattern (the search criteria depends on the value of the invoiceDirection tag)
    :param invoice_category: Type of invoice
    :param payment_method: Method of payment
    :param invoice_appearance: Form of appearance of the invoice
    :param source: Data exchange source
    :param currency: Currency of the invoice
    """

    def __init__(self, tax_number: Union[str, None] = None, group_member_tax_number: Union[str, None] = None,
                 name: Union[str, None] = None, invoice_category: Union[InvoiceCategory, None] = None,
                 payment_method: Union[PaymentMethod, None] = None,
                 invoice_appearance: Union[InvoiceAppearance, None] = None, source: Union[Source, None] = None,
                 currency: Union[str, None] = None):
        self.tax_number = tax_number
        self.group_member_tax_number = group_member_tax_number
        self.name = name
        self.invoice_category = invoice_category
        self.payment_method = payment_method
        self.invoice_appearance = invoice_appearance
        self.source = source
        self.currency = currency
