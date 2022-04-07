# AMALIYOT
#1
otam = {'ism':'Shuhrat',
        'yil':1974,
        "ma'lumoti":"Oliy"
        }
onam = {'ism':'Xulkar',
        'yil':1976,
        "ma'lumoti":"O'rta"
        }
singlim = {'ism':'Sitora',
            'yil':2002,
            "ma'lumoti":"Oliy"
            }
print(f"{otam},\n{onam}\n{singlim}")


#2
sevimli = {'shalola':'lavash',
            'shahzod':'osh',
            'kozim':'danar',
            'doston':'norin',
            'tohir':'chuchvara',
            }
print(sevimli['shalola'], sevimli['shahzod'], sevimli['doston'])


#3
python = {'integer':'son',
          'float':"o'nlik son",
          'string':'matn',
          'if':'agar',
          'else':'aks holda',
          'lists':"ro'yxat",
          'tuples':"o'zgarmas ro'yxat",
          'dictionary':"lug'at",
          }
print(python)


#4
python = {'integer':'son',
          'float':"o'nlik son",
          'string':'matn',
          'if':'agar',
          'else':'aks holda',
          'lists':"ro'yxat",
          'tuples':"o'zgarmas ro'yxat",
          'dictionary':"lug'at",
          }
soz = input("Biror so'z kiriting: ") 
# agar so'z yo'q bo'lsa bunday so'z mavjud emas deb chiqadi
print(python.get(soz,"Bunday so'z mavjud emas")) 


#5
soz = input("Biror so'z kiriting: ")
if soz in python:
    print("Bunday so'z mavjud")
else: 
    print("Bunday so'z mavjud emas")
    







          













