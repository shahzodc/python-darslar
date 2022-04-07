# # # EXCEPTIONS

# # try-except
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh) # xato qaytargan qator'
#     print(f"Siz {2021-yosh} yilda tug'ilgansiz")
# except: # xato yuz berganda bajariluvchi kod
#     print("Butun son kiritmadingiz")
# print("Dastur tugadi")

# # try-except-else
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
# except:
#     print("Butun son kiritmadingiz")
# else:
#     print(f"Siz {2021-yosh}-yilda tug'ilgansiz")

# # MA'LUM TURDAGI XATOLARNI USHLASH
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
# except ValueError: # ValueError xatoligi
#     print("Butun son kiritmadingiz")
# else:
#     print(f"Siz {2021-yosh}-yilda tug'ilgansiz")
    
# # ZeroDivisionError
# x,y=5,10
# try:
#     y/(x-5)
# except ZeroDivisionError: # 0 ga bo'lish xatoligi
#     print("0 ga bo'lib bo'lmaydi")
    
# # IndexError
# mevalar = ['olma','anor','anjir','uzum']
# try:
#     print(mevalar[5])
# except IndexError:
#     print(f"Ro'yxatda {len(mevalar)} ta mevalar bor xolos")

# # KeyError
# user = {"username":"sariqdev",
#         "status":"admin",
#         "email":'admin@sariq.dev',
#         "phone":"998997700222"}
# key = 'tel'
# try:
#     print(f"Foydalanuvchi: {user[key]}")
# except KeyError:
#     print("Bunday kalit mavjud emas")

# # FileNotFoundError
# fayl = "data.txt" # bunday fayl mavjud emas
# try: # faylni ochishga harakat qilamiz
#     f = open(fayl)
# except FileNotFoundError:
#     print(f"{fayl} fayli mavjud emas.")

# # BIR NECHTA XATOLARNI USHLASH
# n = input("Butun son kiriting: ")
# try:
#     n = int(n)
#     x=20/n
# except ValueError: # agar foydalanuvchi butun son kiritmasa
#     print("Butun son kiritmadingiz")
# except ZeroDivisionError: # agar foydalanuvchi 0 kiritsa
#     print("0 ga bo'lib bo'lmaydi")
# else:
#     print(f"x={x}")   

# # XATOLARNI KO'RSATMAY O'TISH
# user = {"username":"sariqdev",
#         "status":"admin",
#         "email":"admin@sariq.dev",
#         "phone":"99897123456"}

# key="tel"
# try:
#     print(f"Foydalanuvchi: {user[key]}")
# except KeyError:
#     pass

# yosh = int(input("Son kiriting: "))
# if yosh<20:
#     pass
# else:
#     pass

# # XATOLARNING OLDINI OLISH
# # try-except 
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh) # xato qaytargan qator
#     print(f"Siz {2021-yosh}-yilda tug'ilgansiz")
# except: # xato yuz berganda bajariluvchi kod
#     print("Butun son kiritmadingiz")
    
# # if-else-while
# while True:
#     yosh = input("Yoshingizni kiriting: ")
#     if yosh.isdigit():
#         yosh = int(yosh)
#         break
# print(f"Siz {2021-yosh}-yilda tug'ilgansiz")





    
    
    






 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





