from typing import List
from dataclasses import dataclass
from .InvoiceOperation import InvoiceOperation


@dataclass
class InvoiceOperationList:
    """Batch invoice operations of the request

    :param compressed_content: Compressed content indicator for the processing flow
    :param invoice_operation: Invoice operation of the request
    """

    compressed_content: bool
    invoice_operation: List[InvoiceOperation]
