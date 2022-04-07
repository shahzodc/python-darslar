# AMALIYOT

class Avtosalon:
    def __init__(self,nomi,manzili,avto):
        self.nomi = nomi
        self.manzili = manzili
        self.avto = avto
           
    def get_info(self):
        """To'liq ma'lumotlar"""
        return f"Salon nomi - {self.nomi}. \
Manzili {self.manzili}. Avto nomi {self.avto}"
    
avto1 = Avtosalon("KIA","SERGILE","K5")
print(avto1.get_info())








        
        
        
    
        
        