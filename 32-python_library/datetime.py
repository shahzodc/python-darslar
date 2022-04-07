import datetime as dt

hozir = dt.datetime.now()
print(hozir)

# sanani ajratib olish
print(hozir.date())
# vaqtni ajratib olish
print(hozir.time())
# soatni ajratib olish
print(hozir.hour)
# minutni ajratib olish
print(hozir.minute)
# sekundni ajratib olish
print(hozir.second)

# bugungi sana
bugun = dt.date.today()
print(f"Bugungi sana: {bugun}")

# qo'lda kiritish talab qilinsa 
ertaga = dt.date(2022,4,5)
print(f"Ertaga sana: {ertaga}")

# vaqt bilan ishlash
hozir = dt.datetime.now()
vaqtHozir = hozir.time()
# qo'lda kiritish talab qilinsa
vaqtKeyin = dt.time(21,00,00)
print(f"Hozir soat: {vaqtHozir}")
print(vaqtKeyin)

# AYIRISH OPERATORIDAN FOYDALANISH
bugun = dt.date.today()
ramazon = dt.date(2022,4,10)
farq = ramazon-bugun
print(f"Ramazonga {farq.days} kun qoldi")

# IKKI VAQT ORALIG'INI SEKUNDLARDA YOKI SOATLARDA KO'RAMIZ
hozir = dt.datetime.now()
futbol = dt.datetime(2022,4,10,23,45,00)
farq = futbol-hozir
sekundlar = farq.seconds
minutlar = int(sekundlar/60)
soatlar = int(minutlar/60)
print(f"Futbol boshlanishiga {sekundlar} sekund qoldi")
print(f"Futbol boshlanishiga {minutlar} minut qoldi")
print(f"Futbol boshlanishiga {soatlar} soat qoldi")

# .srtftime() METODI YORDAMIDA O'ZIMIZGA MOSLAB CHIQARAMIZ
# vaqtni millisekundsiz chiqaramiz
vaqt = hozir.strftime("%H:%M:%S")
print(f"Hozir soat: {vaqt}")
# sanani kun-oy-yil ko'rinishida chiqaramiz
sana = hozir.strftime("%d-%m-%Y")
print(f"Bugun sana: {sana}")
# sanani kun/oy/yil ko'rinishida chiqaramiz
sana_vaqt = hozir.strftime("%d/%m/%Y, %H:%M")
print(sana_vaqt)









  






