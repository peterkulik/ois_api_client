import uuid
from dataclasses import dataclass
from typing import Tuple, Callable, Optional
from datetime import datetime
from .constants import PASSWORD_HASH_CRYPTO_TYPE, REQUEST_SIGNATURE_CRYPTO_TYPE, REQUEST_VERSION, HEADER_VERSION
from .serialization.build_request_signature import build_request_signature
from .serialization.hash_password import hash_password

from .v3_0 import dto


@dataclass
class HeaderFactoryParameters:
    login: str
    tax_number: str
    password: str
    signature_key: str


def _generate_request_id() -> str:
    return f'{datetime.now().strftime("%Y%m%dT%H%M%S%f")}_{str(uuid.uuid4()).replace("-", "")}'[0:30]


def _generate_timestamp() -> datetime:
    return datetime.now()


def make_default_header_factory(
        load_parameters: Callable[[], HeaderFactoryParameters]) -> Callable[[], Tuple[dto.BasicHeader, dto.UserHeader]]:
    return make_header_factory(load_parameters=load_parameters)


def make_header_factory(
        load_parameters: Callable[[], HeaderFactoryParameters]
) -> Callable[[Optional[str], Optional[datetime]], Tuple[dto.BasicHeader, dto.UserHeader]]:
    def _(request_id: Optional[str] = None,
          timestamp: Optional[datetime] = None) -> Tuple[dto.BasicHeader, dto.UserHeader]:
        p = load_parameters()

        if not request_id:
            request_id = _generate_request_id()

        if not timestamp:
            timestamp = _generate_timestamp()

        return dto.BasicHeader(
            request_id=request_id,
            timestamp=timestamp,
            request_version=REQUEST_VERSION,
            header_version=HEADER_VERSION
        ), dto.UserHeader(
            login=p.login,
            password_hash=dto.Crypto(
                value=hash_password(p.password),
                crypto_type=PASSWORD_HASH_CRYPTO_TYPE),
            tax_number=p.tax_number,
            request_signature=dto.Crypto(
                value=build_request_signature(
                    request_id=request_id,
                    timestamp=timestamp,
                    signature_key=p.signature_key),
                crypto_type=REQUEST_SIGNATURE_CRYPTO_TYPE)
        )

    return _
