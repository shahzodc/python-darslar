#1
son = 1
while son<=10: # toki son 5 dan kichik yoki teng ekan
    print(son, end=' ') # sonni konsolga chiqaramiz va 
    son = son+1 # songa 1 ni qo'shamiz
  
  
#2
print('Kiritilgan sonning kvadratini qaytaruvchi dastur.')
savol = "Istalgan son kiriting "
savol += "(to'xtatish uchun 'exit' deb yozing): "
qiymat = ''
while qiymat != 'exit': # toki qiymat exitga teng ekan
    qiymat = input(savol)
    if qiymat != 'exit':
        print(float(qiymat)**2)


#3 ISHORA - FLAG
print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(to'xtatish uchun 'exit' deb yozing): "
ishora = True
while ishora: # toki ishora=True ekan
    qiymat = input(savol)
    if qiymat == 'exit':
        ishora = False
    else:
        print(float(qiymat)**2)


#4 break OPERATORI
print('Kiritilgan sonning kvadratini qaytaruvchi dastur.')
savol = 'Istalgan son kiriting '
savol += "(to'xtatish uchun 'exit' deb yozing: "

while True: # abadiy sikl
    qiymat = input(savol)
    if qiymat == 'exit':
        break # siklni to'xtatish
    else:
        print(float(qiymat)**2)

# break operatori for siklini to'xtatish uchun ham ishlatiladi
sonlar = list(range(1,11))
for son in sonlar:
    if son == 5: # son 5 ga teng bo'lsa, sikl to'xtaydi
        break
    print(f"{son} ning kvadrati {son**2} ga teng")


#3 continue OPERATORI qadam tashlab o'tib ketadi
sonlar = list(range(1,11))
for son in sonlar:
    if son == 5: # son 5 ga teng bo'lsa, sikl boshiga qaytadi
        continue
    print(f"{son} ning kvadrati {son**2} ga teng")


# while sikliga ham misol ko'ramiz
son = 0 
while son<10:
    son += 1
    if son%2!=0: # agar son toq bo'lsa
        continue
    else: # aks holda (juft bo'lsa)
        print(son, end=' ')


# # ABADIY SIKL TUZOG'I
#1
# son = 0 
# while son<10:
#     if son%2!=0:
#         continue
#     else:
#         print(son) # abadiy davom etadi

# #2      
# son = 0
# while son<10:
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)
#     son += 1
    
# #3
# son = 1
# while son>0:
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)
        
        
        
    
   

        
        
        
        




    
    
    
    
    
    
    
    
    
        
        
        
        
        
        



        


    
    