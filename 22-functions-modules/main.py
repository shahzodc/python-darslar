# MODULNI CHAQIRIB OLAMIZ

import avto_info_mod # avto_info_mod modulini chaqiramiz

avto1 = avto_info_mod.avto_info("GM","Malibu","Qora",\
                                "avtomat",2022,40000)
avto_info_mod.info_print(avto1)


# MODULGA QISQA NOM BERISH
import avto_info_mod as aim
avto1 = aim.avto_info("GM","Malibu","Qora","avtomat",2022,40000)
aim.info_print(avto1)


# MODUL ICHIDAN MA'LUM FUNKSIYALARNI CHAQIRIB OLISH
from avto_info_mod import avto_info, info_print
avto1=avto_info("GM","Malibu","Qora","avtomat",2022,40000)
info_print(avto1)


# FUNKSIYALARGA QISQA NOM BERISH
from avto_info_mod import avto_info as ainfo
from avto_info_mod import info_print as iprint
avto1 = ainfo("GM",'Malibu',"Qora",'avtomat',2022,40000)
iprint(avto1)


# MODUL ICHIDAGI BARCHA FUNKSIYALARNI CHAQIRIB OLISH
from avto_info_mod import *
avto1 = avto_info("GM","Malibu","Qora","avtomat",2022,40000)
info_print(avto1)


# MODULDA O'ZGARUVCHI SAQLASH 
# MODUL ICHIDAGI O'ZGARUVCHILARGA HAM 
# XUDDI YUQORIDAGI USULLAR BILAN MUROJAAT ETAMIZ




























































