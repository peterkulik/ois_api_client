from datetime import date
from decimal import Decimal
from typing import List

from .AdditionalData import AdditionalData
from .InvoiceCategory import InvoiceCategory
from .PaymentMethod import PaymentMethod
from .InvoiceAppearance import InvoiceAppearance


class InvoiceDetail:
    """Invoice detail data

    :param invoice_category:
    :param invoice_delivery_date:
    :param invoice_delivery_period_start:
    :param invoice_delivery_period_end:
    :param invoice_accounting_delivery_date:
    :param periodical_settlement:
    :param small_business_indicator:
    :param currency_code:
    :param exchange_rate:
    :param self_billing_indicator:
    :param payment_method:
    :param payment_date:
    :param cash_accounting_indicator:
    :param invoice_appearance:
    :param electronic_invoice_hash:
    :param additional_invoice_data:
    """

    def __init__(self, invoice_category: InvoiceCategory, invoice_delivery_date: date,
                 invoice_delivery_period_start: date, invoice_delivery_period_end: date,
                 invoice_accounting_delivery_date: date, periodical_settlement: bool, small_business_indicator: bool,
                 currency_code: str, exchange_rate: Decimal, self_billing_indicator: bool,
                 payment_method: PaymentMethod, payment_date: date, cash_accounting_indicator: bool,
                 invoice_appearance: InvoiceAppearance, electronic_invoice_hash: str,
                 additional_invoice_data: List[AdditionalData]):
        self.invoice_category = invoice_category
        self.invoice_delivery_date = invoice_delivery_date
        self.invoice_delivery_period_start = invoice_delivery_period_start
        self.invoice_delivery_period_end = invoice_delivery_period_end
        self.invoice_accounting_delivery_date = invoice_accounting_delivery_date
        self.periodical_settlement = periodical_settlement
        self.small_business_indicator = small_business_indicator
        self.currency_code = currency_code
        self.exchange_rate = exchange_rate
        self.self_billing_indicator = self_billing_indicator
        self.payment_method = payment_method
        self.payment_date = payment_date
        self.cash_accounting_indicator = cash_accounting_indicator
        self.invoice_appearance = invoice_appearance
        self.electronic_invoice_hash = electronic_invoice_hash
        self.additional_invoice_data = additional_invoice_data
