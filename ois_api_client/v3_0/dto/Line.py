from typing import Optional
from typing import List
from dataclasses import dataclass
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
from .NewTransportMean import NewTransportMean
from .ProductCodes import ProductCodes
from .ProductFeeClause import ProductFeeClause
from .ProductFeeData import ProductFeeData
from .ReferencesToOtherLines import ReferencesToOtherLines
from .UnitOfMeasure import UnitOfMeasure


@dataclass
class Line:
    """Field type including data of invoice items (product or service)

    :param line_number: Sequential number of the item
    :param line_modification_reference: Marking the goal of modification of the line (in the case of data supply about changes/updates only)
    :param references_to_other_lines: References to connected items if it is necessary according to VAT law
    :param advance_data: Advance related data
    :param product_codes: Product codes
    :param line_expression_indicator: The value is true if the unit of measure of the invoice item is expressible in natural unit
    :param line_nature_indicator: Indication of the nature of the supply of goods or services on a given line
    :param line_description: Name / description of the product or service
    :param quantity: Quantity
    :param unit_of_measure: Canonical representation of the unit of measure of the invoice, according to the interface specification
    :param unit_of_measure_own: Literal unit of measure of the invoice
    :param unit_price: Unit price expressed in the currency of the invoice In the event of simplified invoices gross unit price, in other cases net unit price
    :param unit_price_huf: Unit price expressed in HUF
    :param line_discount_data: Discount data in relation to the item
    :param line_amounts_normal: Item value data to be completed in case of normal (not simplified, but including aggregated) invoice
    :param line_amounts_simplified: Item value data to be completed in case of simplified invoice
    :param intermediated_service: The value is true if the item is an intermediated service - paragraph (4) 1 of the Article 3 of Accounting Act
    :param aggregate_invoice_line_data: Aggregate invoice data
    :param new_transport_mean: Supply of new means of transport - section 89 § and 169 (o) of the VAT law
    :param deposit_indicator: The value is true if the item is bottle/container deposit
    :param obligated_for_product_fee: The value is true if the item is liable to product fee
    :param gpc_excise: Excise duty on natural gas, electricity and coal in Hungarian forints – paragraph (2), Section 118 of the Act on Excise Duties
    :param diesel_oil_purchase: Data of gas oil acquisition after taxation – point a), paragraph (1) of Section 75 of the NGM Decree No. 45/2016. (XI. 29.)
    :param neta_declaration: Value is true, if the taxable person is liable for tax obligation determined in the Act on Public Health Product Tax (Neta tv.). Paragraph (2), Section 3 of the Act CIII of 2011
    :param product_fee_clause: Clauses according to the Act LXXXV of 2011 on Environmental Protection Product Fee (related to the item)
    :param line_product_fee_content: Data on the content of the line's product charge
    :param conventional_line_info: Other conventionally named data to assist in invoice processing
    :param additional_line_data: Other data in relation to the product / service item
    """

    line_number: int
    line_modification_reference: Optional[LineModificationReference]
    references_to_other_lines: Optional[ReferencesToOtherLines]
    advance_data: Optional[AdvanceData]
    product_codes: Optional[ProductCodes]
    line_expression_indicator: bool
    line_nature_indicator: Optional[LineNatureIndicator]
    line_description: Optional[str]
    quantity: Optional[float]
    unit_of_measure: Optional[UnitOfMeasure]
    unit_of_measure_own: Optional[str]
    unit_price: Optional[float]
    unit_price_huf: Optional[float]
    line_discount_data: Optional[DiscountData]
    line_amounts_normal: Optional[LineAmountsNormal]
    line_amounts_simplified: Optional[LineAmountsSimplified]
    intermediated_service: Optional[bool]
    aggregate_invoice_line_data: Optional[AggregateInvoiceLineData]
    new_transport_mean: Optional[NewTransportMean]
    deposit_indicator: Optional[bool]
    obligated_for_product_fee: Optional[bool]
    gpc_excise: Optional[float]
    diesel_oil_purchase: Optional[DieselOilPurchase]
    neta_declaration: Optional[bool]
    product_fee_clause: Optional[ProductFeeClause]
    line_product_fee_content: Optional[List[ProductFeeData]]
    conventional_line_info: Optional[ConventionalInvoiceInfo]
    additional_line_data: Optional[List[AdditionalData]]
