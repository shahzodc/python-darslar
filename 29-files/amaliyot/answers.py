# AMALIYOT
#1
with open('matn.txt') as fayl:
    matn = fayl.read()
    
print(matn)

#2 
with open('pi_million_digits.txt') as fayl:
    pi = fayl.read()
    
# print(pi)

def solishtir():
    """Solishtiruvchi funksiya"""
    data = '09121998'
    return (data in pi)
    
print(solishtir())

#3
with open('pi.txt') as fayl:
    pi = fayl.read()
    pi = pi.rstrip() # oxiridagi bo'shiqlarni olib tashlaymiz
    pi = pi.replace('\n','') # qator tashlash belgisini almashtiramiz
    pi = float(pi) # matnni float (o'nlik) songa o'tkazamiz
print(pi)

# PICKLE YORDAMIDA YANGI FAYLGA SAQLASH
import pickle

with open('yopiq_fayl','wb') as file:
    pickle.dump(pi,file)
    
# PICKLE FAYLDAN O'QISH
with open('yopiq_fayl','rb') as file:
    pi = pickle.load(file)
    
print(pi)

#4
while True:
    book = input("Yaxshi ko'rgan kitobingizni kiriting (to'xtash uchun Enter bosing): ")
    if not book: break
    with open('book.txt','a') as file:
        file.write(book+'\n')
    













    
    


    

    