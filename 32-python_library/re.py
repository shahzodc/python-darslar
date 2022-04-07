import re

word1 = "temir"
word2 = "tomir"
word3 = "tulpor"

andoza = "^t...r"

print(re.match(andoza, word1))
print(re.match(andoza, word2))
print(re.match(andoza, word3))

# e-mail MANZILINI AJRATIB OLAMIZ
matn = "Maqolalar 2020-yilning 20-martiga qadar\
    google@gmail.com elektron pochasida qabul qilinadi"

andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
email = re.findall(andoza,matn)
print(email)

# KUCHLI PAROLNI TEKSHIRISH
andoza = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
msg = "Yangi parol kiriting"
msg += '(kamida: 8 xona, 1 ta lotin bosh va 1 ta kichik, '
msg += "1 ta son va 1 ta maxsus belgi bo'lishi kerak): "

while True:
    password = input(msg)
    if re.match(andoza,password):
        print("Maxfiy so'z qabul qilindi")
        break
    else:
        print("Maxfiy so'z talabga javob bermadi")
        
        
        

                                                     








