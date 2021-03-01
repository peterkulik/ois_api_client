import xml.etree.ElementTree as ET
from ois_api_client.v3_0 import deserialization, dto
from datetime import datetime
from tests.get_root_dir import get_root_dir


def test_deserialize_v30(pytestconfig):
    dir_ = get_root_dir(pytestconfig)

    with open(f'{dir_}/tests/dto/deserialization/v30/Belfoldi ertekesites tobb AFA tipus.xml', 'r') as file:
        xml = file.read().replace('\n', '')

    root: ET.Element = ET.fromstring(xml)
    result = deserialization.deserialize_invoice_data(root)

    assert result is not None
    assert result.invoice_number == '2021/000123A'
    assert result.invoice_issue_date == datetime(2021, 5, 15)
    assert result.invoice_main is not None
    assert result.invoice_main.invoice is not None

    inv = result.invoice_main.invoice
    assert inv.invoice_head is not None
    head = inv.invoice_head
    assert head.supplier_info is not None
    supplier = head.supplier_info
    assert supplier.supplier_name == 'Értékesítő Kft'
    assert supplier.supplier_tax_number is not None
    assert supplier.supplier_tax_number.taxpayer_id == '99999999'
    assert supplier.supplier_tax_number.vat_code == '2'
    assert supplier.supplier_tax_number.county_code == '41'
    assert supplier.supplier_address is not None
    assert supplier.supplier_address.detailed_address is not None
    assert supplier.supplier_address.detailed_address.country_code == 'HU'
    assert supplier.supplier_address.detailed_address.postal_code == '1234'
    assert supplier.supplier_address.detailed_address.city == 'Budapest'
    assert supplier.supplier_address.detailed_address.street_name == 'Hármas'
    assert supplier.supplier_address.detailed_address.public_place_category == 'utca'
    assert supplier.supplier_address.detailed_address.number == '1'

    assert head.customer_info is not None
    customer = head.customer_info
    assert customer.customer_vat_status == dto.CustomerVatStatus.DOMESTIC
    assert customer.customer_vat_data is not None
    assert customer.customer_vat_data.customer_tax_number is not None
    assert customer.customer_vat_data.customer_tax_number.taxpayer_id == '99887764'
    assert customer.customer_vat_data.customer_tax_number.vat_code == '2'
    assert customer.customer_vat_data.customer_tax_number.county_code == '02'
    assert customer.customer_vat_data.customer_tax_number.group_member_tax_number is not None
    assert customer.customer_vat_data.customer_tax_number.group_member_tax_number.vat_code is None
    assert customer.customer_vat_data.customer_tax_number.group_member_tax_number.taxpayer_id == '44455566'
    assert customer.customer_vat_data.customer_tax_number.group_member_tax_number.county_code is None

    assert customer.customer_name == 'Beszerző Kft'
    assert customer.customer_address is not None
    assert customer.customer_address.detailed_address is not None
    assert customer.customer_address.detailed_address.country_code == 'HU'
    assert customer.customer_address.detailed_address.postal_code == '7600'
    assert customer.customer_address.detailed_address.city == 'Pécs'
    assert customer.customer_address.detailed_address.street_name == 'Északi'
    assert customer.customer_address.detailed_address.public_place_category == 'sugárút'
    assert customer.customer_address.detailed_address.number == '123'

    assert head.invoice_detail is not None
    inv_detail = head.invoice_detail

    assert inv_detail.invoice_category == dto.InvoiceCategory.NORMAL
    assert inv_detail.invoice_delivery_date == datetime(2021, 5, 10)
    assert inv_detail.currency_code == 'HUF'
    assert inv_detail.exchange_rate == 1.0
    assert inv_detail.payment_method == dto.PaymentMethod.TRANSFER
    assert inv_detail.payment_date == datetime(2021, 5, 30)
    assert inv_detail.invoice_appearance == dto.InvoiceAppearance.PAPER

    assert inv.invoice_lines is not None
    assert inv.invoice_lines.merged_item_indicator is False
    assert inv.invoice_lines.line is not None
    lines = inv.invoice_lines.line

    assert len(lines) == 9

    first_line = lines[0]
    assert first_line.line_number == 1
    assert first_line.product_codes is not None
    assert first_line.product_codes.product_code is not None
    assert len(first_line.product_codes.product_code) == 1
    assert first_line.product_codes.product_code[0].product_code_category == dto.ProductCodeCategory.VTSZ
    assert first_line.product_codes.product_code[0].product_code_value == '10019120'
    assert first_line.product_codes.product_code[0].product_code_own_value is None
    assert first_line.line_expression_indicator is True
    assert first_line.line_nature_indicator == dto.LineNatureIndicator.PRODUCT
    assert first_line.line_description == 'Búza vetőmag'
    assert first_line.quantity == 10.0
    assert first_line.unit_of_measure == dto.UnitOfMeasure.TON
    assert first_line.unit_price == 50000.0
    assert first_line.line_amounts_normal is not None
    assert first_line.line_amounts_normal.line_net_amount_data is not None
    assert first_line.line_amounts_normal.line_net_amount_data.line_net_amount == 500000.0
    assert first_line.line_amounts_normal.line_net_amount_data.line_net_amount_huf == 500000.0
    assert first_line.line_amounts_normal.line_vat_rate is not None
    assert first_line.line_amounts_normal.line_vat_rate.vat_content is None
    assert first_line.line_amounts_normal.line_vat_rate.vat_amount_mismatch is None
    assert first_line.line_amounts_normal.line_vat_rate.vat_exemption is None
    assert first_line.line_amounts_normal.line_vat_rate.vat_percentage is None
    assert first_line.line_amounts_normal.line_vat_rate.no_vat_charge is None
    assert first_line.line_amounts_normal.line_vat_rate.vat_out_of_scope is None
    assert first_line.line_amounts_normal.line_vat_rate.margin_scheme_indicator is None
    assert first_line.line_amounts_normal.line_vat_rate.vat_domestic_reverse_charge is True
    assert first_line.line_amounts_normal.line_gross_amount_data.line_gross_amount_normal == 500000.0
    assert first_line.line_amounts_normal.line_gross_amount_data.line_gross_amount_normal_huf == 500000.0

    assert first_line.line_amounts_normal.line_vat_data is None

    second_line = lines[1]
    assert second_line.line_number == 2
    assert second_line.references_to_other_lines is not None
    assert second_line.references_to_other_lines.reference_to_other_line is not None
    assert len(second_line.references_to_other_lines.reference_to_other_line) == 1
    assert second_line.references_to_other_lines.reference_to_other_line[0] == 1
    assert second_line.product_codes is not None
    assert second_line.product_codes.product_code is not None
    assert len(second_line.product_codes.product_code) == 1
    assert second_line.product_codes.product_code[0].product_code_category == dto.ProductCodeCategory.TESZOR
    assert second_line.product_codes.product_code[0].product_code_value == '494115'
    assert second_line.product_codes.product_code[0].product_code_own_value is None
    assert second_line.line_expression_indicator is False
    assert second_line.line_nature_indicator == dto.LineNatureIndicator.SERVICE
    assert second_line.line_description == 'Búza vetőmag szállítása'
    assert second_line.line_amounts_normal is not None
    assert second_line.line_amounts_normal.line_net_amount_data is not None
    assert second_line.line_amounts_normal.line_net_amount_data.line_net_amount == 100000.0
    assert second_line.line_amounts_normal.line_net_amount_data.line_net_amount_huf == 100000.0
    assert second_line.line_amounts_normal.line_vat_rate is not None
    assert second_line.line_amounts_normal.line_vat_rate.vat_content is None
    assert second_line.line_amounts_normal.line_vat_rate.vat_amount_mismatch is None
    assert second_line.line_amounts_normal.line_vat_rate.vat_exemption is None
    assert second_line.line_amounts_normal.line_vat_rate.vat_percentage is None
    assert second_line.line_amounts_normal.line_vat_rate.no_vat_charge is None
    assert second_line.line_amounts_normal.line_vat_rate.vat_out_of_scope is None
    assert second_line.line_amounts_normal.line_vat_rate.margin_scheme_indicator is None
    assert second_line.line_amounts_normal.line_vat_rate.vat_domestic_reverse_charge is True
    assert second_line.line_amounts_normal.line_gross_amount_data.line_gross_amount_normal == 100000.0
    assert second_line.line_amounts_normal.line_gross_amount_data.line_gross_amount_normal_huf == 100000.0

    assert second_line.line_amounts_normal.line_vat_data is None


    third_line = lines[2]
    assert third_line.line_amounts_normal.line_vat_data is not None
    assert third_line.line_amounts_normal.line_vat_data.line_vat_amount == 28800.0
    assert third_line.line_amounts_normal.line_vat_data.line_vat_amount_huf == 28800.0

    # todo: other lines

    assert inv.invoice_summary is not None
    assert len(inv.invoice_summary.summary_simplified) == 0

    assert inv.invoice_summary.summary_normal is not None
    assert inv.invoice_summary.summary_normal.summary_by_vat_rate is not None
    assert len(inv.invoice_summary.summary_normal.summary_by_vat_rate) == 7

    first_summary_by_vat_rate = inv.invoice_summary.summary_normal.summary_by_vat_rate[0]
    assert first_summary_by_vat_rate.vat_rate is not None
    assert first_summary_by_vat_rate.vat_rate.vat_out_of_scope is not None
    assert first_summary_by_vat_rate.vat_rate.vat_out_of_scope.case == 'ATK'
    assert first_summary_by_vat_rate.vat_rate.vat_out_of_scope.reason == 'ÁFA hatályán kívül'
    assert first_summary_by_vat_rate.vat_rate.vat_content is None
    assert first_summary_by_vat_rate.vat_rate.vat_percentage is None
    assert first_summary_by_vat_rate.vat_rate.vat_exemption is None
    assert first_summary_by_vat_rate.vat_rate.no_vat_charge is None
    assert first_summary_by_vat_rate.vat_rate.vat_domestic_reverse_charge is None
    assert first_summary_by_vat_rate.vat_rate.margin_scheme_indicator is None
    assert first_summary_by_vat_rate.vat_rate.vat_amount_mismatch is None
    assert first_summary_by_vat_rate.vat_rate_net_data is not None
    assert first_summary_by_vat_rate.vat_rate_net_data.vat_rate_net_amount == 70000.0
    assert first_summary_by_vat_rate.vat_rate_net_data.vat_rate_net_amount_huf == 70000.0
    assert first_summary_by_vat_rate.vat_rate_vat_data.vat_rate_vat_amount == 0
    assert first_summary_by_vat_rate.vat_rate_vat_data.vat_rate_vat_amount_huf == 0
    assert first_summary_by_vat_rate.vat_rate_gross_data.vat_rate_gross_amount == 70000.0
    assert first_summary_by_vat_rate.vat_rate_gross_data.vat_rate_gross_amount_huf == 70000.0

    second_summary_by_vat_rate = inv.invoice_summary.summary_normal.summary_by_vat_rate[1]
    assert second_summary_by_vat_rate.vat_rate is not None
    assert second_summary_by_vat_rate.vat_rate.vat_out_of_scope is None
    assert second_summary_by_vat_rate.vat_rate.vat_content is None
    assert second_summary_by_vat_rate.vat_rate.vat_percentage is None
    assert second_summary_by_vat_rate.vat_rate.vat_exemption is not None
    assert second_summary_by_vat_rate.vat_rate.vat_exemption.case == 'TAM'
    assert second_summary_by_vat_rate.vat_rate.vat_exemption.reason == 'Mentes ÁFA tv. 85.§ (1) i)'
    assert second_summary_by_vat_rate.vat_rate.no_vat_charge is None
    assert second_summary_by_vat_rate.vat_rate.vat_domestic_reverse_charge is None
    assert second_summary_by_vat_rate.vat_rate.margin_scheme_indicator is None
    assert second_summary_by_vat_rate.vat_rate.vat_amount_mismatch is None
    assert second_summary_by_vat_rate.vat_rate_net_data is not None
    assert second_summary_by_vat_rate.vat_rate_net_data.vat_rate_net_amount == 960000.0
    assert second_summary_by_vat_rate.vat_rate_net_data.vat_rate_net_amount_huf == 960000.0
    assert second_summary_by_vat_rate.vat_rate_vat_data.vat_rate_vat_amount == 0
    assert second_summary_by_vat_rate.vat_rate_vat_data.vat_rate_vat_amount_huf == 0
    assert second_summary_by_vat_rate.vat_rate_gross_data.vat_rate_gross_amount == 960000.0
    assert second_summary_by_vat_rate.vat_rate_gross_data.vat_rate_gross_amount_huf == 960000.0

    third_summary_by_vat_rate = inv.invoice_summary.summary_normal.summary_by_vat_rate[2]
    assert third_summary_by_vat_rate.vat_rate is not None
    assert third_summary_by_vat_rate.vat_rate.vat_out_of_scope is None
    assert third_summary_by_vat_rate.vat_rate.vat_content is None
    assert third_summary_by_vat_rate.vat_rate.vat_percentage is None
    assert third_summary_by_vat_rate.vat_rate.vat_exemption is None
    assert third_summary_by_vat_rate.vat_rate.no_vat_charge is None
    assert third_summary_by_vat_rate.vat_rate.vat_domestic_reverse_charge is True
    assert third_summary_by_vat_rate.vat_rate.margin_scheme_indicator is None
    assert third_summary_by_vat_rate.vat_rate.vat_amount_mismatch is None
    assert third_summary_by_vat_rate.vat_rate_net_data is not None
    assert third_summary_by_vat_rate.vat_rate_net_data.vat_rate_net_amount == 600000.0
    assert third_summary_by_vat_rate.vat_rate_net_data.vat_rate_net_amount_huf == 600000.0
    assert third_summary_by_vat_rate.vat_rate_vat_data.vat_rate_vat_amount == 0
    assert third_summary_by_vat_rate.vat_rate_vat_data.vat_rate_vat_amount_huf == 0
    assert third_summary_by_vat_rate.vat_rate_gross_data.vat_rate_gross_amount == 500000.0
    assert third_summary_by_vat_rate.vat_rate_gross_data.vat_rate_gross_amount_huf == 500000.0

    # todo: other summary_by_vat_rates

    assert inv.invoice_summary.summary_normal.invoice_net_amount == 2980000.0
    assert inv.invoice_summary.summary_normal.invoice_net_amount_huf == 2980000.0
    assert inv.invoice_summary.summary_normal.invoice_vat_amount == 283600.0
    assert inv.invoice_summary.summary_normal.invoice_vat_amount_huf == 283600.0

    assert inv.invoice_summary.summary_gross_data is not None
    assert inv.invoice_summary.summary_gross_data.invoice_gross_amount == 3263000.0
    assert inv.invoice_summary.summary_gross_data.invoice_gross_amount_huf == 3263000.0
