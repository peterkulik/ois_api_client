from datetime import datetime, date
import pytest

import ois_api_client as ois
from ois_api_client import InvoiceCategory, PaymentMethod, InvoiceAppearance, Source
from tests.common import config


@pytest.mark.skip()
def test_query_invoice_digest_request_with_additional_parameters():
    client = ois.Client(config.service_url, config.signature_key, config.replacement_key, config.password)

    data = ois.QueryInvoiceDigestRequest(
        header=ois.BasicHeader(request_id=config.get_request_id(), timestamp=config.get_timestamp()),
        user=config.user,
        software=config.software,
        page=1,
        invoice_direction=ois.InvoiceDirection.INBOUND,
        invoice_query_params=ois.InvoiceQueryParams(
            mandatory_query_params=ois.MandatoryQueryParams(
                parameter=ois.MandatoryQueryParams.InsDate(
                    ins_date=ois.DateTimeIntervalParam(
                        date_time_from=datetime(2020, 10, 1),
                        date_time_to=datetime(2020, 10, 30)
                    ))),
            additional_query_params=ois.AdditionalQueryParams(
                tax_number='12345678',
                name='SUPPLIER NAME',
                invoice_category=InvoiceCategory.NORMAL,
                payment_method=PaymentMethod.TRANSFER,
                invoice_appearance=InvoiceAppearance.PAPER,
                source=Source.XML,
                currency="HUF"
            ),
            relational_query_params=ois.RelationalQueryParams(
                # invoice_delivery=RangeDate(
                #     from_operator=RangeDate.FromOperator.GT,
                #     from_value=date(2020, 10, 1),
                #     to_operator=RangeDate.ToOperator.LT,
                #     to_value=date(2020, 11, 1)
                # )
                # invoice_delivery=ois.RelationQueryDate(
                #     query_operator=ois.QueryOperator.LT,
                #     query_value=date(2020, 10, 21)
                # )
                invoice_delivery=date(2020, 10, 9),
                # payment_date=RangeDate(
                #     from_operator=RangeDate.FromOperator.GT,
                #     from_value=date(2020, 10, 1),
                #     to_operator=RangeDate.ToOperator.LT,
                #     to_value=date(2020, 11, 1)
                # )
                # payment_date=ois.RelationQueryDate(
                #     query_operator=ois.QueryOperator.LT,
                #     query_value=date(2020, 10, 21)
                # )
                # payment_date=date(2020, 10, 20),
                # invoice_net_amount=RangeMonetary(
                #     from_operator=RangeMonetary.FromOperator.GT,
                #     from_value=1,
                #     to_operator=RangeMonetary.ToOperator.LT,
                #     to_value=2000000.15
                # )
                # invoice_net_amount=ois.RelationQueryMonetary(
                #     query_operator=ois.QueryOperator.GTE,
                #     query_value=40
                # )
                invoice_net_amount=40,
                # invoice_net_amount_huf=RangeMonetary(
                #     from_operator=RangeMonetary.FromOperator.GTE,
                #     from_value=40,
                #     to_operator=RangeMonetary.ToOperator.LT,
                #     to_value=2000000.15
                # )
                # invoice_net_amount=ois.RelationQueryMonetary(
                #     query_operator=ois.QueryOperator.GTE,
                #     query_value=40
                # )
                invoice_net_amount_huf=40,
                # invoice_vat_amount=RangeMonetary(
                #     from_operator=RangeMonetary.FromOperator.GTE,
                #     from_value=4.2,
                #     to_operator=RangeMonetary.ToOperator.LT,
                #     to_value=2000000.15
                # )
                # invoice_vat_amount=ois.RelationQueryMonetary(
                #     query_operator=ois.QueryOperator.GTE,
                #     query_value=4.1
                # )
                invoice_vat_amount=4.2,
                # invoice_vat_amount_huf=RangeMonetary(
                #     from_operator=RangeMonetary.FromOperator.GTE,
                #     from_value=4.2,
                #     to_operator=RangeMonetary.ToOperator.LTE,
                #     to_value=4.3
                # )
                # invoice_vat_amount_huf=ois.RelationQueryMonetary(
                #     query_operator=ois.QueryOperator.GTE,
                #     query_value=4.1
                # )
                invoice_vat_amount_huf=4.2
            ),
            transaction_query_params=ois.TransactionQueryParams(
                transaction_id='34NYMAM1OO7VON33',
                index=1,
                invoice_operation=ois.ManageInvoiceOperation.CREATE
            )
        )
    )
    response = client.query_invoice_digest(data)

    assert response is not None
    assert response.result is not None
    assert response.result.func_code == 'OK'
    assert response.result.message is None
    assert response.result.error_code is None
    assert response.invoice_digest_result is not None
    assert response.invoice_digest_result.current_page == 1
    assert response.invoice_digest_result.available_page == 1
    assert response.invoice_digest_result.invoice_digest is not None
    assert len(response.invoice_digest_result.invoice_digest) > 0
