from typing import Optional
from datetime import date
from datetime import datetime
from dataclasses import dataclass
from .InvoiceAppearance import InvoiceAppearance
from .InvoiceCategory import InvoiceCategory
from .ManageInvoiceOperation import ManageInvoiceOperation
from .PaymentMethod import PaymentMethod
from .Source import Source


@dataclass
class InvoiceDigest:
    """Digest query result

    :param invoice_number: Sequential number of the original invoice or modifiation document - section 169 (b) or section 170 (1) b) of the VAT law
    :param batch_index: Sequence number of the modification document within the batch
    :param invoice_operation: Invoice operation type
    :param invoice_category: Type of invoice
    :param invoice_issue_date: Invoice or modification document issue date
    :param supplier_tax_number: The supplier's tax number
    :param supplier_group_tax_number: The supplier's group tax number
    :param supplier_name: Name of the seller (supplier)
    :param customer_tax_number: The buyer's tax number
    :param customer_group_tax_number: The buyer's group tax number
    :param customer_name: Name of the customer
    :param payment_method: Method of payment
    :param payment_date: Deadline for payment
    :param invoice_appearance: Form of appearance of the invoice
    :param source: Data exchange source
    :param invoice_delivery_date: Invoice delivery date
    :param currency: Currency of the invoice
    :param invoice_net_amount: Invoice net amount expressed in the currency of the invoice
    :param invoice_net_amount_huf: Invoice net amount expressed in HUF
    :param invoice_vat_amount: Invoice VAT amount expressed in the currency of the invoice
    :param invoice_vat_amount_huf: Invoice VAT amount expressed in HUF
    :param transaction_id: Transaction identifier of the data exchange
    :param index: Sequence number of the invoice within the request
    :param original_invoice_number: Sequence number of the original invoice, on which the modification occurs
    :param modification_index: The unique sequence number referring to the original invoice
    :param ins_date: Insert date in UTC time
    """

    invoice_number: str
    batch_index: Optional[int]
    invoice_operation: ManageInvoiceOperation
    invoice_category: InvoiceCategory
    invoice_issue_date: date
    supplier_tax_number: str
    supplier_group_tax_number: Optional[str]
    supplier_name: str
    customer_tax_number: Optional[str]
    customer_group_tax_number: Optional[str]
    customer_name: Optional[str]
    payment_method: Optional[PaymentMethod]
    payment_date: Optional[date]
    invoice_appearance: Optional[InvoiceAppearance]
    source: Optional[Source]
    invoice_delivery_date: Optional[date]
    currency: Optional[str]
    invoice_net_amount: Optional[float]
    invoice_net_amount_huf: Optional[float]
    invoice_vat_amount: Optional[float]
    invoice_vat_amount_huf: Optional[float]
    transaction_id: Optional[str]
    index: Optional[int]
    original_invoice_number: Optional[str]
    modification_index: Optional[int]
    ins_date: datetime
