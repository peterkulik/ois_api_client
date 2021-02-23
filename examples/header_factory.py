import ois_api_client as ois
from ois_api_client.header_factory import make_default_header_factory, make_header_factory


def _() -> ois.HeaderFactoryParameters:
    """Loads online invoice api authentication settings
    Although this example uses fix values, you can use your secure custom solution to load your settings"""
    return ois.HeaderFactoryParameters(
        login='mr0tapeogrpmmkg',
        tax_number='68293008',
        password='Len123_Ovo',
        signature_key='bf-a7fe-4d5ccb8ec0c72VIKJ21AJZ02'
    )


# Use make_default_header_factory if you don't want to implement custom request id generation and timestamp
make_headers = make_default_header_factory(load_parameters=_)

# Use make_header_factory if you want to generate the request id and/or want to set the timestamp of the request
# make_headers = make_header_factory(load_parameters=_)
#
# header, user_header = make_headers(
#     'your_unique_request_id',
#     datetime.now()  # timestamp
# )
