# # AMALIYOT
# #1
# buyurtmalar = []
# print("Mahsulotlarni kiriting: ")
# n=1 # mahsulotlarni sanash uchun o'zgaruvchi
# while True:
#     nom = f"{n}-mahsulotni kiriting: "
#     mahsulot = input(nom)
#     buyurtmalar.append(mahsulot)
#     javob = input("Ya'na mahsulot qo'shasizmi< (ha/yo'q) ")
#     if javob =='ha':
#         n+=1
#         continue
#     else:
#         break
# print("\nMahsulotlaringiz ro'yxati:")
# for mahsulot in buyurtmalar:
#     print(mahsulot.capitalize())
    
# #2 
# print("e-bozor uchun mahsulot va ularning \
#       narxini shakllantiruvchi dastur:")
# mahsulotlar = {}
# ishora = True
# while ishora:
#     nom = input("Mahsulotingiz nomini kiriting: ")
#     narx = input(f"{nom.title()}ning narxini kiriitng: ")
#     mahsulotlar[nom] = int(narx) # nom kalit, yosh qiymat
    
#     javob = input("Yana mahsulot qo'shasizmi? (ha/yo'q) ")
#     if javob == "yo'q":
#         ishora = False
        
# for nom, narx in mahsulotlar.items():
#     print(f"{nom.title()} {narx} so'm")
    
#3
buyurtmalar = ['olma', 'anjir', 'uzum', 'qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narx = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narx} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")






        
    
    
      
     
      
    
    
    
    





    
    
