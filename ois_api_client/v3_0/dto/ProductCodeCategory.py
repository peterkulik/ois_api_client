from enum import Enum


class ProductCodeCategory(Enum):
    """The type used to mark the kind of product code"""
    VTSZ = 'VTSZ'
    """Customs tariff number CTN"""
    SZJ = 'SZJ'
    """Business service list number BSL"""
    KN = 'KN'
    """CN code (Combined Nomenclature, 2658/87/ECC Annex I)"""
    AHK = 'AHK'
    """Administrative reference code of e-TKO defined in the Act LXVIII of 2016 on Excise Duties"""
    CSK = 'CSK'
    """Packaging product catalogue code of the product according to the Title A) in the Schedule No.1 of the Government Decree No. 343/2011. (XII. 29.)"""
    KT = 'KT'
    """Environmental protection product code of the product according to the Title B) in the Schedule No.1 of the Government Decree No. 343/2011. (XII. 29.)"""
    EJ = 'EJ'
    """Classification of Inventory of Construction"""
    TESZOR = 'TESZOR'
    """Product code according to the TESZOR (Hungarian Classification of Goods and Services), Classification of Product by Activity, CPA - regulation 451/2008/EC"""
    OWN = 'OWN'
    """The own product code of the enterprise"""
    OTHER = 'OTHER'
    """Other product code"""
