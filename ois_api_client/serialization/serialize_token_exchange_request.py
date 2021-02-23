from .serialize_basic_online_invoice_request import serialize_basic_online_invoice_request
from ..v3_0.dto.BasicOnlineInvoiceRequest import BasicOnlineInvoiceRequest


def serialize_token_exchange_request(data: BasicOnlineInvoiceRequest):
    return serialize_basic_online_invoice_request(data, 'TokenExchangeRequest')
