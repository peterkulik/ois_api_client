from dataclasses import dataclass
from .BasicHeader import BasicHeader
from .BasicResult import BasicResult


@dataclass
class BasicResponse:
    """Basic response data

    :param header: Transactional data of the response
    :param result: Basic result data
    """

    header: BasicHeader
    result: BasicResult
