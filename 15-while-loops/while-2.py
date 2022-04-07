# while YORDAMIDA RO'YXATNI TO'LDIRISH
ismlar = []
print("Yaqin do'stingiz ro'yxatini tuzamiz.")
n=1 # ismlarni sanash uchun o'zgaruvchi
while True:
    savol = f"{n}-do'stingiz ismini kiriting: "
    ism = input(savol)
    ismlar.append(ism)
    javob = input("Yana ism qo'shasizmi? (ha/yo'q) ")
    if javob =='ha':
        n+=1
        continue
    else:
        break
print("Do'stlaringiz ro'yxati:")
for ism in ismlar:
    print(ism.title())
    
# while YORDAMIDA LUG'ATNI TO'LDIRISH
print("Do'stlaringiz yoshini saqlaymiz.")
dostlar = {}
ishora = True
while ishora:
    ism = input("Do'stlaringiz ismini kiriting: ")
    yosh = input(f"{ism.title()}ning yoshini kiriting: ")
    dostlar[ism] = int(yosh) # ism kalit, yosh qiymat
    
    javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q) ")
    if javob =="yo'q":
        ishora = False
        
for ism, yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda")
        
# RO'YXAT ELEMENTLARINI O'CHIRISH 
cars = ['lacetti','nexia','toyota','nexia','malibu','nexia']
car = 'nexia'
while car in cars:
    cars.remove(car)
print(cars)

# RO'YXATDAN RO'YXATGA ELEMENT KO'CHIRISH
talabalar = ['hasan', 'husan', 'olim', 'botir']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar[talaba] = int(baho)
    
    
    







        
    



    

