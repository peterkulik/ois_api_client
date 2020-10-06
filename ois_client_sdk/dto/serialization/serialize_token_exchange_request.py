from .serialize_basic import serialize_basic
from ..TokenExchangeRequest import TokenExchangeRequest


def serialize_token_exchange_request(data: TokenExchangeRequest, request_signature: str, password_hash: str):
    return serialize_basic(data, 'TokenExchangeRequest', request_signature, password_hash)
