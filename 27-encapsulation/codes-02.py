# KLASSNING XUSUSIYATLARI VA METODLARI
class Avto:
    num_avto = 0
    def __init__(self,make,model,rang,yil,narx,km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
        self.__km = km
        Avto.num_avto += 1

avto1 = Avto("GM",'Malibu','Qora',2020,40000)
avto2 = Avto("GM","Lacetti",'Oq',2020,20000)
print(avto1.num_avto)
avto3 = Avto("Toyota","Camry","Silver",2018,45000)
print(Avto.num_avto)


# KLASSNING XUSUSIYATLARINI INKAPSULYATSIYA QILISH
class Avto:
    __num_avto = 0 # klassga oid xususiyat
    def __init__(self,make,model,rang,yil,narx,km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
        self.__km = km
        Avto.__num_avto += 1
        

# KLASSGA OID METODLAR
class Avto:
    __num_avto = 0 # klassga oid xususiyat
    def __init__(self,make,model,rang,yil,narx,km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
        self.__km = km
        Avto.__num_avto += 1
        
    @classmethod 
    def get_num_avto(cls):
        return cls.__num_avto
    
avto1 = Avto("GM",'Malibu','Qora',2020,40000)
avto2 = Avto("GM","Lacetti",'Oq',2020,20000)
print(Avto.get_num_avto())




    

     
        
        