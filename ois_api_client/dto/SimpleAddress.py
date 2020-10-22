from typing import Union


class SimpleAddress:
    """Simple address type

    :param postal_code: ZIP code (If can not be interpreted, need to be filled "0000")
    :param city: Settlement
    :param additional_address_detail: Further address data (name and type of public place, house number, floor, door, lot number, etc.)
    :param country_code: ISO 3166 alpha-2 country code
    :param region: ISO 3166 alpha-2 province code (if appropriate in a given country)
    """

    def __init__(self,
                 postal_code: str,
                 city: str,
                 additional_address_detail: str,
                 country_code: str = 'HU',
                 region: Union[str, None] = None):
        self.country_code = country_code
        self.region = region
        self.postal_code = postal_code
        self.city = city
        self.additional_address_detail = additional_address_detail
