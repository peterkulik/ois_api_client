import xml.etree.ElementTree as ET
from datetime import datetime

from ois_client_sdk.common.parameter.Base import Base


class Parameter(Base):
    @property
    def root_element(self) -> str:
        return 'TokenExchangeRequest'
