from typing import List
from dataclasses import dataclass


@dataclass
class DeliveryNotes:
    """Delivery notes

    :param delivery_note: Delivery note
    """

    delivery_note: List[str]
