from typing import Optional
from typing import List
from dataclasses import dataclass
from .BusinessValidationResult import BusinessValidationResult
from .InvoiceStatus import InvoiceStatus
from .TechnicalValidationResult import TechnicalValidationResult


@dataclass
class ProcessingResult:
    """Invoice processing result

    :param index: Sequence number of the invoice within the request
    :param batch_index: Sequence number of the modification document within the batch
    :param invoice_status: Processing status of the invoice
    :param technical_validation_messages: Technical validation messages
    :param business_validation_messages: Business validation messages
    :param compressed_content_indicator: Indicates if the content of the originalRequest needs to be decompressed to be read following the BASE64 decoding
    :param original_request: Invoice data in BASE64 encoded form
    """

    index: int
    batch_index: Optional[int]
    invoice_status: InvoiceStatus
    technical_validation_messages: Optional[List[TechnicalValidationResult]]
    business_validation_messages: Optional[List[BusinessValidationResult]]
    compressed_content_indicator: bool
    original_request: Optional[str]
