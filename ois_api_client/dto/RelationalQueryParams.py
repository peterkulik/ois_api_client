from .RelationQueryDateType import RelationQueryDateType


class RelationalQueryParams:
    """Relational params of the invoice query

    :param invoice_delivery: Query parameter of the invoice delivery date
    :param payment_date: Query parameter of the invoice payment date
    :param invoice_net_amount: Query parameter of the invoice net amount expressed in the currency of the invoice
    :param invoice_net_amount_huf: Query parameter of the invoice net amount expressed in HUF
    :param invoice_vat_amount: Query parameter of the invoice VAT amount expressed in the currency of the invoice
    :param invoice_vat_amount_huf: Query parameter of the invoice VAT amount expressed in HUF
    """

    def __init__(self, invoice_delivery: RelationQueryDateType, payment_date: RelationQueryDateType, invoice_net_amount,
                 invoice_net_amount_huf, invoice_vat_amount,
                 invoice_vat_amount_huf):
        self.invoice_delivery = invoice_delivery
        self.payment_date = payment_date
        self.invoice_net_amount = invoice_net_amount
        self.invoice_net_amount_HUF = invoice_net_amount_huf
        self.invoice_vat_amount = invoice_vat_amount
        self.invoice_vat_amount_HUF = invoice_vat_amount_huf
