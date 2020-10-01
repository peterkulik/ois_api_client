from ois_client_sdk.common.parameter.Header import Header
from ois_client_sdk.common.parameter.User import User
from ois_client_sdk.common.parameter.builders.build_request_signature import build_request_signature
from ois_client_sdk.common.parameter.builders.hash_password import hash_password
from ois_client_sdk.token_exchange.Parameter import Parameter
from tests.common.parameter import config


def test_parameter_serialization():

    par = Parameter(
        header=Header(config.request_id, config.request_version, config.header_version, config.timestamp),
        user=User(config.login, config.tax_number),
        software=config.software
    )

    ph = hash_password(config.password)
    rs = build_request_signature(config.request_id, config.timestamp, config.signature_key)
    serialized_parameter = par.serialize(rs, ph)

    print(serialized_parameter)
