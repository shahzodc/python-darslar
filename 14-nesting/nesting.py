# LUG'ATLAR RO'YXATI

car0 = {
        'model':'lacetti', 'rang':'oq',
        'yil':2018, 'narx':13000,
        'km':50000, 'korobka':'avtomat'
        }
car1 = {
        'model':'nexia 3', 'rang':'qora',
        'yil':2015, 'narx':9000,
        'km':89000, 'korobka':'mexanika'
        }
car2 = {
        'model':'gentra', 'rang':'qizil',
        'yil':2019, 'narx':15000,
        'km':20000, 'korobka':'mexanika'
        }

car = car0

# hammasini bitta ro'yxatga jamlab osonroq usulda chiqaramiz
cars = [car0, car1, car2] # lug'atlar ro'yxati
for car in cars:
    print(f"{car['model'].title()}, "
          f"{car['rang']} rang, "
          f"{car['yil']} yil, "
          f"{car['narx']}$")
    
print(f"\n{cars[0]}") # indeks orqali murojaat etamiz

# BIROR ELEMENTGA MUROJAAT ETISH 
print(f"\n{cars[0]['model']}")
print(f"\n{cars[2]['rang'].title()} "
      f"{cars[2]['model']}")

# for SIKLI YORDAMIDA BO'SH LUG'ATLAR YARATIB OLISHIMIZ HAM MUMKIN
malibus = [] # bo'sh ro'yxat yaratdik
for n in range(10):
    new_car = { # har bir avto uchun lug'at yaratamiz
        'model':'malibu',
        'rang':None, # noaniq rang
        'yil':2020,
        'narx':None, # narxi belgilanmagan
        'km':0,
        'korobka':'avto'
        }
    malibus.append(new_car) # lug'atni ro'yxatga qo'shamiz

for malibu in malibus[:3]:
    malibu['rang']='qizil'
for malibu in malibus[3:6]:
    malibu['rang']='qora'
for malibu in malibus[6:]:
    malibu['rang']='qora'
    malibu['korobka']='mexanika'
for malibu in malibus:
    if malibu['korobka']=='avto':
        malibu['narx']=40000
    else:
        malibu['narx']=35000 
for malibu in malibus:
    print(malibu.values())

# LUG'AT ICHIDA RO'YXAT
dasturchilar = {
    'ali':['python', 'c++'],
    'vali':['html', 'css', 'js'],
    'hasan':['php', 'sql'],
    'husan':['python', 'php'],
    'maryam':['c++', 'c#'],    
    }

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()}: ", end='')
    for til in tillar:
        print(f'{til.upper()} ', end='')

# LUG'AT ICHIDA LUG'AT
hamkasblar = {
    'ali':{'familiya':'valiyev',
           'tyil':1995,
           "malumot":"oliy",
           'tillar':['python', 'c++']
           },
    'vali':{'familiya':'aliyev',
            'tyil':2001,
            "malumot":"o'rta maxsus",
            'tillar':['html', 'css', 'js']
            },
    'hasan':{'familiya':'husanaov',
             'tyil':1999,
             "malumot":"maxsus",
             'tillar':['python','php']
             }
    }

for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['tyil']}-yilda tug'ilgan. \n"
          f"Ma'lumoti: {info['malumot']}. \n"
          "Quyidagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())
        
        
        
        
        
        
    


        

        
        
        
        
    
    
    
    

    
    
    
    
    














    
    
    
    
    
    
          
          
          
