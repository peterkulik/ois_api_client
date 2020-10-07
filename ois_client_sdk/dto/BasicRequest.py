from dataclasses import dataclass

from .Header import Header
from .User import User
from .Software import Software


# @dataclass
# class BasicRequest:
#     header: Header
#     user: User
#     software: Software

class BasicRequest:
    def __init__(self, header: Header, user: User, software: Software):
        self.header = header
        self.user = user
        self.software = software
