from typing import Optional
from datetime import date
from dataclasses import dataclass


@dataclass
class AggregateInvoiceLineData:
    """Field type including aggregate invoice special data

    :param line_exchange_rate: The exchange rate applied to the item, pertaining to 1 (one) unit. This should be filled in only if an aggregate invoice in foreign currency is issued
    :param line_delivery_date: Delivery date of the given item in the case of an aggregate invoice
    """

    line_exchange_rate: Optional[float]
    line_delivery_date: date
