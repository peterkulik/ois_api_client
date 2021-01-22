from typing import Union, List, Optional

from .AdditionalData import AdditionalData
from .AdvanceData import AdvanceData
from .AggregateInvoiceLineData import AggregateInvoiceLineData
from .ConventionalInvoiceInfo import ConventionalInvoiceInfo
from .DieselOilPurchase import DieselOilPurchase
from .DiscountData import DiscountData
from .LineAmountsNormal import LineAmountsNormal
from .LineAmountsSimplified import LineAmountsSimplified
from .LineModificationReference import LineModificationReference
from .LineNatureIndicator import LineNatureIndicator
from .MarginScheme import MarginScheme
from .NewTransportMean import NewTransportMean
from .ProductCodes import ProductCodes
from .ProductFeeClause import ProductFeeClause
from .ProductFeeData import ProductFeeData
from .ReferencesToOtherLines import ReferencesToOtherLines
from .UnitOfMeasure import UnitOfMeasure


class Line:
    """Field type including data of invoice items (product or service)

    :param line_number: Sequential number of the item
    :param line_expression_indicator: The value is true if the unit of measure of the invoice item is expressible in natural unit
    :param line_modification_reference: Marking the goal of modification of the line (in the case of data supply about changes
    :param references_to_other_lines: References to connected items if it is necessary according to VAT law
    :param product_codes: Product codes
    :param line_nature_indicator: Indication of the nature of the supply of goods or services on a given line
    :param line_description: Name / description of the product or service
    :param quantity: Quantity
    :param unit_of_measure: Canonical representation of the unit of measure of the invoice, according to the interface specification
    :param unit_of_measure_own: Literal unit of measure of the invoice
    :param unit_price: Unit price expressed in the currency of the invoice In the event of simplified invoices gross unit price, in other cases net unit price
    :param unit_price_huf: Unit price expressed in HUF
    :param line_discount_data: Discount data in relation to the item
    :param line_amounts: Union[LineAmountsNormal, LineAmountsSimplified]: Item value data to be completed
    :param intermediated_service: The value is true if the item is an intermediated service - paragraph (4) 1 of the Article 3 of Accounting Act
    :param aggregate_invoice_line_data: Aggregate invoice data
    :param new_transport_mean: Supply of new means of transport - section 89 § and 169 (o) of the VAT law
    :param deposit_indicator: The value is true if the item is bottle
    :param margin_scheme_indicator: Marking the margin-scheme taxation as per section 169 (p)(q)
    :param obligated_for_product_fee: The value is true if the item is liable to product fee
    :param gpc_excise: Excise duty on natural gas, electricity and coal in Hungarian forints – paragraph (2), Section 118 of the Act on Excise Duties
    :param diesel_oil_purchase: Data of gas oil acquisition after taxation – point a), paragraph (1) of Section 75 of the NGM Decree No. 45
    :param neta_declaration: Value is true, if the taxable person is liable for tax obligation determined in the Act on Public Health Product Tax (Neta tv.). Paragraph (2), Section 3 of the Act CIII of 2011
    :param product_fee_clause: Clauses according to the Act LXXXV of 2011 on Environmental Protection Product Fee (related to the item)
    :param line_product_fee_content: Data on the content of the line's product charge
    :param conventional_line_info: Other conventionally named data to assist in invoice processing
    :param additional_line_data: Other data in relation to the product / service item
    """
    def __init__(self,
                 line_number: int,
                 line_expression_indicator: bool,
                 line_modification_reference: Optional[LineModificationReference] = None,
                 references_to_other_lines: Optional[ReferencesToOtherLines] = None,
                 advance_data: Optional[AdvanceData] = None,
                 product_codes: Optional[ProductCodes] = None,
                 line_nature_indicator: Optional[LineNatureIndicator] = None,
                 line_description: Optional[str] = None,
                 quantity: Optional[float] = None,
                 unit_of_measure: Optional[UnitOfMeasure] = None,
                 unit_of_measure_own: Optional[str] = None,
                 unit_price: Optional[float] = None,
                 unit_price_huf: Optional[float] = None,
                 line_discount_data: Optional[DiscountData] = None,
                 line_amounts: Union[Optional[LineAmountsNormal], Optional[LineAmountsSimplified]] = None,
                 intermediated_service: Optional[bool] = None,
                 aggregate_invoice_line_data: Optional[AggregateInvoiceLineData] = None,
                 new_transport_mean: Optional[NewTransportMean] = None,
                 deposit_indicator: Optional[bool] = None,
                 margin_scheme_indicator: Optional[MarginScheme] = None,
                 obligated_for_product_fee: Optional[bool] = None,
                 gpc_excise: Optional[float] = None,
                 diesel_oil_purchase: Optional[DieselOilPurchase] = None,
                 neta_declaration: Optional[bool] = None,
                 product_fee_clause: Optional[ProductFeeClause] = None,
                 line_product_fee_content: Optional[List[ProductFeeData]] = None,
                 conventional_line_info: Optional[ConventionalInvoiceInfo] = None,
                 additional_line_data: Optional[List[AdditionalData]] = None):
        self.line_number = line_number
        self.line_modification_reference = line_modification_reference
        self.references_to_other_lines = references_to_other_lines
        self.advance_data = advance_data
        self.product_codes = product_codes
        self.line_expression_indicator = line_expression_indicator
        self.line_nature_indicator = line_nature_indicator
        self.line_description = line_description
        self.quantity = quantity
        self.unit_of_measure = unit_of_measure
        self.unit_of_measure_own = unit_of_measure_own
        self.unit_price = unit_price
        self.unit_price_huf = unit_price_huf
        self.line_discount_data = line_discount_data

        if line_amounts is not None:
            if isinstance(line_amounts, LineAmountsNormal):
                self.line_amounts_normal = line_amounts
            elif isinstance(line_amounts, LineAmountsSimplified):
                self.line_amounts_simplified = line_amounts

        self.intermediated_service = intermediated_service
        self.aggregate_invoice_line_data = aggregate_invoice_line_data
        self.new_transport_mean = new_transport_mean
        self.deposit_indicator = deposit_indicator
        self.margin_scheme_indicator = margin_scheme_indicator
        self.obligated_for_product_fee = obligated_for_product_fee
        self.gpc_excise = gpc_excise
        self.diesel_oil_purchase = diesel_oil_purchase
        self.neta_declaration = neta_declaration
        self.product_fee_clause = product_fee_clause
        self.line_product_fee_content = line_product_fee_content
        self.conventional_line_info = conventional_line_info
        self.additional_line_data = additional_line_data
