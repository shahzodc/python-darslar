# filter() FUNKSIYA
# juft sonlarni qaytaruvchi funksiya
import random as r
sonlar = r.sample(range(100),10)
def juftmi(x):
    """x juft bo'lsa True, aks holda, False qaytramiz"""
    return x%2==0

juft_sonlar = list(filter(juftmi,sonlar))
print(sonlar)
print(juft_sonlar)

# lambda YORDAMIDA YOZIB KO'RAMIZ
import random as r
sonlar = r.sample(range(100),10)
juft_sonlar = list(filter(lambda son: son%2==0,sonlar))
print(sonlar)
print(juft_sonlar)

# filter() yordamida matnlarni saralaymiz
mevalar = ['olma','anor','anjir',"o'rik",'qovun','banan']
mevB = list(filter(lambda meva:meva.startswith('a'),mevalar))
print(mevB)

# Quyidagi dastur mevalar ro'yxatidan nomi 4
# va undan kam harfdan iborat mevalarni saralab oladi
mevalar = ['olma','anor','anjir',"o'rik",'qovun','banan']
mevalar2 = list(filter(lambda meva:len(meva)<=4, mevalar))
print(mevalar2)

# boshlanish va oxirigi harfi bo'yicha so'zlarni topadigan funksiya
mevalar = ['olma','anor','anjir',"o'rik",'qovun','banan']
mevalar2 = list(filter(lambda meva:(meva.startswith('a') and \
                         meva.endswith('r')), mevalar))
print(mevalar2)
     
     
     
     

































