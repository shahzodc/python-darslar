# AMALIYOT

import json

data = {'Model':'Malibu',
        'Rang':'Qora',
        'Yil':2020,
        'Narxi':40000
        }

# JSONGA O'TKAZISH
data_json = json.dumps(data, indent=4)
print(data_json)

# FAYLGA SAQLAB OLISH
with open('data.json','w') as f:
    json.dump(data,f, indent=4)
    
#2 
talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
talaba = json.loads(talaba_json)
print(f"{talaba['ism']} {talaba['familiya']}")

# JSON FAYLGA SALQASH
with open('talaba.json','w') as f:
    json.dump(talaba,f, indent=4)


    
    
    





    
    
    


