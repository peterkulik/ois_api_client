from dataclasses import dataclass


@dataclass
class UserHeader:
    """Authentication data of the request

    :param login: Login name of the technical user
    :param password_hash: Uppercase SHA2-512 hash value of the technical user's password
    :param tax_number: The taxpayer's tax number, whose name the technical user operates in
    :param request_signature: Uppercase SHA3-512 hash value of the request's signature
    """

    login: str
    password_hash: str
    tax_number: str
    request_signature: str
