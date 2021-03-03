import gzip
from base64 import b64decode
from ois_api_client.v3_0 import dto


def decode_invoice_data(invoice_data_result: dto.InvoiceDataResult) -> str:
    bytes_ = b64decode(invoice_data_result.invoice_data)

    if invoice_data_result.compressed_content_indicator:
        bytes_ = gzip.decompress(bytes_)

    return bytes_.decode(encoding='utf-8')
