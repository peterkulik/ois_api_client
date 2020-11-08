from datetime import datetime

from ..constants import REQUEST_VERSION, HEADER_VERSION


class BasicHeader:
    """Transactional data of the request

    :param request_id: Identifier of the request/response, unique with the taxnumber in every data exchange transaction
    :param timestamp: UTC time of the request/response
    :param request_version: Request version number, indicating which datastructure the client sends data in, and in which the response is expected
    :param header_version: Header version number
    """

    def __init__(self, request_id: str, timestamp: datetime, request_version: str = REQUEST_VERSION,
                 header_version: str = HEADER_VERSION):
        self.request_id = request_id
        self.timestamp = timestamp
        self.request_version = request_version
        self.header_version = header_version
