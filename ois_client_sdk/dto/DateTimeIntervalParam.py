from datetime import datetime


class DateTimeIntervalParam:
    """Datestamp query params of invoice

    :param date_time_from: Datetime interval greater or equals parameter
    :param date_time_to: Datetime interval less or equals parameter
    """

    def __init__(self, date_time_from: datetime, date_time_to: datetime):
        self.date_time_from = date_time_from
        self.datetime_to = date_time_to
