# PYTHONDAN JSONGA

# json.dumps()
import json
x = 10
x_json = json.dumps(x)
ism = 'anvar'
ism_json = json.dumps(ism)

# KO'P HOLATLARDA JSON MA'LUMOTLARI 
# LUG'AT KO'RINISHIDA UZATILADI
bemor = {
    'ism':'Alijon Valiyev',
    'yosh': 30,
    'oila': True,
    'farzandlar': ('Ahmad','Bonu'),
    'allergiya': None,
    'dorilar': [
        {'nomi': 'Analgin', 'miqdori': 0.5},
        {'nomi': 'Panadol', 'miqdori':1.2}
        ]
    }
bemor_json = json.dumps(bemor, indent=4)

print(bemor)
print(bemor_json)

# json.dump()
# MA'LUMOTLARNI JSON FORMATIGA O'TKAZISH 
# VA FAYLGA YOZISH
bemor = {
    'ism':'Alijon Valiyev',
    'yosh': 30,
    'oila': True,
    'farzandlar': ('Ahmad','Bonu'),
    'allergiya': None,
    'dorilar': [
        {'nomi': 'Analgin', 'miqdori': 0.5},
        {'nomi': 'Panadol', 'miqdori':1.2}
        ]
    }

import json
with open('bemor.json','w') as f:
    json.dump(bemor,f, indent=4)

# JSONDAN PYTHONGA 
# json.loads()

import json
sonlar = [12,45,23,67]
sonlar_json = json.dumps(sonlar)
sonlar = json.loads(sonlar_json)
bemor = json.loads(bemor_json)
print(sonlar)
print(bemor)

# json.load()
filename = 'bemor.json'
with open(filename) as f:
    bemor = json.load(f)

print(type(bemor))








    









