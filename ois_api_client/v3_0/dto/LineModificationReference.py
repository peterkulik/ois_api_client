from dataclasses import dataclass
from .LineOperation import LineOperation


@dataclass
class LineModificationReference:
    """Marking the goal of modification of the line (in the case of data supply about changes/updates only)

    :param line_number_reference: Line number of the original invoice, which the modification occurs with. In case of create operation the tag shall contain the new line number, as a sequential increment of the the existing lines set
    :param line_operation: Line modification type
    """

    line_number_reference: int
    line_operation: LineOperation
