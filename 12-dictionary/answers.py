# AMALIYOT
#1
python = {'float':"o'nlik sonlar",
          'integer':'butun son',
          'string':'matn',
          'list':"ro'yxat",
          'dictionary':"lug'at",
          'set':"to'plam",
          'loop':'sikl',
          'variable':"o'zgaruvchilar",
          'function':'funksiya',
          'key':'kalit',
          'value':'qiymat'
          }
print("\nFoydalanuvchilarning telefonlari:\n")
for lugat in set(python.values()):
    print(lugat)
    
#2
countries = {'uzbekistan':'tashkent',
              'russia':'moscow',
              'ukraina':'kiyev',
              'france':'parij',
              'germany':'berlin'
              }
print('Mamlakatlar ro\'yxati:')
for county in countries.keys(): # kalitlarni chiqaramiz
    print(county.title())
    
print("\nPoytaxtlar ro'yxati:")
for country in countries.values(): # qiymatlarni chiqaramiz
    print(country.title())
    
#3
countries = {'uzbekistan':'tashkent',
              'rossiya':'moscow',
              'ukraina':'kiyev',
              'fransiya':'parij',
              'germaniya':'berlin'}
country = input('Qaysi davlatning poytaxtini bilishni istaysiz? ').lower()
capital = countries.get(country)

if capital==None:
    print("Kechirasiz bu haqida ma'lumot yo'q")
else:
    print(f"\n{country.title()}ning poytaxti \
{capital.title()} shahri")

#4
menyu = {'osh':15000,
         'manti':9000,
         'lavash':20000,
         'shovla':18000,
         'mastava':22000,
         'chuchvara':19000,
         'danar':17000,
         'shashlik':23000,
         }
print('Uch xil taom tanlang')
buyurtma = []
for n in range(3):
    buyurtma.append(input(f"{n+1}-taom: ").lower())

for savat in buyurtma:
    if savat in menyu:
        print(f"{savat.title()} {menyu[savat]} so'm")
    else:
        print(f"Kechirasiz, bizda {savat} yo'q.")

    

            
    
    





        


    
    









    
    