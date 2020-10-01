import xml.etree.ElementTree as ET
from abc import abstractmethod, ABC
from dataclasses import dataclass

from ois_client_sdk.common.parameter.Header import Header
from ois_client_sdk.common.parameter.Software import Software
from ois_client_sdk.common.parameter.User import User


@dataclass
class Base(ABC):
    header: Header
    user: User
    software: Software

    @property
    @abstractmethod
    def root_element(self) -> str:
        raise NotImplementedError('root_element')

    def serialize(self, request_signature: str, password_hash: str) -> str:
        root = ET.Element(self.root_element)
        self.header.serialize(root)
        self.user.serialize(root, password_hash, request_signature)
        self.software.serialize(root)
        ET.ElementTree(root).write('expected_serialized_parameter.xml', encoding='utf8')
        result = ET.tostring(root, encoding='utf8', method='xml')
        return result
