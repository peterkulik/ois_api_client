from .CustomerInfo import CustomerInfo
from .FiscalRepresentative import FiscalRepresentative
from .InvoiceDetail import InvoiceDetail
from .SupplierInfo import SupplierInfo


class InvoiceHead:
    """Data in header of invoice

    :param supplier_info:
    :param customer_info:
    :param fiscal_representative_info:
    :param invoice_detail:
    """

    def __init__(self, supplier_info: SupplierInfo, customer_info: CustomerInfo,
                 fiscal_representative_info: FiscalRepresentative, invoice_detail: InvoiceDetail):
        self.supplier_info = supplier_info
        self.customer_info = customer_info
        self.fiscal_representative_info = fiscal_representative_info
        self.invoice_detail = invoice_detail
