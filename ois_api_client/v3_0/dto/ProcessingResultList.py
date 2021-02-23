from typing import Optional
from typing import List
from dataclasses import dataclass
from .AnnulmentData import AnnulmentData
from .OriginalRequestVersion import OriginalRequestVersion
from .ProcessingResult import ProcessingResult


@dataclass
class ProcessingResultList:
    """Processing results of the request

    :param processing_result: Invoice processing result
    :param original_request_version: requestVersion value of the invoice exchange
    :param annulment_data: Status data of technical annulment
    """

    processing_result: List[ProcessingResult]
    original_request_version: OriginalRequestVersion
    annulment_data: Optional[AnnulmentData]
