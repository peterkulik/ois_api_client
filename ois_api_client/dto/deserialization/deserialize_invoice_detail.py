import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from .deserialize_additional_data import deserialize_additional_data
from ..InvoiceDetail import InvoiceDetail
from ..InvoiceCategory import InvoiceCategory
from ..InvoiceAppearance import InvoiceAppearance
from ..PaymentMethod import PaymentMethod
from ...constants import NAMESPACE_DATA


def deserialize_invoice_detail(element: ET.Element) -> Union[InvoiceDetail, None]:
    if element is None:
        return None

    invoice_category = XR.get_child_text(element, 'invoiceCategory', NAMESPACE_DATA)
    invoice_appearance = XR.get_child_text(element, 'invoiceAppearance', NAMESPACE_DATA)
    payment_method = XR.get_child_text(element, 'paymentMethod', NAMESPACE_DATA)

    result = InvoiceDetail(
        invoice_category=InvoiceCategory(invoice_category) if invoice_category is not None else None,
        invoice_delivery_date=XR.get_child_date(element, 'invoiceDeliveryDate', NAMESPACE_DATA),
        currency_code=XR.get_child_text(element, 'currencyCode', NAMESPACE_DATA),
        exchange_rate=XR.get_child_float(element, 'exchangeRate', NAMESPACE_DATA),
        invoice_appearance=InvoiceAppearance(invoice_appearance) if invoice_appearance is not None else None,
        invoice_delivery_period_start=XR.get_child_date(element, 'invoiceDeliveryPeriodStart', NAMESPACE_DATA),
        invoice_delivery_period_end=XR.get_child_date(element, 'invoiceDeliveryPeriodEnd', NAMESPACE_DATA),
        invoice_accounting_delivery_date=XR.get_child_date(element, 'invoiceAccountingDeliveryDate', NAMESPACE_DATA),
        periodical_settlement=XR.get_child_bool(element, 'periodicalSettlement', NAMESPACE_DATA, False),
        small_business_indicator=XR.get_child_bool(element, 'smallBusinessIndicator', NAMESPACE_DATA, False),
        self_billing_indicator=XR.get_child_bool(element, 'selfBillingIndicator', NAMESPACE_DATA, False),
        payment_method=PaymentMethod(payment_method) if payment_method is not None else None,
        payment_date=XR.get_child_date(element, 'paymentDate', NAMESPACE_DATA),
        cash_accounting_indicator=XR.get_child_bool(element, 'cashAccountingIndicator', NAMESPACE_DATA, False),
        electronic_invoice_hash=XR.get_child_text(element, 'electronicInvoiceHash', NAMESPACE_DATA),
        additional_invoice_data=[deserialize_additional_data(el) for el in
                                 XR.find_all_child(element, 'additionalInvoiceData', NAMESPACE_DATA)]
    )

    return result
