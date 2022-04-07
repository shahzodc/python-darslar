
# map() FUNKSIYASI
from math import sqrt
sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
ildizlar = list(map(sqrt,sonlar))
print(ildizlar)

sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
def daraja2(x):
    """Berilgan sonning kvadratini qaytaruvchi funksiya"""
    return x*x
print(list(map(daraja2,sonlar)))

# lambda FUNKSIYASI YORDAMIDA YOZAMIZ
sonlar = list(range(11))
kvadratlar = list(map(lambda x:x*x,sonlar))
print(kvadratlar)

# for YORDAMIDA YOZAMIZ
sonlar = list(range(11))
kvadratlar = []
for son in sonlar:
    kvadratlar.append(son*son)
print(kvadratlar)

# map() FUNKSIYASIGA BIR NECHTA RO'YXATLAR HAM UZATISH MUMKIN
a = [4, 5, 6]
b = [7, 8, 9]
a_plus_b = list(map(lambda x,y:x+y,a,b))
print(a_plus_b)

# map() istalgan ko'rinishdagi ma'lumot turlari bilan ishlaydi
ismlar = ['hasan','husan','olim','umid']
print(list(map(lambda matn:matn.upper(),ismlar)))


