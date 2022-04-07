#1
avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
for avto in avtolar: # sikl sharti
    if avto == "bmw": # operator sharti
        print(avto.upper()) # operator badani
    else:  # operator sharti
        print(avto.title()) # operator badani
  
#2
javob = float(input("12*6 nechchiga teng ? "))
if javob!=72:
    print("Javob xato")
else:
    print("Javob tog'ri")

#3
yosh = int(input("Yoshingiz nechchida? "))
if yosh>=18:
    print("Xush kelibsiz")
else:
    print('Kirish mumkin emas')

#4
yil = int(input("Tug'ilgan yilingizni kiriting: "))
if 2021-yil<18:
    print(f"Yoshingiz {2021-yil} da ekan")
    print("Kirish mumkin emas")
else:
    print("Xush kelibsiz")

#5
login = input("Yangi login tanlang: ")
if len(login)<=5: # login uzunligini tekshiramiz
    print("Login 5 harfdan ko'proq bo'lishi shart")
else:
    print("Login qabul qilindi")



    
    
    
    
    
    
    

        
        