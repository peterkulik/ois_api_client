from dataclasses import dataclass
from .BasicResponse import BasicResponse


@dataclass
class GeneralErrorHeaderResponse(BasicResponse):
    """Generic fault type for every REST operation"""

