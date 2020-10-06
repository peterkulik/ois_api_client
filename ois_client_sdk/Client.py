import requests
import xml.etree.ElementTree as ET

from .constants import NAMESPACE
from .dto.deserialization.deserialize_token_exchange_response import deserialize_token_exchange_response
from .dto.serialization.build_request_signature import build_request_signature
from .dto.serialization.hash_password import hash_password
from .dto.serialization.serialize_token_exchange_request import serialize_token_exchange_request
from .dto.TokenExchangeRequest import TokenExchangeRequest
from .exceptions.GeneralError import GeneralError


class Client:
    def __init__(self, uri: str, signature_key: str, replacement_key: str, password: str):
        self._uri = uri
        self._signature_key = signature_key
        self._replacement_key = replacement_key
        self._password_hash = hash_password(password)
        ET.register_namespace('', NAMESPACE)

    def token_exchange(self, data: TokenExchangeRequest):
        rs = build_request_signature(data.header.request_id, data.header.timestamp, self._signature_key)
        par = serialize_token_exchange_request(data, rs, self._password_hash)
        response = self.call_operation('tokenExchange', par)
        result = deserialize_token_exchange_response(response)
        return result

    def call_operation(self, operation: str, parameter: ET.Element) -> str:
        data = ET.tostring(parameter, method='xml', encoding='utf-8', xml_declaration=True)

        with requests.post(url=f'{self._uri}/{operation}',
                           data=data,
                           headers={'Content-Type': 'application/xml',
                                    'Accept': 'application/xml'}) as response:
            if '<GeneralErrorResponse' in response.text:
                raise GeneralError(response.content.decode('utf-8'))

        return response.content.decode('utf-8')
