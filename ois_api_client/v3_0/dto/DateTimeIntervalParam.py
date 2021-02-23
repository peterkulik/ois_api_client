from datetime import datetime
from dataclasses import dataclass


@dataclass
class DateTimeIntervalParam:
    """Datestamp query params of invoice

    :param date_time_from: Datetime interval greater or equals parameter
    :param date_time_to: Datetime interval less or equals parameter
    """

    date_time_from: datetime
    date_time_to: datetime
