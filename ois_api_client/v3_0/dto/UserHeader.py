from dataclasses import dataclass
from .Crypto import Crypto


@dataclass
class UserHeader:
    """Authentication data of the request

    :param login: Login name of the technical user
    :param password_hash: Hash value of the technical user's password
    :param tax_number: The taxpayer's tax number, whose name the technical user operates in
    :param request_signature: Hash value of the request's signature
    """

    login: str
    password_hash: Crypto
    tax_number: str
    request_signature: Crypto
