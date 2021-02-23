from dataclasses import dataclass


@dataclass
class NewCreatedLines:
    """New invoice lines created by the modification document

    :param line_number_interval_start: Invoice line interval start
    :param line_number_interval_end: Invoice line interval end (inclusive)
    """

    line_number_interval_start: int
    line_number_interval_end: int
