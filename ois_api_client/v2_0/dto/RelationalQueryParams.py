from typing import Optional
from typing import List
from dataclasses import dataclass
from .RelationQueryDate import RelationQueryDate
from .RelationQueryMonetary import RelationQueryMonetary


@dataclass
class RelationalQueryParams:
    """Relational params of the invoice query

    :param invoice_delivery: Query parameter of the invoice delivery date
    :param payment_date: Query parameter of the invoice payment date
    :param invoice_net_amount: Query parameter of the invoice net amount expressed in the currency of the invoice
    :param invoice_net_amount_huf: Query parameter of the invoice net amount expressed in HUF
    :param invoice_vat_amount: Query parameter of the invoice VAT amount expressed in the currency of the invoice
    :param invoice_vat_amount_huf: Query parameter of the invoice VAT amount expressed in HUF
    """

    invoice_delivery: Optional[List[RelationQueryDate]]
    payment_date: Optional[List[RelationQueryDate]]
    invoice_net_amount: Optional[List[RelationQueryMonetary]]
    invoice_net_amount_huf: Optional[List[RelationQueryMonetary]]
    invoice_vat_amount: Optional[List[RelationQueryMonetary]]
    invoice_vat_amount_huf: Optional[List[RelationQueryMonetary]]
