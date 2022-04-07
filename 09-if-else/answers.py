#1
cars = ['toyota','mazda','hyundai','gm','kia']
for car in cars:
    if car == 'gm':
        print(car.upper())
    else:
        print(car.title())

#2
cars = ['toyota','mazda','hyundai','gm','kia']
for car in cars:
    if car != 'gm':
        print(car.title())
    else:
        print(car.upper())

#3
login = input("Login kiriting: ")
if login == "Shahzod":
    print("Xush kelibsiz Admin")
else:
    print("Xush kelibsiz", login)

#4
son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))
if son1==son2:
    print("Sonlar teng")
else:
    print("Sonlar teng emas")

#5
son = int(input("Istalgan son kiriting: "))
if son>0:
    print(son, "musbat son")
else:
    print("manfiy son")

#6
son = int(input("Son kiriting: "))
if son<0:
    print(son, "bu manfiy son musbat son kiriting")
else:
    print(son, "sonining ildizi", son**2)

#7
son = int(input("Son kiriting: "))
if son%2==0:
    print(son, 'juft son')
else:
    print(son, 'toq son')
    
    
    
    
    
    
