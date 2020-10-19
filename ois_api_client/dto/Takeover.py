from enum import Enum


class Takeover(Enum):
    """Field type for data of takeover"""
    TO_01 = '01'
    """The supplier takes over buyer’s product fee liability on the basis of Paragraph (4), Section 14 of the Act 
    LXXXV of 2011 """
    TO_02_aa = '02_aa'
    """On the basis of contract, the buyer takes over supplier’s product fee liability on the basis of sub-point aa), 
    Paragraph (5), Section 14 of the Act LXXXV of 2011 """
    TO_02_ab = '02_ab'
    TO_02_b = '02_b'
    TO_02_c = '02_c'
    TO_02_d = '02_d'
    TO_02_ea = '02_ea'
    TO_02_eb = '02_eb'
    TO_02_fa = '02_fa'
    TO_02_fb = '02_fb'
    TO_02_ga = '02_ga'
    TO_02_gb = '02_gb'
