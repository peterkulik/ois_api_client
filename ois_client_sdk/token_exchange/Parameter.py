from dataclasses import dataclass

from ois_client_sdk.common.parameter.Base import Base


@dataclass
class Parameter(Base):
    @property
    def root_element(self) -> str:
        return 'TokenExchangeRequest'
