from datetime import date
from dataclasses import dataclass


@dataclass
class DateIntervalParam:
    """Date query params of invoice

    :param date_from: Date interval greater or equals parameter
    :param date_to: Date interval less or equals parameter
    """

    date_from: date
    date_to: date
