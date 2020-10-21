from datetime import date
from typing import List, Union

from .RelationQueryDate import RelationQueryDate
from .RelationQueryMonetary import RelationQueryMonetary
from .custom.RangeDate import RangeDate
from .custom.RangeMonetary import RangeMonetary


class RelationalQueryParams:
    """Relational params of the invoice query

    :param invoice_delivery: Query parameter of the invoice delivery date
    :param payment_date: Query parameter of the invoice payment date
    :param invoice_net_amount: Query parameter of the invoice net amount expressed in the currency of the invoice
    :param invoice_net_amount_huf: Query parameter of the invoice net amount expressed in HUF
    :param invoice_vat_amount: Query parameter of the invoice VAT amount expressed in the currency of the invoice
    :param invoice_vat_amount_huf: Query parameter of the invoice VAT amount expressed in HUF
    """

    def __init__(self, invoice_delivery: Union[date, RangeDate, RelationQueryDate, None] = None,
                 payment_date: Union[date, RangeDate, RelationQueryDate, None] = None,
                 invoice_net_amount: Union[float, RangeMonetary, RelationQueryMonetary, None] = None,
                 invoice_net_amount_huf: Union[float, RangeMonetary, RelationQueryMonetary, None] = None,
                 invoice_vat_amount: Union[float, RangeMonetary, RelationQueryMonetary, None] = None,
                 invoice_vat_amount_huf: Union[float, RangeMonetary, RelationQueryMonetary, None] = None):
        self.invoice_delivery = invoice_delivery
        self.payment_date = payment_date
        self.invoice_net_amount = invoice_net_amount
        self.invoice_net_amount_huf = invoice_net_amount_huf
        self.invoice_vat_amount = invoice_vat_amount
        self.invoice_vat_amount_huf = invoice_vat_amount_huf
