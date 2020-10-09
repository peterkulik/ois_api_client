from .AuditData import AuditData


class InvoiceDataResult:
    """Invoice number based query result

    :param invoice_data: Invoice data in BASE64 encoded form
    :param audit_data: Invoice audit data
    :param compressed_content_indicator: Indicates if the content of the invoice needs to be decompressed to be read following the BASE64 decoding
    """

    def __init__(self, invoice_data: str, audit_data: AuditData, compressed_content_indicator: bool):
        self.invoice_data = invoice_data
        self.audit_data = audit_data
        self.compressed_content_indicator = compressed_content_indicator
