import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from ..InvoiceAppearance import InvoiceAppearance
from ..InvoiceCategory import InvoiceCategory
from ..InvoiceDigest import InvoiceDigest
from ..InvoiceDigestResult import InvoiceDigestResult
from ..ManageInvoiceOperation import ManageInvoiceOperation
from ..PaymentMethod import PaymentMethod
from ..Source import Source


def _deserialize_invoice_digest(el: ET.Element) -> InvoiceDigest:
    return InvoiceDigest(
        invoice_number=XR.get_child_text(el, 'invoiceNumber'),
        batch_index=XR.get_child_int(el, 'batchIndex'),
        invoice_operation=ManageInvoiceOperation[XR.get_child_text(el, 'invoiceOperation')],
        invoice_category=InvoiceCategory[XR.get_child_text(el, 'invoiceCategory')],
        invoice_issue_date=XR.get_child_date(el, 'invoiceIssueDate'),
        supplier_tax_number=XR.get_child_text(el, 'supplierTaxNumber'),
        supplier_group_tax_number=XR.get_child_text(el, 'supplierGroupTaxNumber'),
        supplier_name=XR.get_child_text(el, 'supplierName'),
        customer_tax_number=XR.get_child_text(el, 'customerTaxNumber'),
        customer_group_tax_number=XR.get_child_text(el, 'customerGroupTaxNumber'),
        customer_name=XR.get_child_text(el, 'customerName'),
        payment_method=PaymentMethod(XR.get_child_text(el, 'paymentMethod')),
        payment_date=XR.get_child_date(el, 'paymentDate'),
        invoice_appearance=InvoiceAppearance(XR.get_child_text(el, 'invoiceAppearance')),
        source=Source(XR.get_child_text(el, 'source')),
        invoice_delivery_date=XR.get_child_date(el, 'invoiceDeliveryDate'),
        currency=XR.get_child_text(el, 'currency'),
        invoice_net_amount=XR.get_child_decimal(el, 'invoiceNetAmount'),
        invoice_net_amount_huf=XR.get_child_decimal(el, 'invoiceNetAmountHUF'),
        invoice_vat_amount=XR.get_child_decimal(el, 'invoiceVatAmount'),
        invoice_vat_amount_huf=XR.get_child_decimal(el, 'invoiceVatAmountHUF'),
        transaction_id=XR.get_child_text(el, 'transactionId'),
        index=XR.get_child_int(el, 'index'),
        original_invoice_number=XR.get_child_text(el, 'originalInvoiceNumber'),
        modification_index=XR.get_child_int(el, 'modificationIndex'),
        ins_date=XR.get_child_utc_datetime(el, 'insDate')
    )


def deserialize_invoice_digest_result(parent: ET.Element) -> Union[InvoiceDigestResult, None]:
    idr_el = XR.find_child(parent, 'invoiceDigestResult')

    if idr_el is None:
        return None

    id_els = XR.find_all_child(idr_el, 'invoiceDigest')

    result = InvoiceDigestResult(
        current_page=XR.get_child_int(idr_el, 'currentPage'),
        available_page=XR.get_child_int(idr_el, 'availablePage'),
        invoice_digest=[_deserialize_invoice_digest(id_el) for id_el in id_els]
    )

    return result
