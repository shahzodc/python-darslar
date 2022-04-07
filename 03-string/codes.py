# STRING-MATN

viloyat = "Farg'ona"
avto = 'Nexia 3'
print(viloyat, avto)

# Uncide jadvalidagi emoji-smayliklardan foydalanamiz
matn = "Men yangi 📱 oldim"
print(matn)

# Matnlarni qo'shish
ism = 'Ahad'
print("Mening ismim" + ism)

ism = 'Ahad'
familiya = 'Qayum'
print(ism + familiya) # bir-biriga qo'shib yozildi

ism = 'Ahad'
familiya = 'Qayum'
print(ism + ' ' + familiya) # orasi ajratib yozildi

# f-string # matn ko'rinishidagi o'zgaruvchilarni birlashtirish
ism = "Ahad"
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif)

# uzun matnlarni yasash
fname = "James"
lname = 'Bond'
matn = f"Salom, mening ismim {lname}. {fname} {lname}!"
print(matn)

# f-string ichida ifodalarni ham jamlab yozishimiz mumkin
tyil = 2002
print(f"Siz {tyil}-yilda tug'ilgansiz.")
print(f"Yoshingiz {2021-tyil} da")

# Maxsus belgilar
# \t matnga bo'shliq qo'shish
# \n yangi qatordan boshlash
print('Hello World')
print('Hello \tWorld') # \t bo'sh joy qo'shish
print("Hello \nWorld") # \n qator tashlash

# Metodlar bilan ishlash
# upper() metodi matndagi har bir harfni bosh harfga aylantiradi
ism = 'anvar'
familiya = 'narzullayev'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.upper())

# lower() metodi har bir harfni kichik harfga o'zgartiradi
ism = 'Anvar'
familiya = 'Narzullayev'
ism_sharif = f'{ism} {familiya}'
print(ism_sharif.lower())

# title() metodi matndagi har bir so'zning birinchi harfini katta bilan yozadi
ism_sharif = 'james bond'
print(ism_sharif.title())

# capitalize() metodi matndagi birinchi so'zning birinchi harfini katta bilan yozadi
ism_sharif = 'james bod'
print(ism_sharif.capitalize())

# lstrip() matn boshidagi bo'shliqni
# rstrip() matn oxiridagi bo'shliqni
# strip() matn boshi va oxiridagi bo'shliqlarni olib tashlaydi

meva = "   olmani   "
print("Men " + meva.lstrip() + " yaxshi ko'raman") # matn boshidagi boshliqni 
print("Men " + meva.rstrip() + " yaxshi ko'raman") # matn oxiridagi bo'shliqni
print("Men " + meva.strip() + " yaxsh ko'raman") # matn boshi va oxiridagi bo'shliqni olib tashlaydi

















































