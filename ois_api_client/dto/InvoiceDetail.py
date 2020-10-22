from datetime import date
from typing import List, Union

from .AdditionalData import AdditionalData
from .InvoiceCategory import InvoiceCategory
from .PaymentMethod import PaymentMethod
from .InvoiceAppearance import InvoiceAppearance


class InvoiceDetail:
    """Invoice detail data

    :param invoice_category:
    :param invoice_delivery_date:
    :param currency_code:
    :param exchange_rate:
    :param invoice_appearance:
    :param invoice_delivery_period_start:
    :param invoice_delivery_period_end:
    :param invoice_accounting_delivery_date:
    :param periodical_settlement:
    :param small_business_indicator:
    :param self_billing_indicator:
    :param payment_method:
    :param payment_date:
    :param cash_accounting_indicator:
    :param electronic_invoice_hash:
    :param additional_invoice_data:
    """

    def __init__(self,
                 invoice_category: InvoiceCategory,
                 invoice_delivery_date: date,
                 currency_code: str,
                 exchange_rate: float,
                 invoice_appearance: InvoiceAppearance,
                 invoice_delivery_period_start: Union[date, None] = None,
                 invoice_delivery_period_end: Union[date, None] = None,
                 invoice_accounting_delivery_date: Union[date, None] = None,
                 periodical_settlement: bool = False,
                 small_business_indicator: bool = False,
                 self_billing_indicator: bool = False,
                 payment_method: Union[PaymentMethod, None] = None,
                 payment_date: Union[date, None] = None,
                 cash_accounting_indicator: bool = False,
                 electronic_invoice_hash: Union[str, None] = None,
                 additional_invoice_data: Union[List[AdditionalData], None] = None):
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
