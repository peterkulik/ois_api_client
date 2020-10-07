from .Header import Header
from .User import User


class BasicRequest:
    """Basic request data

    :param header: Transactional data of the request
    :param user: Authentication data of the request
    """
    def __init__(self, header: Header, user: User):
        self.header = header
        self.user = user
