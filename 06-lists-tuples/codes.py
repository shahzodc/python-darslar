# # RO'YXATNI TARTIBLASH

# .sort() metodi
cars = ['bmw', 'volvo', 'gm', 'tesla', 'audi']
cars.sort()
print(cars)

# TESKARI TARTIBLASH
cars = ['bmw', 'volvo', 'gm', 'tesla', 'audi']
cars.sort(reverse=True)
print(cars)

# .sorted() metodi 
mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farrux']
print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
print("Asl ro'yxat o'zarmas qoldi:", mehmonlar)

# TESKARI TARTIBLASH
print(sorted(mehmonlar, reverse=True))
print(sorted(mehmonlar))

# SONLARNI HAM TARTIBLAYMIZ
ages = [12, 98, 34, 65, 34, 76, 11]
ages.sort()
print(ages)
print(sorted(ages, reverse=True))

# RO'YXATNI AYLANTIRISH
fruits = ['pear', 'banana', 'apple', 'watermelon', 'lemon']
fruits.reverse()
print(fruits)

# RO'YXATNI UZUNLIGINI TOPISH
fruits = ['pear', 'banana', 'apple', 'watermelon', 'lemon']
print("Elementlar soni:", len(fruits))

# range() FUNKSIYASI
sonlar = list(range(0,10))
print(sonlar)

juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam bilan
toq_sonlar = list(range(1,20,2)) # 1 dan 20 gacha 2 qadam bilan
print("Juft sonlar: ", juft_sonlar)
print("Toq sonlar: ", toq_sonlar)

# SONLI RO'YXAT USTIDA SODDA AMALLAR
narxlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
arzon = min(narxlar)
qimmat = max(narxlar)
jami = sum(narxlar)
print("Eng arzon narx", arzon,\
      ". Eng qimmati", qimmat,\
          ". Jami:", jami)
     
# RO'YXATNI KESISH
cars = ['bmw', 'volvo', 'gm', 'toyota', 'tesla', 'audi']
my_cars = cars[0:3] # 0 dan boshlab 3 ta element ajratib olamiz 
print(my_cars)

print(cars[2:5]) # 2-4-5-elementlarni ajratib olish
print(cars[2:]) # 2-elementdan ro'yxat oxirigacha kesish

# RO'YXATDAN NUSXA OLISH
sonlar = [1, 2, 3, 4, 5] # sonlar degan ro'yxat yaratamiz
sonlar2 = sonlar[:] # sonlar2 degan ro'yxatni sonlarga tenglaymiz
sonlar2.append(6)
sonlar2.append(7)
print("Bu sonlar ro'yxati:", sonlar)
print("Bu sonlar2 ro'yxati:", sonlar2)

# TULPES - O'ZGARMAS RO'YXATLAR
# O'ZGARMAS RO'YXATLARDA [] O'RNIGA () ISHLATILADI
tomonlar = (20, 30, 55.2)
print(tomonlar)

toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
print(toys[0])
print(toys[-1])
print(toys[2:5])

# O'ZGARMAS RO'YXAT YARATAMIZ
toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga aylantiramiz
toys.append('dragon')
toys.remove('bus')
toys[1] = "mcquen"
toys = tuple(toys) # o'zgarmas ro'yxatga (Tuple) ga aylantiramiz
print(toys)




































 




















