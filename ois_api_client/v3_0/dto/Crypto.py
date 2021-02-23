from dataclasses import dataclass


@dataclass
class Crypto:
    """Denoting type of cryptographic method

    :param value: Value of Crypto
    :param crypto_type: string attribute

    """

    value: str
    crypto_type: str
