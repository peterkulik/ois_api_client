from typing import Optional
from dataclasses import dataclass


@dataclass
class DetailedAddress:
    """Detailed address data

    :param country_code: ISO 3166 alpha-2 country code
    :param region: ISO 3166 alpha-2 province code (if appropriate in a given country)
    :param postal_code: ZIP code (If can not be interpreted, need to be filled "0000")
    :param city: Settlement
    :param street_name: Name of public place
    :param public_place_category: Category of public place
    :param number: House number
    :param building: Building
    :param staircase: Staircase
    :param floor: Floor
    :param door: Door number
    :param lot_number: Lot number
    """

    country_code: str
    region: Optional[str]
    postal_code: str
    city: str
    street_name: str
    public_place_category: str
    number: Optional[str]
    building: Optional[str]
    staircase: Optional[str]
    floor: Optional[str]
    door: Optional[str]
    lot_number: Optional[str]
