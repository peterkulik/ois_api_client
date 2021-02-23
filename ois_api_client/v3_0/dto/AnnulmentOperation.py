from dataclasses import dataclass
from .ManageAnnulmentOperation import ManageAnnulmentOperation


@dataclass
class AnnulmentOperation:
    """Technical annulment operation of the request

    :param index: Sequence number of the technical annulment within the request
    :param annulment_operation: Type of the desired technical annulment operation
    :param invoice_annulment: Technical annulment data in BASE64 encoded form
    """

    index: int
    annulment_operation: ManageAnnulmentOperation
    invoice_annulment: str
