# FUNKSIYADAN YAGONA QIYMAY QAYTARISH

def toliq_ism(ism, familiya):
    """To'liq ism qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familiya}"
    return toliq_ism
talaba1 = toliq_ism('shahzod','rahimberdiyev')
talaba2 = toliq_ism('shalola',"yo'ldoshboyeva")

print(f"Darsga kelmagan talabalar: {talaba1.title()} va {talaba2.title()}")

# IXTIYORIY ARGUMENTLAR
def toliq_ism(ism, familiya, otasining_ismi=''):
    """To'liq ism qaytaruvchi funksiya"""
    if otasining_ismi: # otasining ismi mavjud bo'lsa
        toliq_ism = f"{ism} {otasining_ismi} {familiya}" 
    else:
        toliq_ism = f"{ism} {familiya}"
    return toliq_ism.title()

talaba1 = toliq_ism('shahzod','rahimberdiyev')
talaba2 = toliq_ism('hakim','olim','abrorovich')
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

# FUNKSIYADAN LUG'AT QAYTARISH
def avto_info(kompaniya, model, rangi, korobka, yili, narxi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narx':narxi}
    return avto

avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
avto2 = avto_info("GM",'Gentra','Oq','Mexanika',2016,15000)
avtolar = [avto1, avto2]
print('Onlayn bozordagi mavjud avtomashinalar:')
for avto in avtolar:
    if avto['narx']:
        narx = avto['narx']
    else:
        narx = "No'malum"
    print(f"{avto['rang']} {avto['model']}. Narxi: {narx}")

# FUNKSIYADAN RO'YXAT QAYTARAMIZ

def oraliq(min, max):
    sonlar = [] # bo'sh ro'yxat
    while min<max:
        sonlar.append(min)
        min += 1
    return sonlar

print(oraliq(0,10))
print(oraliq(10,21))

# FUNKSIYALARNI SIKLDA ISHLATISH
def avto_info(kompaniya, model, rangi, korobka, yili, narxi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narx':narxi}
    return avto

print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
avtolar = [] # salondagi avtolar uchun bo'sh ro'yxat
while True:
    print("\nQuyidagi ma'lumotlarni kiriting", end='')
    kompaniya=input("Ishlab chiqaruvchi: ")
    model=input("Model: ")
    rangi=input("Rangi: ")
    korobka=input('Korobka: ')
    yili=input("Ishlab chiqarilgan yili: ")
    narxi=input("Narxi: ")
    # Kiritilgan ma'lumotlardan avto_info yordamida 
    # lug'at shakllantirib, ro'yxatga qo'shamiz:
    avtolar.append(avto_info(kompaniya, model, rangi, \
                              korobka, yili, narxi))
        # Yana avto qo'shish-qo'shmaslikni so'raymiz
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob=='no':
        break

print("\nSalominimizdagi avtolar:")
for avto in avtolar:
    if avto ['narx']:
        narx = avto['narx']
    else:
        narx = "No'malum"
    print(f"{avto['rang'].title()} {avto['model'].title()}, {korobka} karobka. Narxi: {narx}")
