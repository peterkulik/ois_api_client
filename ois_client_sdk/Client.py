from datetime import datetime

from ois_client_sdk.common.parameter.builders.build_request_signature import build_request_signature
from ois_client_sdk.token_exchange.Parameter import Parameter


class Client:
    uri: str
    signature_key: str
    replacement_key: str
    namespace = str

    def __init__(self, uri: str, signature_key: str, replacement_key: str,
                 namespace: str = 'http://schemas.nav.gov.hu/OSA/2.0/api'):
        self.uri = uri
        self.signature_key = signature_key
        self.replacement_key = replacement_key
        self.namespace = namespace

    def token_exchange(self, parameter: Parameter):
        rs = build_request_signature(parameter.header.request_id, parameter.header.timestamp, self.signature_key)
        par = parameter.serialize(rs)

    def call_operation(self):
        # request = (HttpWebRequest)
        # WebRequest.Create($"{uri}/{operation}");
        # request.Method = "POST";
        # request.Accept = "application/xml";
        # request.ContentType = "application/xml";
        # request.ProtocolVersion = HttpVersion.Version10;
        # var
        # requestContent = parameter.Serialize();
        # byte[]
        # postBytes = Encoding.UTF8.GetBytes(requestContent);
        # request.ContentLength = postBytes.Length;
        pass
