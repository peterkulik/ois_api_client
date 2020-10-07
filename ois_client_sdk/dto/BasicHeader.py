from datetime import datetime


class BasicHeader:
    """Transactional data of the request

    :param request_id: Identifier of the request/response, unique with the taxnumber in every data exchange transaction
    :param timestamp: UTC time of the request/response
    """

    def __init__(self, request_id: str, timestamp: datetime):
        self.request_id = request_id
        self.timestamp = timestamp
