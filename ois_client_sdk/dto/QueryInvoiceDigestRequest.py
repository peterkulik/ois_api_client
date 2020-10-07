from datetime import date
from enum import Enum
from typing import Union

from .BasicRequest import BasicRequest
from .Header import Header
from .Software import Software
from .User import User


class InvoiceDirection(Enum):
    """Inbound or outbound invoice query parameter"""
    INBOUND = 'INBOUND'
    OUTBOUND = 'OUTBOUND'


class DateIntervalParam:
    """Date query params of invoice

    :param date_from: Date interval greater or equals parameter
    :param date_to: Date interval less or equals parameter
    """

    def __init__(self, date_from: date, date_to: date):
        self.date_from = date_from
        self.date_to = date_to


class DateTimeIntervalParam:
    """Datestamp query params of invoice

    :param date_time_from: Datetime interval greater or equals parameter
    :param date_time_to: Datetime interval less or equals parameter
    """

    def __init__(self, date_time_from: date, date_time_to: date):
        self.date_time_from = date_time_from
        self.date_to = date_time_to


class MandatoryQueryParam:
    """Mandatory params of the invoice query

    :param parameter: One of the
    """

    class InvoiceIssueDate:
        """InvoiceIssueDate parameter

        :param invoice_issue_date: Date range of the invoice issue date
        """

        def __init__(self, invoice_issue_date: DateIntervalParam):
            self.invoice_issue_date = invoice_issue_date

    class InsDate:
        """InsDate parameter

        :param ins_date: Datetime range of processing data exchange in UTC time
        """

        def __init__(self, ins_date: DateTimeIntervalParam):
            self.ins_date = ins_date

    class OriginalInvoiceNumber:
        """OriginalInvoiceNumber parameter

        :param original_invoice_number: Sequence number of the original invoice, on which the modification occurs
        """

        def __init__(self, original_invoice_number: str):
            self.original_invoice_number = original_invoice_number

    def __init__(self, parameter: Union[InvoiceIssueDate, InsDate, OriginalInvoiceNumber]):
        self.parameter = parameter


class Source(Enum):
    """Data exchange source"""
    WEB = 'WEB'  # Web exchange
    XML = 'XML'  # Manual XML upload
    MGM = 'MGM'  # Machine-to-machine exchange
    OPG = 'OPG'  # Online cash register exchange
    OSZ = 'OSZ'  # NTCA online invoicing


class InvoiceAppearanceType(Enum):
    """Form of appearance of the invoice type"""
    PAPER = 'PAPER'  # Invoice issued on paper
    ELECTRONIC = 'ELECTRONIC'  # Electronic invoice (non-EDI)
    EDI = 'EDI'  # EDI invoice
    UNKNOWN = 'UNKNOWN'  # The software cannot be identify the form of appearance of the invoice or it is unknown
    # at the time of issue


class PaymentMethod(Enum):
    """Method of payment"""
    TRANSFER = 'TRANSFER'  # Bank transfer
    CASH = 'CASH'  # Cash
    CARD = 'CARD'  # Debit card, credit card, other cash-substitute payment instrument
    VOUCHER = 'VOUCHER'  # Voucher,  bill of exchange, other non-cash payment instrument
    OTHER = 'OTHER'  # Other


class InvoiceCategory(Enum):
    """Type of invoice"""
    NORMAL = 'NORMAL'  # Normal (not simplified and not aggregate) invoice
    SIMPLIFIED = 'SIMPLIFIED'  # Simplified invoice
    AGGREGATE = 'AGGREGATE'  # Aggregate invoice


class AdditionalQueryParams:
    """Additional params of the invoice query

    :param tax_number: Tax number of the supplier or the customer of the invoice (the search criteria depends on the value of the invoiceDirection tag)
    :param group_member_tax_number:  Tax number of group member of the supplier or the customer of the invoice (the search criteria depends on the value of the invoiceDirection tag)
    :param name: Query param of the supplier or the customer of the invoice for leading match pattern (the search criteria depends on the value of the invoiceDirection tag)
    :param invoice_category: Type of invoice
    :param payment_method: Method of payment
    :param invoice_appearance: Form of appearance of the invoice
    :param source: Data exchange source
    :param currency: Currency of the invoice
    """

    def __init__(self, tax_number: str, group_member_tax_number: str, name: str, invoice_category: InvoiceCategory,
                 payment_method: PaymentMethod, invoice_appearance: InvoiceAppearanceType, source: Source,
                 currency: str):
        self.tax_number = tax_number
        self.group_member_tax_number = group_member_tax_number
        self.name = name
        self.invoice_category = invoice_category
        self.payment_method = payment_method
        self.invoice_appearance = invoice_appearance
        self.source = source
        self.currency = currency


class QueryOperator(Enum):
    """Relational operator type"""
    EQ = 'EQ'  # Equals
    GT = 'GT'  # Greater than relation
    GTE = 'GTE'  # Greater or equals relation
    LT = 'LT'  # Less than relation
    LTE = 'LTE'  # Less or equals relation


class RelationQueryDateType:
    """Query parameter for date values

    :param query_operator: Query operator
    :param query_value: Query value
    """

    def __init__(self, query_operator: QueryOperator, query_value: date):
        self.query_operator = query_operator
        self.query_value = query_value


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


class ManageInvoiceOperation(Enum):
    """Invoice operation type"""
    CREATE = 'CREATE'  # Original invoice exchange
    MODIFY = 'MODIFY'  # Modification invoice exchange
    STORNO = 'STORNO'  # Exchange concerning invoice invalidation


class TransactionQueryParams:
    """Transactional params of the invoice query

    :param transaction_id: Transaction identifier of the data exchange
    :param index: Sequence number of the invoice within the request
    :param invoice_operation: Invoice operation type
    """

    def __init__(self, transaction_id: str, index: int, invoice_operation: ManageInvoiceOperation):
        self.transaction_id = transaction_id
        self.index = index
        self.invoice_operation = invoice_operation


class InvoiceQueryParams:
    """Invoice query parameters

    :param mandatory_query_params: Mandatory params of the invoice query
    :param additional_query_params: Additional params of the invoice query
    :param relational_query_params: Relational params of the invoice query
    :param transaction_query_params: Transactional params of the invoice query
    """

    def __init__(self, mandatory_query_params: MandatoryQueryParams, additional_query_params: AdditionalQueryParams,
                 relational_query_params: RelationalQueryParams, transaction_query_params: TransactionQueryParams):
        self.mandatory_query_params = mandatory_query_params
        self.additional_query_params = additional_query_params
        self.relational_query_params = relational_query_params
        self.transaction_query_params = transaction_query_params


class QueryInvoiceDigestRequest(BasicRequest):
    """Request type of the POST /queryInvoiceDigest REST operation

    :param page: The queried page count
    :param invoice_direction: Inbound or outbound invoice query parameter
    :param invoice_query_params: Invoice query parameters
    """

    def __init__(self, header: Header, user: User, software: Software, page: int, invoice_direction: InvoiceDirection,
                 invoice_query_params: InvoiceQueryParams):
        super().__init__(header, user, software)
        self.page = page
        self.invoice_direction = invoice_direction
        self.invoice_query_params = invoice_query_params
