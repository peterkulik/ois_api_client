from datetime import date
from typing import List, Optional

from .AdditionalData import AdditionalData
from .ConventionalInvoiceInfo import ConventionalInvoiceInfo
from .InvoiceCategory import InvoiceCategory
from .PaymentMethod import PaymentMethod
from .InvoiceAppearance import InvoiceAppearance


class InvoiceDetail:
    """Invoice detail data

    :param invoice_category: Type of invoice. In case of modification document the type of original invoice
    :param invoice_delivery_date: Delivery date (if this field does not exist on the invoice, the date of the invoice should be considered as such) - section 169 (g) of the VAT law
    :param currency_code: ISO 4217 currency code on the invoice
    :param exchange_rate: In case any currency is used other than HUF, the applied exchange rate should be mentioned: 1 unit of the foreign currency expressed in HUF
    :param invoice_appearance: Form of appearance of the invoice or modification document
    :param invoice_delivery_period_start: The first day of the delivery, if the invoice delivery is a period
    :param invoice_delivery_period_end: The last day of the delivery, if the invoice delivery is a period
    :param invoice_accounting_delivery_date: Date of accounting accomplishment. In the event of a period, the last day of the period
    :param periodical_settlement: Indicates where by agreement of the parties it gives rise to successive statements of account or successive payments relating to the supply of goods, or the supply of services, or if the consideration agreed upon for such goods and
    :param small_business_indicator: Marking of low tax-bracket enterprise
    :param utility_settlement_indicator: Marking the fact of utility settlement invoice (invoice according to Act CLXXXVIII of 2013)
    :param self_billing_indicator: Marking the fact of self-billing (in the case of self-billing the value is true)
    :param payment_method: Method of payment
    :param payment_date: Deadline for payment
    :param cash_accounting_indicator: Marking the fact of cash accounting if this is indicated on the invoice - section 169 (h) of the VAT law. The value is true in case of cash accounting
    :param conventional_invoice_info: Other conventionally named data to assist in invoice processing
    :param additional_invoice_data: Other data in relation to the invoice
    """

    def __init__(self,
                 invoice_category: InvoiceCategory,
                 invoice_delivery_date: date,
                 currency_code: str,
                 exchange_rate: float,
                 invoice_appearance: InvoiceAppearance,
                 invoice_delivery_period_start: Optional[date] = None,
                 invoice_delivery_period_end: Optional[date] = None,
                 invoice_accounting_delivery_date: Optional[date] = None,
                 periodical_settlement: Optional[bool] = None,
                 small_business_indicator: Optional[bool] = None,
                 utility_settlement_indicator: Optional[bool] = None,
                 self_billing_indicator: Optional[bool] = None,
                 payment_method: Optional[PaymentMethod] = None,
                 payment_date: Optional[date] = None,
                 cash_accounting_indicator: Optional[bool] = None,
                 conventional_invoice_info: Optional[ConventionalInvoiceInfo] = None,
                 additional_invoice_data: Optional[List[AdditionalData]] = None):
        self.invoice_category = invoice_category
        self.invoice_delivery_date = invoice_delivery_date
        self.invoice_delivery_period_start = invoice_delivery_period_start
        self.invoice_delivery_period_end = invoice_delivery_period_end
        self.invoice_accounting_delivery_date = invoice_accounting_delivery_date
        self.periodical_settlement = periodical_settlement
        self.small_business_indicator = small_business_indicator
        self.utility_settlement_indicator = utility_settlement_indicator
        self.currency_code = currency_code
        self.exchange_rate = exchange_rate
        self.self_billing_indicator = self_billing_indicator
        self.payment_method = payment_method
        self.payment_date = payment_date
        self.cash_accounting_indicator = cash_accounting_indicator
        self.conventional_invoice_info = conventional_invoice_info
        self.invoice_appearance = invoice_appearance
        self.additional_invoice_data = additional_invoice_data
