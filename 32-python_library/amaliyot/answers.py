# 1
import datetime as dt

hozir = dt.date.today()
ramazon = dt.date(2022,4,14)
farq = ramazon-hozir
print(f"Ramazonga {farq.days} kun qoldi")

#2
import re
andoza = '^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
msg = 'Telefon raqam kiriting: '

while True:
    number = input(msg)
    if re.match(andoza,number):
        print("Raqam qabul qilindi")
        break
    else:
        print("Telefon raqam xato kiritildi")