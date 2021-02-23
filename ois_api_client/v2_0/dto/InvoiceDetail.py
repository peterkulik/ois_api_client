from typing import Optional
from typing import List
from datetime import date
from dataclasses import dataclass
from .AdditionalData import AdditionalData
from .InvoiceAppearance import InvoiceAppearance
from .InvoiceCategory import InvoiceCategory
from .PaymentMethod import PaymentMethod


@dataclass
class InvoiceDetail:
    """Invoice detail data

    :param invoice_category: Type of invoice. In case of modification document the type of original invoice
    :param invoice_delivery_date: Delivery date (if this field does not exist on the invoice, the date of the invoice should be considered as such) - section 169 (g) of the VAT law
    :param invoice_delivery_period_start: The first day of the delivery, if the invoice delivery is a period
    :param invoice_delivery_period_end: The last day of the delivery, if the invoice delivery is a period
    :param invoice_accounting_delivery_date: Date of accounting accomplishment. In the event of a period, the last day of the period
    :param periodical_settlement: Indicates where by agreement of the parties it gives rise to successive statements of account or successive payments relating to the supply of goods, or the supply of services, or if the consideration agreed upon for such goods and/or services applies to specific periods.
    :param small_business_indicator: Marking of low tax-bracket enterprise
    :param currency_code: ISO 4217 currency code on the invoice
    :param exchange_rate: In case any currency is used other than HUF, the applied exchange rate should be mentioned: 1 unit of the foreign currency expressed in HUF
    :param self_billing_indicator: Marking the fact of self-billing (in the case of self-billing the value is true)
    :param payment_method: Method of payment
    :param payment_date: Deadline for payment
    :param cash_accounting_indicator: Marking the fact of cash accounting if this is indicated on the invoice - section 169 (h) of the VAT law. The value is true in case of cash accounting
    :param invoice_appearance: Form of appearance of the invoice or modification document
    :param electronic_invoice_hash: Electronic invoice or modification document file SHA256 hash value
    :param additional_invoice_data: Other data in relation to the invoice
    """

    invoice_category: InvoiceCategory
    invoice_delivery_date: date
    invoice_delivery_period_start: Optional[date]
    invoice_delivery_period_end: Optional[date]
    invoice_accounting_delivery_date: Optional[date]
    periodical_settlement: Optional[bool]
    small_business_indicator: Optional[bool]
    currency_code: str
    exchange_rate: float
    self_billing_indicator: Optional[bool]
    payment_method: Optional[PaymentMethod]
    payment_date: Optional[date]
    cash_accounting_indicator: Optional[bool]
    invoice_appearance: InvoiceAppearance
    electronic_invoice_hash: Optional[str]
    additional_invoice_data: Optional[List[AdditionalData]]
