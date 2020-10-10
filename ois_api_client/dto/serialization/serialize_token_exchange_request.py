from .serialize_basic_online_invoice_request import serialize_basic_online_invoice_request
from .. import TokenExchangeRequest


def serialize_token_exchange_request(data: TokenExchangeRequest, request_signature: str, password_hash: str):
    return serialize_basic_online_invoice_request(data, 'TokenExchangeRequest', request_signature, password_hash)
