from .LineOperation import LineOperation


class LineModificationReference:
    """Marking the goal of modification of the line (in the case of data supply about changes

    :param line_number_reference:
    :param line_operation:
    """

    def __init__(self, line_number_reference: int, line_operation: LineOperation):
        self.line_number_reference = line_number_reference
        self.line_operation = line_operation
