import requests
import xml.etree.ElementTree as ET

from . import GeneralError

from .v3_0 import dto, namespaces as ns
from .v3_0.deserialization.deserialize_query_invoice_data_response import deserialize_query_invoice_data_response
from .v3_0.deserialization.deserialize_query_invoice_digest_response import deserialize_query_invoice_digest_response
from .v3_0.deserialization.deserialize_token_exchange_response import deserialize_token_exchange_response
from .serialization.serialize_query_invoice_data_request import serialize_query_invoice_data_request
from .serialization.serialize_query_invoice_digest_request import serialize_query_invoice_digest_request
from .serialization.serialize_token_exchange_request import serialize_token_exchange_request


class Client:
    def __init__(self, uri: str):
        self._uri = uri
        ET.register_namespace('', ns.API)

    def token_exchange(self, data: dto.BasicOnlineInvoiceRequest) -> dto.TokenExchangeResponse:
        par = serialize_token_exchange_request(data)
        response = self.call_operation('tokenExchange', par)
        root: ET.Element = ET.fromstring(response)
        result = deserialize_token_exchange_response(root)
        return result

    def query_invoice_digest(self, data: dto.QueryInvoiceDigestRequest) -> dto.QueryInvoiceDigestResponse:
        par = serialize_query_invoice_digest_request(data)
        response = self.call_operation('queryInvoiceDigest', par)
        root: ET.Element = ET.fromstring(response)
        result = deserialize_query_invoice_digest_response(root)
        return result

    def query_invoice_data(self, data: dto.QueryInvoiceDataRequest) -> dto.QueryInvoiceDataResponse:
        par = serialize_query_invoice_data_request(data)
        response = self.call_operation('queryInvoiceData', par)
        root: ET.Element = ET.fromstring(response)
        result = deserialize_query_invoice_data_response(root)
        return result

    def call_operation(self, operation: str, parameter: ET.Element) -> str:
        data = ET.tostring(parameter, method='xml', encoding='utf-8')

        with requests.post(url=f'{self._uri}/{operation}',
                           data=data,
                           headers={'Content-Type': 'application/xml',
                                    'Accept': 'application/xml'}) as response:
            if '<GeneralErrorResponse' in response.text:
                response_content = response.content.decode('utf-8')
                raise GeneralError(response_content)

        return response.content.decode('utf-8')
