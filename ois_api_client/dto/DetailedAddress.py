from typing import Union, Optional


class DetailedAddress:
    """Detailed address data

    :param country_code: ISO 3166 alpha-2 country code
    :param postal_code: ZIP code (If can not be interpreted, need to be filled "0000")
    :param city: Settlement
    :param street_name: Name of public place
    :param public_place_category: Category of public place
    :param region: ISO 3166 alpha-2 province code (if appropriate in a given country)
    :param number: House number
    :param building: Building
    :param staircase: Staircase
    :param floor: Floor
    :param door: Door number
    :param lot_number: Lot number
    """

    def __init__(self,
                 country_code: str,
                 postal_code: str,
                 city: str,
                 street_name: str,
                 public_place_category: str,
                 region: Optional[str] = None,
                 number: Optional[str] = None,
                 building: Optional[str] = None,
                 staircase: Optional[str] = None,
                 floor: Optional[str] = None,
                 door: Optional[str] = None,
                 lot_number: Optional[str] = None):
        self.country_code = country_code
        self.region = region
        self.postal_code = postal_code
        self.city = city
        self.street_name = street_name
        self.public_place_category = public_place_category
        self.number = number
        self.building = building
        self.staircase = staircase
        self.floor = floor
        self.door = door
        self.lot_number = lot_number
