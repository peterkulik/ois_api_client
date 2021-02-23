from ois_api_client.v3_0 import dto

software = dto.Software(
    software_id='HUU10000000TESTNUM',
    software_name='SuperSoftware',
    software_operation=dto.SoftwareOperation.LOCAL_SOFTWARE,
    software_main_version='1.0',
    software_dev_name='John Doe',
    software_dev_contact='info@johndoe.com',
    software_dev_country_code='HU',
    software_dev_tax_number='12345678')
