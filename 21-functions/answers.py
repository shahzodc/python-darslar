# AMALIYOT

#1
def kopaytma(*sonlar):
    """Kiritilgan sonlar ko'paytmasini qaytaruvchi dastur"""
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
        return kopaytma
print(kopaytma(4,5,6,8))


#2
def talaba(ism,familiya,**malumotlar):
    """Talabalar haqida ma'lumotlarni lug'at ko'rinishida qaytaruvchi dastur"""
    malumotlar['ism']=ism
    malumotlar['familiya']=familiya
    return malumotlar

talaba1 = talaba("shahzod","rahimberdiyev",kasbi='dasturchi')
print(talaba1)


    
