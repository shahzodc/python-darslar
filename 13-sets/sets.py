# TO'PLAMLAR 

# set() to'plam
sonlar = {1,2,3}
print(sonlar)
ismlar = {'valijon','alijon','boqijon'}
print(ismlar)


# TO'PLAM BIR XIL ELEMENTLARNI SAQLAMAYDI
sonlar = {1,2,3,3,4,4,5,6}
print(sonlar)

mevalar = ['olma','anjir','olma','uzum','olma','uzum']
mevalar = set(mevalar)
mevalar = list(mevalar) # ro'yxatga o'tkazish
print(mevalar)


# TO'PLAMGA ELEMENT QO'SHISH
mevalar = {'anjir','olma','uzum'}
mevalar.add('banan') # bitta element qo'shamiz
print(mevalar)
mevalar.update(['anor','qovun']) # birdan ortiq element qo'shamiz
print(sorted(mevalar))


# TO'PLAMDAN ELEMENT O'CHIRISH
# .discard() va .remove() metodlari
mevalar = {'anjir','olma','uzum','banan','anor'}
mevalar.discard('anjir') # elementni o'chiramiz
print(mevalar)
mevalar.remove('banan') # elementni o'chiramiz
print(mevalar)

sonlar = {1,2,3,4,5,6}
sonlar.discard(7) # to'plamda 7 yo'q
print(sonlar) # kalit xatoligi deb chiqmaydi
# sonlar.remove(7)  # to'plamda 7 yo'q
# print(sonlar) # kalit xatoligi deb chiqadi


# .pop() METODI TASODIFIY ELEMENTNI SUG'URIB OLADI
sonlar = {1,2,3,4,5,6,7,8}
son = sonlar.pop() 
print(son)


#  TO'PLAMLAR USTIDA AMALLAR
A = {1,2,3,4}
B = {3,4,5,6}
C = A|B # ikki to'plamni birlashtirish
print(C)
D = A.union(B) # ikki to'plamni birlashtirish
print(D)


# & operatori bir xil elementlarni topadi
# .intersection() metodi ham bir xil elementlarni topadi
A = {1,2,3,4}
B = {3,4,5,6}
print(A&B) # bir xil elementlarini topish
print(A.intersection(B)) # bir xil elementlarini topish


# IKKI TO'PLAM ORASIDAGI FARQ
# - operatori
# .difference()
A = {1,2,3,4}
B = {3,4,5,6}
print(A-B) # 1 va 2 A da bor B da yo'q
print(B.difference(A)) # 5 va 6 B da bor A da yo'q


# TO'PLAMLAR ORASIDAGI SIMMETRIK FARQ
# ^ operatori
# .symmetric_defference() metodi
A = {1,2,3,4}
B = {3,4,5,6}
print(A^B)
print(A.symmetric_difference(B))























































