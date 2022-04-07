# DUNDER METHODS

class Avto:
    __num_avto = 0 
    """Avtombil klassi"""
    def __init__(self,make,model,rang,yil,narx):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
        Avto.__num_avto += 1
        
    def __repr__(self):
        """Obyekt haqida ma'lumot"""
        return f"Avto: {self.rang} {self.make} {self.model}"
    
# OBYEKTLARNI TAQQOSLASH
    def __eq__(self,boshqa_avto):
        """Tenglik"""
        return self.narx == boshqa_avto.narx

    def __lt__(self,boshqa_avto):
        """Kichik"""
        return self.narx < boshqa_avto.narx
    
    def __le__(self,boshqa_avto):
        """Kichik yoki teng"""
        return self.narx <= boshqa_avto.narx
        
# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# avto2 = Avto("GM","Gentra","Oq",2020,40000)  
# print(avto1)
# print(avto1==avto2)


# OBYEKTNING UZUNLIGI
class AvtoSalon:
    """Avtosalon klassi"""
    def __init__(self,name):
        self.name = name
        self.avtolar = []
        
    def __repr__(self):
        return f"{self.name} avtosaloni"
    
    def add_avto(self,avto):
        if isinstance(avto,Avto):
            self.avtolar.append(avto)
        else:
            print("Avto obyektini kiriting")
            
    def __len__(self):
        return len(self.avtolar)
    
                      
salon1 = AvtoSalon("\nMaxAvto")

avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Gentra","Oq",2020,40000)

# Yuqoridagi obyektlarni salon1 ga qo'shamiz
for avto in [avto1,avto2]:
    salon1.add_avto(avto)

print(salon1)
print(len(salon1))






    
    
    
    
































