# AMALIYOT

class Avto:
    def __init__(self,model,rang,korobka,narx):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narx = narx
        self.kilometr = 0 # Standart qiymat
        
    def get_avto(self):
        return f"{self.model} {self.rang} {self.korobka}"
    
    def get_info(self):
        return f"{self.rang} {self.model}. {self.korobka.title()} korobka. \
Narxi {self.narx}. {self.kilometr} kilometr yurgan."
            
    def set_km(self,kilometr):
        """Kilometrni o'zgartirish"""
        self.kilometr = kilometr
    
    def update_km(self):
        """Kilometrni yangilab borish"""
        self.kilometr += 1
  
avto1 = Avto('Gentra','Qora','Avtomat',15000,)
avto1.set_km(1)
avto1.update_km() # kilometrni oshiramiz
print(avto1.get_info())



        
        
        
    




         
            
        
        