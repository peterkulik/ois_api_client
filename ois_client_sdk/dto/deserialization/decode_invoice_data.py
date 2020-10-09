from base64 import b64decode


def decode_invoice_data(data: str) -> str:
    return b64decode(data).decode(encoding='utf-8')
