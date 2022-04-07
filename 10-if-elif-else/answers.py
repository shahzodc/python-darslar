# # AMALIYOT

# #1
# son = int(input("Juft son kiriting: "))
# if son%2==0:
#     print(son, 'juft son')
# else:
#     print(son, 'juft son emas')
    
# #2
# yosh = int(input('Yoshingizni kiriting: '))

# if yosh<4 or yosh>60:
#     print('Kirish bepul')
# elif yosh<18:
#     print("Kirish 10000 so'm")
# elif yosh>18:
#     print('Kirish 20000 so\'m')

# #3
# son1 = int(input("Birinchi sonni kiriting: "))
# son2 = int(input("Ikkinchi sonni kiriting: "))

# if son1==son2:
#     print("Sonlar teng")
# elif son1>son2:
#     print(son1, "soni", son2, "sonidan katta")
# elif son1<son2:
#     print(son1, "soni", son2, "sonidan kichkina")

# #4
# mahsulotlar = ['tuz','shakar','non','asal','qaymoq','shokolat']
# savat = [] # bo'sh ro'yxat

# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print("Do'konimizda bu mahsulot yo'q")

# #5
# mahsulotlar = ['tuz','shakar','non','asal','qaymoq','shokolat']
# savat = []

# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulot qo'shing: "))
    
# bor_mahsulotlar = []
# mavjud_emas = []

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)  
        
# if bor_mahsulotlar:
#     print("\nSiz so'ragan barcha mahsulotlar bor")
# if mavjud_emas:
#     print("Do'konimizda quyidagi mahsulotlar yo'q")
#     for mahsulotlar in mavjud_emas:
#         print(mahsulot)

# #6
# users = ['shahzod','shalola','kozim','sitora','doston']
# login = input("Login kiriting: ")
# if login in users:
#     print("Bu login band iltimos yangi login tanlang")
# else:  
#     print("Xush kelibsiz", login)
    
# #7
# son = int(input("Istalgan butun son kiriting: "))          
# for n in range(2,10):
#     if not (son%n):
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")

        
        
    
    
    

    