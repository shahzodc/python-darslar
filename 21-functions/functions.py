# # MOSLASHUVCHAN FUNKSIYA(*args, **kwargs)

# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini qayataruvchi funksiya"""
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi

# print(summa(1,2,3,4,5,6,7))

# # OSONROQ USULDA YARATAMIZ
# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini qaytaruvchi funksiya"""
#     return sum(sonlar)

# print(summa(4,5,6,7))

# # AGAR FUNKSIYA BIR NECHTA ARGUMENT 
# # QABUL QILSA *args ARGUMENTI DOIM OXIRIDA YOZILADI
# def summa(x,y,*sonlar):
#     """Kiritilgan sonlar yig'indisini qaytaruvchi funksiya"""
#     return x+y+sum(sonlar)

# print(summa(2,3,4,2,4,5,65))

# **kwargs USULI
def avto_info(kompaniya,model,**malumotlar):
    """Avto haqidagi ma'lumotlarni lug'at
    ko'rinishida qaytaruvchi funksiya"""
    malumotlar['kompaniya']=kompaniya
    malumotlar['model']=model
    return malumotlar

avto1 = avto_info('GM, malibu', rang='qora', yil=2018)
avto2 = avto_info("Kia", 'K5', rang='qizil', narx=35000)
print(avto2)
    


    















