import xml.etree.ElementTree as ET
from abc import abstractmethod, ABC
from datetime import datetime

from ois_client_sdk.common.parameter.Header import Header
from ois_client_sdk.common.parameter.Software import Software
from ois_client_sdk.common.parameter.User import User


class Base(ABC):
    header: Header
    user: User
    software: Software

    @property
    @abstractmethod
    def root_element(self) -> str:
        raise NotImplementedError('root_element')

    def serialize(self, request_signature: str) -> ET.Element:
        result = ET.Element(self.root_element)
        self.header.serialize(result)
        self.user.serialize(result, request_signature)
        self.software.serialize(result)
        return result
