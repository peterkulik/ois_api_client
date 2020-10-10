# ois_api_client 
**Online Invoice System API Client**

*API Version: 2.0*

**The library is under active development!**

## What is it?
**ois_api_client** is a python client for the hungarian, offical Online Invoice System public API.
You can find the API documentation here:

https://onlineszamla.nav.gov.hu/dokumentaciok

**Implemented API requests:**
- query_invoice_digest
- query_invoice_data
- token_exchange

## Where to get it
```sh
# PyPI
pip install ois_api_client
```

## License
[MIT](LICENSE)

## Usage

- Build up your client
```python
import ois_api_client as ois
from datetime import datetime, timezone

client = ois.Client(
    uri='https://api-test.onlineszamla.nav.gov.hu/invoiceService/v2',    
    signature_key='your_signature_key',
    replacement_key='youre_replacement_key',
    password='your_password'
)
```

- Build up general parameters for each request
```python
user = ois.UserHeader(
    login='your_login',
    tax_number='your_taxnumbers_first_8_character')

software = ois.Software(
    id='your_software_id',
    name='your_software_name',
    operation='LOCAL_SOFTWARE',
    main_version='your_software_version',
    dev_name='your_software_dev_name',
    dev_contact='your_software_dev_email',
    dev_country_code='your_software_dev_country_code',
    dev_tax_number='yourc_software_dev_tax_number')
```

- List invoices
```python
digest_request = ois.QueryInvoiceDigestRequest(
    header=ois.BasicHeader(
        request_id='your_generated_unique_request_id',
        timestamp=datetime.now().astimezone(tz=timezone.utc)),
    user=user,
    software=software,
    page=1,
    invoice_direction=ois.InvoiceDirection.INBOUND,
    invoice_query_params=ois.InvoiceQueryParams(
        ois.MandatoryQueryParams(
            ois.MandatoryQueryParams.InsDate(
                ois.DateTimeIntervalParam(
                    date_time_from=datetime(2020, 10, 1),
                    date_time_to=datetime(2020, 10, 30)
                ))))
)

try:
    digest_response = client.query_invoice_digest(digest_request)

    print(digest_response.invoice_digest_result.available_page)
    print(digest_response.invoice_digest_result.current_page)

    for i in digest_response.invoice_digest_result.invoice_digest:
        print(i.invoice_number)
        # ...
except ois.GeneralError as err:
    gen_err: ois.GeneralErrorResponse = ois.deserialize_general_error_response(err.general_error_response)
    print(gen_err.result.message)
    print(gen_err.result.error_code)
    print(gen_err.result.func_code)

    for tvm in gen_err.technical_validation_messages:
        print(tvm.message)
        print(tvm.validation_error_code)
        print(tvm.validation_result_code)
except Exception as err:
    print(err)
```

- Get details of an invoice
```python
data_request = ois.QueryInvoiceDataRequest(
    header=ois.BasicHeader(
        request_id='your_generated_unique_request_id',
        timestamp=datetime.now()),
    user=user,
    software=software,
    invoice_number_query=ois.InvoiceNumberQuery(
        invoice_number='12345678/2020',
        invoice_direction=ois.InvoiceDirection.OUTBOUND,
        batch_index=None,
        supplier_tax_number=None
    )
)

try:
    data_response = client.query_invoice_data(data_request)
    invoice_xml_as_string = ois.decode_invoice_data(data_response.invoice_data_result.invoice_data)
    print(invoice_xml_as_string)
except ois.GeneralError as err:
    gen_err: ois.GeneralErrorResponse = ois.deserialize_general_error_response(err.general_error_response)
    print(gen_err.result.message)
    print(gen_err.result.error_code)
    print(gen_err.result.func_code)

    for tvm in gen_err.technical_validation_messages:
        print(tvm.message)
        print(tvm.validation_error_code)
        print(tvm.validation_result_code)
except Exception as err:
    print(err)
```



