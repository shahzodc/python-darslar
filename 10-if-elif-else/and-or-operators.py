# # AND VA OR OPERATORLARI

# OR OPERATORI  
kun = input("Bugun qanday kun? ")
if kun.lower()=='shanba' or kun.lower()=='yakshanba':
    print('Bugun dam olish kuni')
else:
    print('Bugun ish kuni')
    
    
# AND OPERATORI
kun = input("Bugun qanday kun? ")
harorat = float(input('Havo harorati qanday? '))
if kun.lower()=='yakshanba' and harorat>=30:
    print('Cho\'milgani ketdik')
elif kun.lower()=='yakshanba' and harorat<30:
    print('Uyda dam olamiz')
    

# BIR NECHTA SHARTLARNI KETMA-KET YOZISH
yosh = int(input('Yoshingizni kiriting? '))
kun = input('Bugungi kunni kiriting? ')
if (yosh<7 or yosh>65) and kun=='chorshanba':
    print('Bugun siz uchun Muzeyga kirish bepul')


# BOOLEAN MA'LUMOTLAR TURI  
a = True # o'zgaruvchilarda saqlashimiz mumkin
b = False # o'zgaruvchilarda saqlashimiz mumkin

narx = 15000 # mijoz 15000 so'mga taom oldi
choy = True # mijoz choy ham oldi
salat = False # mijoz salat olmadi

if choy and salat: # agar mijoz choy va salat olgan bo'lsa
    narx = narx + 10000 # narxga 10000 so'm qo'shamiz
elif choy or salat: # agar choy yoki salat olgan bo'lsa
    narx = narx + 5000 # narxga 5000 so'm qo'shamiz
print(f"Jami {narx} so'm") # Yakuniy narxni chiqaramiz


# SHARTLARNI KETMA-KET TEKSHIRISH
narx = 15000 # mijoz 15000 so'mga ovqat oldi
choy = True
salat = False
non = True
kompot = True
assorti = False

if choy: # agar choy olsa
    print('Mijoz choy oldi')
    narx = narx + 3000
if salat: # agar salat olsa
    print("Mijoz salat oldi")
    narx = narx + 5000
if non: # agar non olsa
    print('Mijoz non oldi')
    narx = narx + 2000
if kompot: # agar kompot olsa
    print('Mijoz kompot oldi')
    narx = narx + 5000
if assorti: # agar assorti olsa
    print("Mijoz assorti oldi")
    narx = narx + 15000
print(f"Jami {narx} so'm")


# RO'YXAT TARKIBINI TEKSHIRISH
# in OPERATORI
menyu = ['osh','qozonkabob','shashlik','norin','somsa']
ovqat = input('Nima ovqat yeysiz? ')
if ovqat.lower() in menyu:
    print('Buyurtma qabul qilindi')
else:
    print('Afsuski, bizda bunday ovqat yo\'q')


# not in OPERATORI
menyu = ['osh','qozonkabob','shashlik','norin','somsa']
ovqat = input('Nima ovqat yeysiz? ')
if ovqat.lower() not in menyu:
    print('Afsuski, bizda bunday ovqat yo\'q')
else:
    print('Buyurtma qabul qilindi')


# IKKI RO'YXATNI SOLISHTIRISH
menyu = ['osh','qozonkabob','shashlik','norin','somsa']
buyurtmalar = ['osh','somsa','manti','shashlik']
for taom in buyurtmalar:
    if taom in menyu:
        print(f"Menyuda {taom} bor")
    else:
        print(f"Kechirasiz, menyuda {taom} yo'q")


# RO'YXAT BO'SH EMASLIGINI TEKSHIRISH
list1 = [1,2,3]
len(list1)>30 # ro'yxat bo'sh emasligini tekshiramiz
list2 = [] # bo'sh ro'yxat
len(list2)>0  # ro'yxat bo'sh emasligini tekshiramiz


# TEKSHIRISHNING OSON YO'LI
list1 = [1,2,3]
if list1: # Bu ifoda True qaytaradi, sababi list1 bo'sh emas
    print("Ro'yxatda elementlar bor")
    
    
# YANA BIR MISOL KO'RAMIZ
menyu = ['osh','qozonkabob','shashlik','norin','somsa']
buyurtmalar = ['osh','somsa','manti','shashlik']


if buyurtmalar:
    for taom in buyurtmalar:
        if taom in menyu:
            print(f"Menyuda {taom} bor")
        else:
            print(f"Kechirasiz, menyuda {taom} yo'q")
else: # agar ro'yxat bo'sh bo'lsa
    print("Savatchangiz bo'sh")



















    
    
    
    
    
    
    

    
    
    
    
          














    
    









    
    
    
    
    
    
    
    
    
    
    
    