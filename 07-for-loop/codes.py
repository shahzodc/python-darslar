#1 for SIKLI
mehmonlar = ['ALI', 'Vali', 'Hasan', 'Husan', 'Olim']
for mehmon in mehmonlar: # sikl sharti
    print(mehmon) # sikl badani
    
#2 for SIKLI QANDAY ISHLAYDI
mehmonlar = ['Ali','Vali','Hasan','Husan','Olim']
for mehmon in mehmonlar: # sikl badani
    print(f"\nHurmatli {mehmon}") # sikl badani
    print("Sizni 20-mart kuni nahorgi oshga taklif qilamiz.")
    print("Hurmat bilan, Xudoyberdiyevlar oilasi")
    
cars = ['nexia','tico','damas']
for car in cars: # sikl sharti
    print(car.title()) # sikl badani 
print("Ko'rganlar qilar havas") # sikldan keyingi kod

#3 for YORDAMIDA SONLI RO'YXATLAR BILAN ISHLASH
sonlar = list(range(1,11))
for son in sonlar: # sikl sharti
    print(f"{son} ning kvadrati {son**2} ga teng") # sikl badani

sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
sonlar_kvadrati = [] # bo'sh ro'yxat
for son in sonlar: # sikl sharti
    sonlar_kvadrati.append(son**2) # sikl badani
print(sonlar)
print(sonlar_kvadrati)

#4 for va input()
dostlar = [] # bo'sh ro'yxat
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5): # sikl sharti
    dostlar.append(input(f"{n+1}-ismni kiriting: ")) # sikl badani
    print(dostlar)





    
    
    
    
    
    
    















 




    
    
 
    
    