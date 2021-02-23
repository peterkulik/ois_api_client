from dataclasses import dataclass
from .BasicHeader import BasicHeader
from .Software import Software
from .UserHeader import UserHeader


@dataclass
class BasicRequest:
    """Basic request data

    :param header: Transactional data of the request
    :param user: Authentication data of the request
    :param software: Billing software data
    """

    header: BasicHeader
    user: UserHeader
    software: Software
