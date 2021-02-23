from typing import Optional
from dataclasses import dataclass
from .CustomerInfo import CustomerInfo
from .FiscalRepresentative import FiscalRepresentative
from .InvoiceDetail import InvoiceDetail
from .SupplierInfo import SupplierInfo


@dataclass
class InvoiceHead:
    """Data in header of invoice

    :param supplier_info: Data related to the issuer of the invoice (supplier)
    :param customer_info: Data related to the customer
    :param fiscal_representative_info: Data related to the fiscal representative
    :param invoice_detail: Invoice detail adata
    """

    supplier_info: SupplierInfo
    customer_info: Optional[CustomerInfo]
    fiscal_representative_info: Optional[FiscalRepresentative]
    invoice_detail: InvoiceDetail
