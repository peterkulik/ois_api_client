from decimal import Decimal
from datetime import date, datetime
from .InvoiceAppearance import InvoiceAppearance
from .InvoiceCategory import InvoiceCategory
from .ManageInvoiceOperation import ManageInvoiceOperation
from .PaymentMethod import PaymentMethod
from .Source import Source


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

    def __init__(self, invoice_number: str, batch_index: int, invoice_operation: ManageInvoiceOperation,
                 invoice_category: InvoiceCategory, invoice_issue_date: date, supplier_tax_number: str,
                 supplier_group_tax_number: str, supplier_name: str, customer_tax_number: str,
                 customer_group_tax_number: str, customer_name: str, payment_method: PaymentMethod, payment_date: date,
                 invoice_appearance: InvoiceAppearance, source: Source, invoice_delivery_date: date, currency: str,
                 invoice_net_amount: Decimal, invoice_net_amount_huf: Decimal, invoice_vat_amount: Decimal,
                 invoice_vat_amount_huf: Decimal, transaction_id: str, index: int, original_invoice_number: str,
                 modification_index: int, ins_date: datetime):
        self.invoice_number = invoice_number
        self.batch_index = batch_index
        self.invoice_operation = invoice_operation
        self.invoice_category = invoice_category
        self.invoice_issue_date = invoice_issue_date
        self.supplier_tax_number = supplier_tax_number
        self.supplier_group_tax_number = supplier_group_tax_number
        self.supplier_name = supplier_name
        self.customer_tax_number = customer_tax_number
        self.customer_group_tax_number = customer_group_tax_number
        self.customer_name = customer_name
        self.payment_method = payment_method
        self.payment_date = payment_date
        self.invoice_appearance = invoice_appearance
        self.source = source
        self.invoice_delivery_date = invoice_delivery_date
        self.currency = currency
        self.invoice_net_amount = invoice_net_amount
        self.invoice_net_amount_huf = invoice_net_amount_huf
        self.invoice_vat_amount = invoice_vat_amount
        self.invoice_vat_amount_huf = invoice_vat_amount_huf
        self.transaction_id = transaction_id
        self.index = index
        self.original_invoice_number = original_invoice_number
        self.modification_index = modification_index
        self.ins_date = ins_date
