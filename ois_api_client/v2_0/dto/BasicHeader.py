from typing import Optional
from datetime import datetime
from dataclasses import dataclass
from .HeaderVersion import HeaderVersion
from .RequestVersion import RequestVersion


@dataclass
class BasicHeader:
    """Transactional data of the request

    :param request_id: Identifier of the request/response, unique with the taxnumber in every data exchange transaction
    :param timestamp: UTC time of the request/response
    :param request_version: Request version number, indicating which datastructure the client sends data in, and in which the response is expected
    :param header_version: Header version number
    """

    request_id: str
    timestamp: datetime
    request_version: RequestVersion
    header_version: Optional[HeaderVersion]
