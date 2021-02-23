from dataclasses import dataclass
from .Software import Software
from .BasicRequest import BasicRequest


@dataclass
class BasicOnlineInvoiceRequest(BasicRequest):
    """Online Invoice specific basic request data

    :param software: Billing software data
    """

    software: Software
