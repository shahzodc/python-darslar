# AMALIYOT    
    
mask = {
    'ism':'elon mask',
    'yosh':44,
    'millati':'ingliz',
    'asarlar':'spacex'
        }
durov = {
    'ism':'pavel durov',
    'yosh':30,
    'millati':'rus',
    'asarlar':'dasturlash asoslari'
        }
tramp = {
    'ism':'donald tramp',
    'yosh':56,
    'millati':'ingliz',
    'asarlar':'boylik sari'
    }
kiyosaki = {
    'ism':'robert kiyosaki',
    'yosh':67,
    'millati':'xitoy',
    'asarlar':'boy ota kambag\'al ota'
    }
shaxslar = [mask, durov, tramp, kiyosaki]
for shaxs in shaxslar:
    print(f"{shaxs['ism'].title()}, "
          f"{shaxs['yosh']} yosh, "
          f"{shaxs['millati']} millati")
    


