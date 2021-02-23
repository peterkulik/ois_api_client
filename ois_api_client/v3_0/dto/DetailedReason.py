from dataclasses import dataclass


@dataclass
class DetailedReason:
    """Detailed justification of exemption

    :param case: Case notation with code
    :param reason: Case notation with text
    """

    case: str
    reason: str
