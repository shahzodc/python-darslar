# INKAPSULYATSIYA

from uuid import uuid4

class Avto:
    def __init__(self,make,model,rang,yil,narx,km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
        self.__km = km
        self.__id = uuid4()
        
    def get_km(self):
        return self.__km
    def get_id(self):
        return self.__id
    
    def add_km(self,km):
        if km>=0:
            self.__km += km
        else:
            return "Mashinaning km kamaytirib bo'lmaydi"
        
avto1=Avto("GM","Malibu","Qora",2020,40000,10000)
print(f"ID: {avto1.get_id()}")
avto1.add_km(2500)
print(avto1.get_km()) 




    