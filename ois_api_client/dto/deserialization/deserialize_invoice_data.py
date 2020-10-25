import xml.etree.ElementTree as ET
from typing import Union

from .deserialize_batch_invoice import deserialize_batch_invoice
from .deserialize_invoice import deserialize_invoice
from .XmlReader import XmlReader as XR
from ..InvoiceData import InvoiceData
from ..InvoiceMain import InvoiceMain
from ...constants import NAMESPACE_DATA


def deserialize_invoice_data(invoice_data_as_xml: str) -> Union[InvoiceData, None]:
    if invoice_data_as_xml is None:
        return None

    root_el: ET.Element = ET.fromstring(invoice_data_as_xml)
    invoice_main_el = XR.find_child(root_el, 'invoiceMain', namespace=NAMESPACE_DATA)
    invoice_el = XR.find_child(invoice_main_el, 'invoice', namespace=NAMESPACE_DATA)

    if invoice_el is not None:
        data = deserialize_invoice(invoice_el)
    else:
        batch_invoice_el = XR.find_child(invoice_main_el, 'batchInvoice', namespace=NAMESPACE_DATA)
        data = deserialize_batch_invoice(batch_invoice_el)

    result = InvoiceData(
        invoice_number=XR.get_child_text(root_el, 'invoiceNumber', namespace=NAMESPACE_DATA),
        invoice_issue_date=XR.get_child_date(root_el, 'invoiceIssueDate', namespace=NAMESPACE_DATA),
        invoice_main=InvoiceMain(
            data=data
        )
    )

    return result
    # Invoice(
    #             invoice_head=InvoiceHead(
    #                 supplier_info=SupplierInfo(
    #                     supplier_tax_number=TaxNumber(
    #                         taxpayer_id='',
    #                         vat_code=None,
    #                         county_code=None
    #                     ),
    #                     supplier_name='',
    #                     # supplier_address=DetailedAddress(
    #                     #     postal_code='',
    #                     #     city='',
    #                     #     street_name='',
    #                     #     public_place_category='',
    #                     #     country_code='',
    #                     #     region='',
    #                     #     number='',
    #                     #     building='',
    #                     #     staircase='',
    #                     #     floor='',
    #                     #     door='',
    #                     #     lot_number=''
    #                     # ),
    #                     supplier_address=SimpleAddress(
    #                         postal_code='',
    #                         city='',
    #                         additional_address_detail='',
    #                         country_code='',
    #                         region=''
    #                     ),
    #                     group_member_tax_number=TaxNumber(
    #                         taxpayer_id='',
    #                         vat_code=''
    #                     ),
    #                     community_vat_number='',
    #                     supplier_bank_account_number='',
    #                     individual_exemption=False,
    #                     excise_licence_num=''
    #                 ),
    #                 invoice_detail=InvoiceDetail(
    #                     invoice_category=InvoiceCategory.NORMAL,
    #                     invoice_delivery_date=date(2020, 10, 10),
    #                     currency_code='',
    #                     exchange_rate=12,
    #                     invoice_appearance=InvoiceAppearance.PAPER,
    #                     invoice_delivery_period_start=date(2020, 10, 10),
    #                     invoice_delivery_period_end=date(2020, 10, 10),
    #                     invoice_accounting_delivery_date=date(2020, 10, 10),
    #                     periodical_settlement=True,
    #                     small_business_indicator=False,
    #                     self_billing_indicator=True,
    #                     payment_method=PaymentMethod.CASH,
    #                     payment_date=date(2020, 10, 10),
    #                     cash_accounting_indicator=False,
    #                     electronic_invoice_hash='',
    #                     additional_invoice_data=[
    #                         AdditionalData(
    #                             data_name='',
    #                             data_description='',
    #                             data_value=''
    #                         ), AdditionalData(
    #                             data_name='',
    #                             data_description='',
    #                             data_value=''
    #                         )]
    #                 ),
    #                 customer_info=CustomerInfo(
    #                     customer_name='',
    #                     # customer_address=DetailedAddress(
    #                     #     postal_code='',
    #                     #     city='',
    #                     #     street_name='',
    #                     #     public_place_category='',
    #                     #     country_code='',
    #                     #     region='',
    #                     #     number='',
    #                     #     building='',
    #                     #     staircase='',
    #                     #     floor='',
    #                     #     door='',
    #                     #     lot_number=''
    #                     # ),
    #                     customer_address=SimpleAddress(
    #                         postal_code='',
    #                         city='',
    #                         additional_address_detail='',
    #                         country_code='',
    #                         region=''
    #                     ),
    #                     customer_tax_number=TaxNumber(
    #                         taxpayer_id='',
    #                         vat_code='',
    #                         county_code=''
    #                     ),
    #                     group_member_tax_number=TaxNumber(
    #                         taxpayer_id='',
    #                         vat_code='',
    #                         county_code=''
    #                     ),
    #                     community_vat_number='',
    #                     third_state_tax_id='',
    #                     customer_bank_account_number=''
    #                 ), fiscal_representative_info=FiscalRepresentative(
    #                     fiscal_representative_tax_number=TaxNumber(
    #                         taxpayer_id='',
    #                         vat_code='',
    #                         county_code=''
    #                     ),
    #                     fiscal_representative_name='',
    #                     # fiscal_representative_address=DetailedAddress(
    #                     #     postal_code='',
    #                     #     city='',
    #                     #     street_name='',
    #                     #     public_place_category='',
    #                     #     country_code='',
    #                     #     region='',
    #                     #     number='',
    #                     #     building='',
    #                     #     staircase='',
    #                     #     floor='',
    #                     #     door='',
    #                     #     lot_number=''
    #                     # ),
    #                     fiscal_representative_address=SimpleAddress(
    #                         postal_code='',
    #                         city='',
    #                         additional_address_detail='',
    #                         country_code='',
    #                         region=''
    #                     ),
    #                     fiscal_representative_bank_account_number=''
    #                 )
    #             ),
    #             invoice_summary=Summary(
    #                 # summary=SummaryNormal(
    #                 #     summary_by_vat_rate=[
    #                 #         SummaryByVatRate(
    #                 #             vat_rate=VatRate(
    #                 #                 vat_percentage=27,
    #                 #                 vat_exemption='',
    #                 #                 vat_out_of_scope=True,
    #                 #                 vat_domestic_reverse_charge=False,
    #                 #                 margin_scheme_vat=False,
    #                 #                 margin_scheme_no_vat=True
    #                 #             ),
    #                 #             vat_rate_net_data=VatRateNetData(
    #                 #                 vat_rate_net_amount=130,
    #                 #                 vat_rate_net_amount_huf=160
    #                 #             ),
    #                 #             vat_rate_vat_data=VatRateVatData(
    #                 #                 vat_rate_vat_amount=30,
    #                 #                 vat_rate_vat_amount_huf=50
    #                 #             ),
    #                 #             vat_rate_gross_data=VatRateGrossData(
    #                 #                 vat_rate_gross_amount=130,
    #                 #                 vat_rate_gross_amount_huf=100
    #                 #             )
    #                 #         ),
    #                 #         SummaryByVatRate(
    #                 #             vat_rate=VatRate(
    #                 #                 vat_percentage=18,
    #                 #                 vat_exemption='',
    #                 #                 vat_out_of_scope=True,
    #                 #                 vat_domestic_reverse_charge=False,
    #                 #                 margin_scheme_vat=False,
    #                 #                 margin_scheme_no_vat=True
    #                 #             ),
    #                 #             vat_rate_net_data=VatRateNetData(
    #                 #                 vat_rate_net_amount=130,
    #                 #                 vat_rate_net_amount_huf=160
    #                 #             ),
    #                 #             vat_rate_vat_data=VatRateVatData(
    #                 #                 vat_rate_vat_amount=30,
    #                 #                 vat_rate_vat_amount_huf=50
    #                 #             ),
    #                 #             vat_rate_gross_data=VatRateGrossData(
    #                 #                 vat_rate_gross_amount=130,
    #                 #                 vat_rate_gross_amount_huf=100
    #                 #             )
    #                 #         )
    #                 #     ],
    #                 #     invoice_net_amount=300,
    #                 #     invoice_net_amount_huf=300,
    #                 #     invoice_vat_amount=30,
    #                 #     invoice_vat_amount_huf=30
    #                 # ),
    #                 summary=[
    #                     SummarySimplified(
    #                         vat_content=5,
    #                         vat_content_gross_amount=24,
    #                         vat_content_gross_amount_huf=25
    #                     ),
    #                     SummarySimplified(
    #                         vat_content=18,
    #                         vat_content_gross_amount=24,
    #                         vat_content_gross_amount_huf=25
    #                     )
    #                 ],
    #                 summary_gross_data=SummaryGrossData(
    #                     invoice_gross_amount=40,
    #                     invoice_gross_amount_huf=50
    #                 )
    #             ),
    #             invoice_reference=InvoiceReference(
    #                 original_invoice_number='',
    #                 modification_index=1,
    #                 modify_without_master=True
    #             ),
    #             invoice_lines=Lines(
    #                 items=[
    #                     Line(
    #                         line_number=1,
    #                         line_modification_reference=LineModificationReference(
    #                             line_number_reference=1,
    #                             line_operation=LineOperation.CREATE
    #                         ),
    #                         references_to_other_lines=ReferencesToOtherLines(
    #                             items=[1, 2, 3]
    #                         ),
    #                         advance_indicator=True,
    #                         product_codes=ProductCodes(
    #                             items=[
    #                                 ProductCode(
    #                                     product_code_category=ProductCodeCategory.KT,
    #                                     product_code_value='',
    #                                     product_code_own_value=''
    #                                 ),
    #                                 ProductCode(
    #                                     product_code_category=ProductCodeCategory.EJ,
    #                                     product_code_value='',
    #                                     product_code_own_value=''
    #                                 ),
    #                             ]
    #                         ),
    #                         # todo: MORE
    #                     )
    #                     # todo: MORE LINES
    #                 ]),
    #             product_fee_summary=[
    #                 ProductFeeSummary(
    #                     product_fee_operation=ProductFeeOperation.REFUND,
    #                     product_fee_data=[
    #                         ProductFeeData(
    #                             product_fee_code=ProductCode(
    #                                 product_code_category=ProductCodeCategory.EJ,
    #                                 product_code_value='',
    #                                 product_code_own_value=''
    #                             ),
    #                             product_fee_quantity=13,
    #                             product_fee_measuring_unit=ProductFeeMeasuringUnit.KG,
    #                             product_fee_rate=123.12,
    #                             product_fee_amount=2323.23
    #                         ),
    #                         ProductFeeData(
    #                             product_fee_code=ProductCode(
    #                                 product_code_category=ProductCodeCategory.EJ,
    #                                 product_code_value='',
    #                                 product_code_own_value=''
    #                             ),
    #                             product_fee_quantity=13,
    #                             product_fee_measuring_unit=ProductFeeMeasuringUnit.KG,
    #                             product_fee_rate=123.12,
    #                             product_fee_amount=2323.23
    #                         )],
    #                     product_charge_sum=123,
    #                     payment_evidence_document_data=PaymentEvidenceDocumentData(
    #                         evidence_document_no='',
    #                         evidence_document_date=date(2020, 10, 10),
    #                         obligated_name='',
    #                         # obligated_address=DetailedAddress(
    #                         #     postal_code='',
    #                         #     city='',
    #                         #     street_name='',
    #                         #     public_place_category='',
    #                         #     country_code='',
    #                         #     region='',
    #                         #     number='',
    #                         #     building='',
    #                         #     staircase='',
    #                         #     floor='',
    #                         #     door='',
    #                         #     lot_number=''
    #                         # ),
    #                         obligated_address=SimpleAddress(
    #                             postal_code='',
    #                             city='',
    #                             additional_address_detail='',
    #                             country_code='',
    #                             region=''
    #                         ),
    #                         obligated_tax_number=TaxNumber(
    #                             taxpayer_id='',
    #                             vat_code='',
    #                             county_code=''
    #                         )
    #                     )
    #                 )
    #             ]
    #         )
    #     )
    # )
