from enum import Enum


class OriginalRequestVersion(Enum):
    """Request version value of the queried invoice"""
    O_1_0 = '1.0'
    O_1_1 = '1.1'
    O_2_0 = '2.0'
    O_3_0 = '3.0'
