from dataclasses import dataclass
from .BasicHeader import BasicHeader
from .BasicResult import BasicResult
from .Software import Software


@dataclass
class BasicResponse:
    """Basic response data

    :param header: Transactional data of the response
    :param result: Basic result data
    :param software: Billing software data
    """

    header: BasicHeader
    result: BasicResult
    software: Software
