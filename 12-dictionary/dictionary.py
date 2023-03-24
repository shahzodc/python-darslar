# LUG'ATLAR BILAN ISHLASH

# .items() METODI kalit qiymatlarni chiqaradi
#1
talaba = {
    'ism':'alijon',
    'familiya':'shamshiyev',
    'yosh':22,
    'fakultet':'matematika',
    'kurs':4
    }
print(talaba.items())
# tushunarli ko'rinishda chiqaramiz
for kalit, qiymat in talaba.items(): 
    print(f"Kalit: {kalit}")
    print(f"Qiymat: {qiymat}")

#2
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }
for k, q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q}")

#3 .keys() METODI faqat kalitlarni chiqaradi
mahsulotlar = {
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000,
    }
print(mahsulotlar.keys())
print('\nDo\'kondagi mahsulotlar: ')
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())

#4 RO'YXAT VA LUG'AT
mahsulotlar = {
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000,
    }
bozorlik =['anor','uzum','non','baliq']
for m in mahsulotlar:
    if m in bozorlik:
        print(f"{m.title()} {mahsulotlar[m]} so'm")
        
for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"Kechirasiz, bizda {buyum} yo'q")
         
# LUG'AT ELEMENTLARINI TARTIB BILAN CHIQARISH
# .sorted()
mahsulotlar = {
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000,
    }
print("\nDo'konimizdagi mahsulotlar:")
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())
    
# .values() METODI faqat qiymatlarni chiqaradi
telefonlar = {
    'ali':'iphone',
    'vali':'galaxy s9',
    'olim':'mi 10',
    'orif':'nokia 3310',
    'umar':'iphone'
    }
print(telefonlar.values())

print('\nFoydalanuvchilarning telefonlari:')
for tel in telefonlar.values():
    print(tel)
     
# set() funksiyasidan foydalanamiz
print("\nFoydalanuvchilarning telefonlari:")
for tel in set(telefonlar.values()): 
    print(tel)
