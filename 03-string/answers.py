# # AMALIYOT
# kocha = "Bog'bon"
# mahalla = "Sag'bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"
# print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

# print("Quyidagi ma'lumotlarni kiriting!")
kocha = input("Ko'changiz nomi? ")
mahalla = input("Mahallangiz nomi? ")
tuman = input("Tumaningiz nomi? ")
viloyat = input("Viloyatingiz nomi? ")
# print(f"\n{kocha.capitalize()} ko'chasi,\n{mahalla.capitalize()} mahallasi,\
#       \n{tuman.capitalize()} tumani,\n{viloyat.capitalize()} viloyati.")
      
manzil = f"\n{kocha.title()} ko'chasi,\
    \n{mahalla.upper()} mahallasi,\
        \n{tuman.capitalize()} tumani,\
            \n{viloyat.lower()} viloyati"
print(manzil)