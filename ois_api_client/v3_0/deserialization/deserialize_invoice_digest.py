from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import BASE
from ..namespaces import COMMON
from ..namespaces import API
from ...deserialization.create_enum import create_enum
from ..dto.InvoiceDigest import InvoiceDigest
from ..dto.ManageInvoiceOperation import ManageInvoiceOperation
from ..dto.InvoiceCategory import InvoiceCategory
from ..dto.PaymentMethod import PaymentMethod
from ..dto.InvoiceAppearance import InvoiceAppearance
from ..dto.Source import Source


def deserialize_invoice_digest(element: ET.Element) -> Optional[InvoiceDigest]:
    if element is None:
        return None

    result = InvoiceDigest(
        invoice_number=XR.get_child_text(element, 'invoiceNumber', API),
        batch_index=XR.get_child_int(element, 'batchIndex', API),
        invoice_operation=create_enum(ManageInvoiceOperation, XR.get_child_text(element, 'invoiceOperation', API)),
        invoice_category=create_enum(InvoiceCategory, XR.get_child_text(element, 'invoiceCategory', API)),
        invoice_issue_date=XR.get_child_date(element, 'invoiceIssueDate', API),
        supplier_tax_number=XR.get_child_text(element, 'supplierTaxNumber', API),
        supplier_group_member_tax_number=XR.get_child_text(element, 'supplierGroupMemberTaxNumber', API),
        supplier_name=XR.get_child_text(element, 'supplierName', API),
        customer_tax_number=XR.get_child_text(element, 'customerTaxNumber', API),
        customer_group_member_tax_number=XR.get_child_text(element, 'customerGroupMemberTaxNumber', API),
        customer_name=XR.get_child_text(element, 'customerName', API),
        payment_method=create_enum(PaymentMethod, XR.get_child_text(element, 'paymentMethod', API)),
        payment_date=XR.get_child_date(element, 'paymentDate', API),
        invoice_appearance=create_enum(InvoiceAppearance, XR.get_child_text(element, 'invoiceAppearance', API)),
        source=create_enum(Source, XR.get_child_text(element, 'source', API)),
        invoice_delivery_date=XR.get_child_date(element, 'invoiceDeliveryDate', API),
        currency=XR.get_child_text(element, 'currency', API),
        invoice_net_amount=XR.get_child_float(element, 'invoiceNetAmount', API),
        invoice_net_amount_huf=XR.get_child_float(element, 'invoiceNetAmountHUF', API),
        invoice_vat_amount=XR.get_child_float(element, 'invoiceVatAmount', API),
        invoice_vat_amount_huf=XR.get_child_float(element, 'invoiceVatAmountHUF', API),
        transaction_id=XR.get_child_text(element, 'transactionId', API),
        index=XR.get_child_int(element, 'index', API),
        original_invoice_number=XR.get_child_text(element, 'originalInvoiceNumber', API),
        modification_index=XR.get_child_int(element, 'modificationIndex', API),
        ins_date=XR.get_child_datetime(element, 'insDate', API),
        completeness_indicator=XR.get_child_bool(element, 'completenessIndicator', API),
    )

    return result
