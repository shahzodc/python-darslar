# BIR NECHTA SHARTLARNI TEKSHIRISH
#1
son = int(input("Son kiriting: "))
if son>0: # agar son 0 dan katta bo'lsa
    print("Son musbat")
elif son<0: # aks holda, agar son 0 dan kichik bo'lsa
    print("Son manfiy")
else: # aks holda
    print("Son 0 ga teng")
    
#2
yosh = int(input('Yoshingiz nechchida? '))
if yosh<4:
    print('Sizga kirish bepul')
elif yosh<=12:
    print('Sizga kirish 5000 so\'m')
else:
    print('Sizga kirish 10000 so\'m')

#3
# print() funksiyasini ishlatmasdan yozamiz
yosh = int(input('Yoshingiz nechchida: '))
if yosh<=4:
    price = 0
elif yosh<=12:
    price = 5000
elif yosh<65:
    price = 10000
else:
    price = 8000
print(f"Sizga kirish {price} so'm")

#4 if-elif-else zanjirida else qismi majburiy emas
yosh = int(input("Yoshingiz nechchida? "))
if yosh<=4:
    price = 0
elif yosh<=12:
    price = 5000
elif yosh<65:
    price = 100000
elif yosh>=65:
    price = 8000
print(f"Sizga kirish {price} so'm")

    
    
    
    
    


