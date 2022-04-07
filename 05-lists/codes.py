# RO'YXATLAR LISTS

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # so'zlardan iborat ro'yxat
narxlar = [12000, 18000, 10900, 22000] # sonlarda iborat ro'yxat
sonlar = ['bir', 'ikki', 3, 4, 5] # aralash ro'yxat
ismlar = [] # bo'sh ro'yxat

# RO'YXAT ELEMENTLARI
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
print("Birinchi meva:", mevalar[0]) # birinchi meva
print("Ikkinchi meva:", mevalar[1]) # ikkinchi meva
print("Oxirgi meva:", mevalar[3]) # oxirgi meva


# MATN KO'RINISHIDAGI ELEMENTLARGA STRING METODLARINI QO'LLASHIMIZ MUMKIN
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
print("Birinchi meva:", mevalar[0].title())
print("Ikkinchi meva:", mevalar[0].upper())


# ELEMENTLAR USTIDA ARIFMETIK AMALLAR BAJARISH
narxlar = [12000, 18000, 10900, 22000]
print(narxlar[2] + narxlar[3])


# LIST OXIRIDAGI ELEMENTGA -1 INDEKSI ORQALI MUROJAAT ETISHIMIZ MUMKIN
sonlar = [10, 12, 345, -23, 445, 61, -45, 56, -34]
print(sonlar[-1]) 


# ELEMENTNI O'ZGARTIRISH
narxlar = [1200, 18000, 10900, 22000]
narxlar[0] = 13000 # 1-qiymatni 13000 ga o'zgartiramiz
narxlar[2] = 11000 # 3-qiymatni 11000 ga o'zgartiramiz
narxlar[3] = narxlar[3]+2000 # 4-qiymatga 2000 qo'shamiz
print(narxlar)


# YANGI ELEMENT QO'SHISH
# .appaend() metodi
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
mevalar.append("tarvuz") # mevalar oxiriga tarvuz qoshamiz
print(mevalar)

cars = [] # bo'sh ro'yxat 
cars.append("Lacetti") # Lacetti  qo'shamiz
cars.append("Nexia 3") # Nexia 3 qo'shamiz
cars.append("Cobalt") # Cobalt qo'shamiz
print(cars)


# .insert() metodi
cars = ['Lacetti', 'Nexia 3', 'Cobalt']
cars.insert(0, 'Cobalt') # 1 ga Cobalt qo'shamiz
cars.insert(1, 'Malibu') # 2 ga Malibu qo'shamiz
cars.insert(2, 'Damas') # 3 ga Damas qo'shamiz
print(cars)


# ELEMENTNI O'CHRISH
# del operatori
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
del mevalar[1] # 2-element (anjir) ni o'chirib tashlaymiz 
print(mevalar)


# .remove() metoti
mevalar = ['olma', 'anjir', 'olma', 'shaftoli', "o'rik", 'anor']
mevalar.remove('olma') # olmani o'chiramiz
print(mevalar)


# ELEMENTNI SUG'URIB OLISH
# .pop() metodi
bozorlik = ["yog", 'un', 'piyoz', 'banan', "go'sht"]
mahsulot = bozorlik.pop(3) # 4-elementni sug'urib olamiz
print("Men " + mahsulot + " sotib oldim")
print("Olinmagan mahsulotlar: ", bozorlik)

# .pop() metodida indeks berilmasa ro'yxatni
# oxiridan sug'urib oladi
numbers = [1, 2, 3, 4, 5]
print(numbers)
numbers.pop()
print(numbers)



















































