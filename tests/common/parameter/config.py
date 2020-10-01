from datetime import datetime

from ois_client_sdk.common.parameter.Software import Software


def get_local_timezone():
    return datetime.now().astimezone().tzinfo


service_url = 'https://api-test.onlineszamla.nav.gov.hu/invoiceService/v2'
signature_key = 'bf-a7fe-4d5ccb8ec0c72VIKJ21AJZ02'
replacement_key = '3de02VIKJ21BMJBB'
request_id = 'bcead463430d48ef8b42ccd18b24fd'
request_version = '2.0'
header_version = '1.0'
login = 'test_login'
tax_number = '98765432'
password = 'Len123_Ovo'
software = Software(id='Super12345Software',
                    name='SuperSoftware',
                    operation='LOCAL_SOFTWARE',
                    main_version='1.0',
                    dev_name='John Doe',
                    dev_contact='info@johndoe.com',
                    dev_country_code='HU',
                    dev_tax_number='12345678')
timestamp = datetime(2020, 9, 29, 9, 35, 25, 132000, tzinfo=get_local_timezone())
expected_request_signature = '51EC5ABA9140BCB1927195CDF4E0FA3BA3F57E153B95FE7FADFA103F84FD8CF8AB62B321EDC17E02123896150B463A16A50E56494FAC39058D0B6226B03A484F'
expected_password_hash = '6F458D2CD4D1519B1D6C7FEF6F4F84827BC8099D1910A406048E5E80079952A4E49E7EFCC9E93F31A8B4D327B603E9EFF9DD1DCEE47FE82201C49AFD1A9B707B'