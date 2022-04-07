car = {'model':'ferrari','rang':'qizil'}
print(car)
print(car['model']) # kalit so'z orqali murojaat etamiz
print(car['rang']) # kalit so'z orqali murojaat etamiz

talaba = {'ism':'murod_olimov','yosh':20, 't_yil':2000}
print(f"{talaba['ism'].title()},\
  {talaba['t_yil']}-yilda tug'ilgan,\
  {talaba['yosh']} yoshda")
 
 
car = {
        'make':'GM',
        'model':'Malibu',
        'color':'Black',
        'gear':'Automatic',
        'year':2020,
        'price':40000
        }
# print(car)


# get() METODI  KeyError xatoligini oldini oladi
narx = car.get('narx', 'Bunday kalit mavjud emas')
print(narx)
narx = car.get('narx') # None qaytaradi
print(narx)


# YANGI JUFTLIK QO'SHISH
talaba={}
talaba['kurs']='4'
talaba['fakultet']='informatika'
print(talaba)


# BO'SH LUG'AT
car={}
car['model']='Mazda 6'
car['color']='Red'
car['price']=40000
car['price']=38000 # qiymatni o'zgartirish
print(f"{car['color']} {car['model']}, {car['price']}$")


# KALIT SO'Z-QIYMAT JUFTLIGINI O'CHIRISH
car = {'model':'Malibu','color':'Black','price':40000}
print(car)
del car['color'] # kalit so'zni o'chiramiz
print(car)








































          
          
          

