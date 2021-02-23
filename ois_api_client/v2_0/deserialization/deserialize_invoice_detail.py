from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ...deserialization.create_enum import create_enum
from ..dto.InvoiceDetail import InvoiceDetail
from ..dto.InvoiceCategory import InvoiceCategory
from ..dto.PaymentMethod import PaymentMethod
from ..dto.InvoiceAppearance import InvoiceAppearance
from .deserialize_additional_data import deserialize_additional_data


def deserialize_invoice_detail(element: ET.Element) -> Optional[InvoiceDetail]:
    if element is None:
        return None

    result = InvoiceDetail(
        invoice_category=create_enum(InvoiceCategory, XR.get_child_text(element, 'invoiceCategory', DATA)),
        invoice_delivery_date=XR.get_child_date(element, 'invoiceDeliveryDate', DATA),
        invoice_delivery_period_start=XR.get_child_date(element, 'invoiceDeliveryPeriodStart', DATA),
        invoice_delivery_period_end=XR.get_child_date(element, 'invoiceDeliveryPeriodEnd', DATA),
        invoice_accounting_delivery_date=XR.get_child_date(element, 'invoiceAccountingDeliveryDate', DATA),
        periodical_settlement=XR.get_child_bool(element, 'periodicalSettlement', DATA),
        small_business_indicator=XR.get_child_bool(element, 'smallBusinessIndicator', DATA),
        currency_code=XR.get_child_text(element, 'currencyCode', DATA),
        exchange_rate=XR.get_child_float(element, 'exchangeRate', DATA),
        self_billing_indicator=XR.get_child_bool(element, 'selfBillingIndicator', DATA),
        payment_method=create_enum(PaymentMethod, XR.get_child_text(element, 'paymentMethod', DATA)),
        payment_date=XR.get_child_date(element, 'paymentDate', DATA),
        cash_accounting_indicator=XR.get_child_bool(element, 'cashAccountingIndicator', DATA),
        invoice_appearance=create_enum(InvoiceAppearance, XR.get_child_text(element, 'invoiceAppearance', DATA)),
        electronic_invoice_hash=XR.get_child_text(element, 'electronicInvoiceHash', DATA),
        additional_invoice_data=[deserialize_additional_data(e) for e in XR.find_all_child(element, 'additionalInvoiceData', DATA)],
    )

    return result
