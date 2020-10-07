from datetime import datetime
from ois_client_sdk import User, Software


def get_local_timezone():
    return datetime.now().astimezone().tzinfo


service_url = 'https://api-test.onlineszamla.nav.gov.hu/invoiceService/v2'
signature_key = 'bf-a7fe-4d5ccb8ec0c72VIKJ21AJZ02'
replacement_key = '3de02VIKJ21BMJBB'
request_id = '202010052156'
password = 'Len123_Ovo'
user = User(login='mr0tapeogrpmmkg',
            tax_number='68293008')
software = Software(id='HUU10000000TESTNUM',
                    name='SuperSoftware',
                    operation='LOCAL_SOFTWARE',
                    main_version='1.0',
                    dev_name='John Doe',
                    dev_contact='info@johndoe.com',
                    dev_country_code='HU',
                    dev_tax_number='12345678')
timestamp = datetime(2020, 10, 7, 13, 26, 0, 000000, tzinfo=get_local_timezone())
expected_request_signature = 'ACB2695B7D55DA520F39FC829DB9190B0A61F54D4F29A6CB8EBA59A585B116ACA09F724CC45967E9A86F82D8CD0624263DA38BF71A69E094E9734B4D35702C26'
expected_password_hash = '6F458D2CD4D1519B1D6C7FEF6F4F84827BC8099D1910A406048E5E80079952A4E49E7EFCC9E93F31A8B4D327B603E9EFF9DD1DCEE47FE82201C49AFD1A9B707B'