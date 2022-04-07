# FAYLLAR BILAN ISHLASH

# FAYLDAN MA'LUMOT O'QISH
with open('pi.txt') as fayl:
    pi = fayl.read()
    # qator oxiridagi bo'shliqlarni olib tashlaymiz
    pi = pi.rstrip() 
    # qator tashlash beligisini almashtiramiz
    pi = pi.replace('\n','')
    # matnni folat (o'nlik) songa o'tkazamiz
    pi = float(pi)
    
print(pi)


# PAPKA ICHIDAGI FAYLLARNI OCHISH
with open('data/talabalar.txt') as fayl:
    talabalar = fayl.read()
    
print(talabalar)


# FAYLLARNI QATORMA-QATOR O'QISH
filename = 'data/talabalar.txt'
with open(filename) as file:
    for line in file:
        print(line)

        
# QATORLARNI RO'YXAT KO'RINISHIDA SAQLAB OLISH UCHUN .readlines() metodidan foydalanamiz
with open(filename) as  file:
    talabalar = file.readlines()
print(talabalar)   
# qator tashlash \n belgisini olib tashlaymiz
talabalar = [talaba.rstrip() for talaba in talabalar]     
print(talabalar)
     
   
# FAYLGA MA'LUMOT YOZISH
# YANGI FAYLGA YOZISH
faylnomi = "new_file.txt"
ism = 'Olim Hasanov'
tyil = 2004
with open(faylnomi,'w') as fayl:
    fayl.write(ism+'\n')
    fayl.write(str(tyil)+"\n")
    
# FAYLGA MA'LUMOT QO'SHISH
with open(faylnomi,'a') as fayl:
    fayl.write('Alijon Valiyev\n')
    fayl.write('2000')


# O'ZGARUVCHILARNI FAYLDA SAQLASH
# PICKLE FAYLGA SAQLASH
import pickle

talaba1 = {'ism':'hasan', 'familiya':'husanov', 'tyil':2003, 'kurs':1}
talaba2 = {'ism':'alijon', 'familiya':'valiyev', 'tyil':2004, 'kurs':1}

with open('info','wb') as file:
    pickle.dump(talaba1,file)
    pickle.dump(talaba2,file)
    
# PICKLE FAYLDAN O'QISH
with open('info','rb') as file:
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)

print(talaba1)
print(talaba2)
    

    
    



        
        
        
        
        
        
        
        
        
        
        
        
        
    

