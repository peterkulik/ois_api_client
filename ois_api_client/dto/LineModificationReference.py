from .LineOperation import LineOperation


class LineModificationReference:
    """Marking the goal of modification of the line (in the case of data supply about changes

    :param line_number_reference: Line number of the original invoice, which the modification occurs with. In case of create operation the tag shall contain the new line number, as a sequential increment of the the existing lines set
    :param line_operation: Line modification type
    """

    def __init__(self,
                 line_number_reference: int,
                 line_operation: LineOperation
                 ):
        self.line_number_reference = line_number_reference
        self.line_operation = line_operation
