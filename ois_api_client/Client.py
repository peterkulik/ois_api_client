import requests
import xml.etree.ElementTree as ET

from .constants import NAMESPACE

from . import QueryInvoiceDataRequest
from . import QueryInvoiceDataResponse
from . import QueryInvoiceDigestRequest
from . import QueryInvoiceDigestResponse
from . import TokenExchangeRequest
from . import TokenExchangeResponse

from . import build_request_signature
from . import hash_password
from . import GeneralError

from .dto.deserialization.deserialize_query_invoice_data_response import deserialize_query_invoice_data_response
from .dto.deserialization.deserialize_query_invoice_digest_response import deserialize_query_invoice_digest_response
from .dto.deserialization.deserialize_token_exchange_response import deserialize_token_exchange_response
from .dto.serialization.serialize_query_invoice_data_request import serialize_query_invoice_data_request
from .dto.serialization.serialize_query_invoice_digest_request import serialize_query_invoice_digest_request
from .dto.serialization.serialize_token_exchange_request import serialize_token_exchange_request


class Client:
    def __init__(self, uri: str, signature_key: str, replacement_key: str, password: str):
        self._uri = uri
        self._signature_key = signature_key
        self._replacement_key = replacement_key
        self._password_hash = hash_password(password)
        ET.register_namespace('', NAMESPACE)

    def token_exchange(self, data: TokenExchangeRequest) -> TokenExchangeResponse:
        rs = build_request_signature(data.header.request_id, data.header.timestamp, self._signature_key)
        par = serialize_token_exchange_request(data, rs, self._password_hash)
        response = self.call_operation('tokenExchange', par)
        result = deserialize_token_exchange_response(response)
        return result

    def query_invoice_digest(self, data: QueryInvoiceDigestRequest) -> QueryInvoiceDigestResponse:
        rs = build_request_signature(data.header.request_id, data.header.timestamp, self._signature_key)
        par = serialize_query_invoice_digest_request(data, rs, self._password_hash)
        response = self.call_operation('queryInvoiceDigest', par)
        result = deserialize_query_invoice_digest_response(response)
        return result

    def query_invoice_data(self, data: QueryInvoiceDataRequest) -> QueryInvoiceDataResponse:
        rs = build_request_signature(data.header.request_id, data.header.timestamp, self._signature_key)
        par = serialize_query_invoice_data_request(data, rs, self._password_hash)
        response = self.call_operation('queryInvoiceData', par)
        result = deserialize_query_invoice_data_response(response)
        return result

    def call_operation(self, operation: str, parameter: ET.Element) -> str:
        data = ET.tostring(parameter, method='xml', encoding='utf-8', xml_declaration=True)

        with requests.post(url=f'{self._uri}/{operation}',
                           data=data,
                           headers={'Content-Type': 'application/xml',
                                    'Accept': 'application/xml'}) as response:
            if '<GeneralErrorResponse' in response.text:
                response_content = response.content.decode('utf-8')
                raise GeneralError(response_content)

        return response.content.decode('utf-8')
