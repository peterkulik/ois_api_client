from datetime import date


class DateIntervalParam:
    """Date query params of invoice

    :param date_from: Date interval greater or equals parameter
    :param date_to: Date interval less or equals parameter
    """

    def __init__(self, date_from: date, date_to: date):
        self.date_from = date_from
        self.date_to = date_to
