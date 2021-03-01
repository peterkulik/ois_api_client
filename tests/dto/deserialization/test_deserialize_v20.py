import xml.etree.ElementTree as ET
from ois_api_client.v2_0 import deserialization, dto
from datetime import datetime
from tests.get_root_dir import get_root_dir


def test_deserialize_v20(pytestconfig):
    dir_ = get_root_dir(pytestconfig)

    with open(f'{dir_}/tests/dto/deserialization/v20/test.xml', 'r') as file:
        xml = file.read().replace('\n', '')

    root: ET.Element = ET.fromstring(xml)
    result = deserialization.deserialize_invoice_data(root)

    assert result is not None
    assert result.invoice_number == '2020/000123'
    assert result.invoice_issue_date == datetime(2020, 5, 15)
    assert result.invoice_main is not None
    assert result.invoice_main.invoice is not None

    inv = result.invoice_main.invoice
    assert inv.invoice_head is not None
    head = inv.invoice_head
    assert head.supplier_info is not None
    supplier = head.supplier_info

    assert supplier.supplier_name == 'Szállító Kft'
    assert supplier.supplier_tax_number is not None
    assert supplier.supplier_tax_number.taxpayer_id == '11111111'
    assert supplier.supplier_tax_number.vat_code == '2'
    assert supplier.supplier_tax_number.county_code == '42'
    assert supplier.supplier_address is not None
    assert supplier.supplier_address.detailed_address is not None
    assert supplier.supplier_address.detailed_address.country_code == 'HU'
    assert supplier.supplier_address.detailed_address.postal_code == '1111'
    assert supplier.supplier_address.detailed_address.city == 'Budapest'
    assert supplier.supplier_address.detailed_address.street_name == 'Példa'
    assert supplier.supplier_address.detailed_address.public_place_category == 'utca'
    assert supplier.supplier_address.detailed_address.number == '777'
    assert supplier.supplier_address.detailed_address.floor == '1.'
    assert supplier.supplier_address.detailed_address.door == '3.'
    assert supplier.supplier_bank_account_number == '88888888-66666666-12345678'

    assert head.customer_info is not None
    customer = head.customer_info
    assert customer.customer_tax_number is not None
    assert customer.customer_tax_number.taxpayer_id == '33333333'
    assert customer.customer_tax_number.vat_code == '2'
    assert customer.customer_tax_number.county_code == '02'
    assert customer.customer_name == 'Vevő Kft'
    assert customer.customer_address is not None
    assert customer.customer_address.detailed_address is not None
    assert customer.customer_address.detailed_address.country_code == 'HU'
    assert customer.customer_address.detailed_address.postal_code == '7600'
    assert customer.customer_address.detailed_address.city == 'Pécs'
    assert customer.customer_address.detailed_address.street_name == 'Kitalált'
    assert customer.customer_address.detailed_address.public_place_category == 'köz'
    assert customer.customer_address.detailed_address.number == '8'

    assert head.invoice_detail is not None
    inv_detail = head.invoice_detail

    assert inv_detail.invoice_category == dto.InvoiceCategory.NORMAL
    assert inv_detail.invoice_delivery_date == datetime(2020, 5, 10)
    assert inv_detail.currency_code == 'HUF'
    assert inv_detail.exchange_rate == 1.0
    assert inv_detail.payment_method is None
    assert inv_detail.payment_date == datetime(2020, 5, 30)
    assert inv_detail.invoice_appearance == dto.InvoiceAppearance.PAPER

    assert inv_detail.additional_invoice_data is not None
    assert len(inv_detail.additional_invoice_data) == 1
    assert inv_detail.additional_invoice_data[0].data_name == 'X00001_MRSZ'
    assert inv_detail.additional_invoice_data[0].data_description == 'MRSZ'
    assert inv_detail.additional_invoice_data[0].data_value == 'Megrendelés szám: 12345678/2020'

    assert inv.invoice_lines is not None
    assert inv.invoice_lines.line is not None
    lines = inv.invoice_lines.line

    assert len(lines) == 4

    first_line = lines[0]
    assert first_line.line_number == 1
    assert first_line.product_codes is not None
    assert first_line.product_codes.product_code is not None
    assert len(first_line.product_codes.product_code) == 1
    assert first_line.product_codes.product_code[0].product_code_category == dto.ProductCodeCategory.VTSZ
    assert first_line.product_codes.product_code[0].product_code_value == '02031110'
    assert first_line.product_codes.product_code[0].product_code_own_value is None
    assert first_line.line_expression_indicator is True
    assert first_line.line_nature_indicator == dto.LineNatureIndicator.PRODUCT
    assert first_line.line_description == 'Hűtött házi sertés (fél)'
    assert first_line.quantity == 1500.00
    assert first_line.unit_of_measure == dto.UnitOfMeasure.KILOGRAM
    assert first_line.unit_price == 400.0
    assert first_line.line_amounts_normal is not None
    assert first_line.line_amounts_normal.line_net_amount_data is not None
    assert first_line.line_amounts_normal.line_net_amount_data.line_net_amount == 600000.0
    assert first_line.line_amounts_normal.line_net_amount_data.line_net_amount_huf == 600000.0
    assert first_line.line_amounts_normal.line_vat_rate is not None
    assert first_line.line_amounts_normal.line_vat_rate.vat_exemption is None
    assert first_line.line_amounts_normal.line_vat_rate.vat_percentage == 0.05
    assert first_line.line_amounts_normal.line_vat_rate.vat_out_of_scope is None
    assert first_line.line_amounts_normal.line_vat_rate.vat_domestic_reverse_charge is None

    assert first_line.line_amounts_normal.line_gross_amount_data is not None
    assert first_line.line_amounts_normal.line_gross_amount_data.line_gross_amount_normal == 630000.0
    assert first_line.line_amounts_normal.line_gross_amount_data.line_gross_amount_normal_huf == 630000.0

    assert first_line.line_amounts_normal.line_vat_data is not None
    assert first_line.line_amounts_normal.line_vat_data.line_vat_amount == 30000.0
    assert first_line.line_amounts_normal.line_vat_data.line_vat_amount == 30000.0

    assert inv.invoice_summary is not None
    assert len(inv.invoice_summary.summary_simplified) == 0

    assert inv.invoice_summary.summary_normal is not None
    assert inv.invoice_summary.summary_normal.summary_by_vat_rate is not None
    assert len(inv.invoice_summary.summary_normal.summary_by_vat_rate) == 2

    first_summary_by_vat_rate = inv.invoice_summary.summary_normal.summary_by_vat_rate[0]
    assert first_summary_by_vat_rate.vat_rate is not None
    assert first_summary_by_vat_rate.vat_rate.vat_out_of_scope is None
    assert first_summary_by_vat_rate.vat_rate.vat_percentage == 0.05
    assert first_summary_by_vat_rate.vat_rate.vat_exemption is None
    assert first_summary_by_vat_rate.vat_rate.vat_domestic_reverse_charge is None
    assert first_summary_by_vat_rate.vat_rate_net_data is not None
    assert first_summary_by_vat_rate.vat_rate_net_data.vat_rate_net_amount == 600000.0
    assert first_summary_by_vat_rate.vat_rate_net_data.vat_rate_net_amount_huf == 600000.0
    assert first_summary_by_vat_rate.vat_rate_vat_data.vat_rate_vat_amount == 30000.0
    assert first_summary_by_vat_rate.vat_rate_vat_data.vat_rate_vat_amount_huf == 30000.0
    assert first_summary_by_vat_rate.vat_rate_gross_data.vat_rate_gross_amount == 630000.0
    assert first_summary_by_vat_rate.vat_rate_gross_data.vat_rate_gross_amount_huf == 630000.0

    assert inv.invoice_summary.summary_normal.invoice_net_amount == 4952000.0
    assert inv.invoice_summary.summary_normal.invoice_net_amount_huf == 4952000.0
    assert inv.invoice_summary.summary_normal.invoice_vat_amount == 1205040.0
    assert inv.invoice_summary.summary_normal.invoice_vat_amount_huf == 1205040.0

    assert inv.invoice_summary.summary_gross_data is not None
    assert inv.invoice_summary.summary_gross_data.invoice_gross_amount == 6157040.0
    assert inv.invoice_summary.summary_gross_data.invoice_gross_amount_huf == 6157040.0

