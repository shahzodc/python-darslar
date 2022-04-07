# # AMALIYOT
# #1
# def malumot_ber(ism, familiya, t_yil, yosh, tel=None):
#     malumot = {'ism':ism,
#                'familiya':familiya,
#                't_yil':t_yil,
#                'yosh':yosh,
#                'tel':tel}
#     return malumot

# shaxs1 = malumot_ber('Shahzod','Rahimberdiyev',1998,23)
# shaxs2 = malumot_ber('Shalola',"Yo'ldoshboyeva",1999,22,942163353)
# shaxslar = [shaxs1, shaxs2]
# print("Foydalanuvchilarnining ma'lumotlari:")
# for shaxs in shaxslar:
#     if shaxs['tel']:
#         tel = shaxs['tel']
#     else:
#         tel = "Noma'lum"
#     print(f"Ismi: {shaxs['ism']} \nFamiliyasi: {shaxs['familiya']}"
#     f"\nTug'ilgan yili: {shaxs['t_yil']}"
#     f"\nYoshi: {shaxs['yosh']} da"
#     f"\nTel raqami: {tel}")
    
# #2
# def malumot_ber(ism, familiya, t_yil, yosh, tel=None):
#     malumotlar = {'ism':ism,
#                   'familiya':familiya,
#                   't_yil':t_yil,
#                   'yosh':yosh,
#                   'tel':tel}
#     return malumotlar

# print("Mijozlar haqida ma'lumot")
# mijozlar = [] # mijozlar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting", end='')
#     ism=input("Ism: ")
#     familiya=input('Familiya: ')
#     t_yil=input("Tug'ilgan yil: ")
#     yosh=input("Yosh: ")
#     tel=input("Telefon raqam: ")
    
#     mijozlar.append(malumot_ber(ism, familiya, t_yil, yosh, tel))
    
#     javob = input("Yana malumot qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break
# for mijoz in mijozlar:
#     if mijoz['tel']:
#         tel = mijoz['tel']
#     else:
#         tel = "Noma'lum"
#     print(f"Ismi: {mijoz['ism']} \nFamiliyasi: {mijoz['familiya']}"
#           f"\nTug'ilgan yili: {mijoz['t_yil']}"
#           f"\nYoshi: {mijoz['yosh']} da"
#           f"\nTel raqami: {tel}")

# #3
# def son_kirit(son1,son2,son3):
#         son = son1
#         if son2>=son:
#             son = son2
#         if son3>=son:
#             son = son3
#         return son

# print(son_kirit(19,18,20))

# #4
# def aylana_info(radius, pi=3.14159):
#     aylana = {"radius":radius,
#               "diametr":2*radius,
#               "perimetri":2*radius*pi,
#               "yuza":pi*radius**2}
#     return aylana

# print(aylana_info(4))

# #5
# def tub_sonlar(min,max):
#     tub_sonlar = []
#     for n in range(min,max+1):
#         tub = True 
#         if (n==1):
#             tub = False
#         elif(n==2):
#             tub = True
#         else:
#             for x in range(2,n):
#                 if(n%x==0):
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
            
#     return tub_sonlar

# print(tub_sonlar(3,90))

# #6
# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x==0 or x==1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x-1]+sonlar[x-2])
#     return sonlar

# print(fibonacci(10))










  
    
    
    





