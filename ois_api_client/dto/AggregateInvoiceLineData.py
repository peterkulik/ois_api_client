from datetime import date
from typing import Union


class AggregateInvoiceLineData:
    """Field type including aggregate invoice special data

    :param line_delivery_date: Delivery date of the given item in the case of an aggregate invoice
    :param line_exchange_rate: The exchange rate applied to the item, pertaining to 1 (one) unit. This should be filled in only if an aggregate invoice in foreign currency is issued
    """

    def __init__(self,
                 line_delivery_date: date,
                 line_exchange_rate: Union[float, None] = None):
        self.line_exchange_rate = line_exchange_rate
        self.line_delivery_date = line_delivery_date
