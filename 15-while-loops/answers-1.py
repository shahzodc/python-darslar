#1
kitob = "Yoqtirgan kitobizni kiriting "
kitob += "(to'xtatish uchun 'stop' deb yozing): "
qiymat = ''
while qiymat != 'stop': # toki qiymat stopga teng emas ekan
    qiymat = input(kitob)
    if qiymat != 'stop':
        print(qiymat)
            
#2
savol = 'Yoshingizni kiriting: '
while True:
    qiymat = input(savol)
    if  qiymat == 'exit' or qiymat == 'quit':
        break
    yosh = int(qiymat)
    if yosh<7:
        narx = 2000
    elif yosh<=18:
        narx = 3000
    elif yosh<=65:
        narx = 10000
    elif narx>65:
        narx = 0
    if narx==0:
        print('Sizga kirish bepul')
    else:
        print(f"Chipta {narx} so'm")  

#3
savol = "Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting \n"
savol += "Dasturni to'xtatish uchun 'exit' deb yozing: "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif qiymat =='Exit':
        continue # agar foydalanuvchi manfiy son kiritsa siklni takrorlaymiz
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz}, ga teng")
        

            
        
        
        
        
    
        
        
        
        
        
        


    
        
    
        

    
    