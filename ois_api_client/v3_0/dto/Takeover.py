from enum import Enum


class Takeover(Enum):
    """Field type for data of takeover"""
    T_01 = '01'
    """The supplier takes over buyer’s product fee liability on the basis of Paragraph (4), Section 14 of the Act LXXXV of 2011"""
    T_02_AA = '02_aa'
    """On the basis of contract, the buyer takes over supplier’s product fee liability on the basis of sub-point aa), Paragraph (5), Section 14 of the Act LXXXV of 2011"""
    T_02_AB = '02_ab'
    T_02_B = '02_b'
    T_02_C = '02_c'
    T_02_D = '02_d'
    T_02_EA = '02_ea'
    T_02_EB = '02_eb'
    T_02_FA = '02_fa'
    T_02_FB = '02_fb'
    T_02_GA = '02_ga'
    T_02_GB = '02_gb'
