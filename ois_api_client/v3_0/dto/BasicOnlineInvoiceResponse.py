from dataclasses import dataclass
from .Software import Software
from .BasicResponse import BasicResponse


@dataclass
class BasicOnlineInvoiceResponse(BasicResponse):
    """Online Invoice specific basic response data

    :param software: Billing software data
    """

    software: Software
