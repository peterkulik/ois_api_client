from dataclasses import dataclass
from .BasicHeader import BasicHeader
from .UserHeader import UserHeader


@dataclass
class BasicRequest:
    """Basic request data

    :param header: Transactional data of the request
    :param user: Authentication data of the request
    """

    header: BasicHeader
    user: UserHeader
