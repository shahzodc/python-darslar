# FUNCTIONS - FUNKSIYALAR

# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum")

# # QIYMAT QABUL QILUVCHI FUNKSIYA
# def salom_ber(ism):
#     """Foydalanuvchiga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}")

# # DOCSTRING
# def salom_ber(ism):
#     """Foydalanuvchi ismini qabul qilib, 
#     unga salom beruvchi funksiya""" # Docstring
#     print(f"Assalomu alaykum, hurmatli {ism.title()}")
    
# print(salom_ber.__doc__) # Docstringni konsolga chiqarish

# # ARGUMENT VA PARAMETR
# # PARAMETRNI BIZ BIRAMIZ
# # ARGUMENTNI FOYDALANUVCHI KIRITADI

# # FUNKSIYAGA BIR NECHA ARGUMENT UZATISH
# def toliq_ism(ism, familiya):
#     """ism va familiyani jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}") 

# def yosh_hisobla(ism, tugilgan_yil):
#     """Foydalanuvchi yoshini hisoblaydigan funksiya"""
#     print(f"{ism.title()} {2022-tugilgan_yil} yoshda")


# # PARAMETR NOMI BILAN UZATISH
# yosh_hisobla(tugilgan_yil=1998, ism='shahzod')

# toliq_ism(familiya='hakimov',ism='shahzod')

# # STANDART QIYMAT
# def yosh_hisobla(tugilgan_yil, joriy_yil=2022):
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

# # FUNKSIYAGA MUROJAAT ETISHDA XATOLIKLAR
# # 1-misol
# def yosh_hisobla(tugilgan_yil, joriy_yil=2022):
#     """Tug'ilgan yildan yoshini hisoblaymiz"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

# tyil = (input("Tug'ilgan yilizni kiriting: ")) # int(input()) bo'lishi kerak
# yosh_hisobla(tyil)

# # 2-misol
# def yosh_hisobla(tugilgan_yil, joriy_yil): # joriy_yil=2022 bo'lishi kerak
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
# yosh_hisobla(1998)

# # 3-misol
# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum")
    
# salom_ber('hasan') # funksiyada parametr berilmagan

# # 4-misol
# def toliq_ism(ism, familiya):
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
    
# toliq_ism('olim hakimov') # ism familiya alohida yozilishi kerak edi


          



    
    





    

 






    
    

    
    

















      


    
 
    
    

    
    
    



    
    


    

    
    
    
    
    