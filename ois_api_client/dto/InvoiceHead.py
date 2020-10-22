from typing import Union

from .CustomerInfo import CustomerInfo
from .FiscalRepresentative import FiscalRepresentative
from .InvoiceDetail import InvoiceDetail
from .SupplierInfo import SupplierInfo


class InvoiceHead:
    """Data in header of invoice

    :param supplier_info: Data related to the issuer of the invoice (supplier)
    :param invoice_detail: Invoice detail adata
    :param customer_info: Data related to the customer
    :param fiscal_representative_info: Data related to the fiscal representative
    """

    def __init__(self,
                 supplier_info: SupplierInfo,
                 invoice_detail: InvoiceDetail,
                 customer_info: Union[CustomerInfo, None] = None,
                 fiscal_representative_info: Union[FiscalRepresentative, None] = None):
        self.supplier_info = supplier_info
        self.customer_info = customer_info
        self.fiscal_representative_info = fiscal_representative_info
        self.invoice_detail = invoice_detail
