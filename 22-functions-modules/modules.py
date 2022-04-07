# MODULES

# math MODULI
# sqrt() - qavs ichida berilgan qiymatning kvadrat ildizini qaytaradi
import math
x=400
print(math.sqrt(x))

# pow(x,n) - x ning n-darajasini qaytaruvchi funksiya
import math
print(math.pow(5,5))

# pi - ning qiymatini saqlovchi o'zgaruvchi 
from math import pi
print(pi)

# log2(x) va log10(x) - x ning 2 lik va
# 10 lik logarifmlarini qaytaruvchu funksiyalar
import math
print(math.log2(8))
print(math.log10(100))


# random MODULI
# randint(a,b)
import random as r # random modulini r deb chaqiramiz
son = r.randint(0,100)
print(son)

# choice(x) 
ismlar = ['olim','anvar','hasan','husan']
ism = r.choice(ismlar) # tasodifiy ism tanlaymiz
print(ism)

# yana bir misol:
x = list(range(0,51,5)) # ro'yxat yaratamiz
print(x)
print(r.choice(x)) # tasodifiy element tanlaymiz

# shuffle(x) - x ichidagi elementlarni tasodifiy qaytaruvchi funksiya
x = list(range(11)) # ro'yxat yaratamiz
print(x)
r.shuffle(x) # ro'yxatni aralashtirib tashlaymiz
print(x)

# sample(x,k) - x ro'yxat ichidan tasodifiy 
# k ta elementni ajratib olish
from random import sample 
x = list(range(0,100)) # 0 dan 100 gacha sonlar ro'yxati
y = sample(x,k=10) # ro'yxatdan 10 ta element ajratish
print(y)