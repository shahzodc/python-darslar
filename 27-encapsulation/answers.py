# AMALIYOT
#1 
from uuid import uuid4

class Shaxs:
    __num_shaxs = 0
    def __init__(self,ism,familiya,passport,tyil,yosh=0):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.__yosh = yosh
        self.__id = uuid4()
        Shaxs.__num_shaxs += 1
    
    @classmethod 
    def get_num_shaxs(cls):
        return cls.__num_shaxs
        
    def get_info(self):
        info = f"{self.ism} {self.familiya}."
        info += f"\nPassport:{self.passport}. \n{self.tyil}-yilda tug'ilgan."
        info += f"\nYoshi {self.__yosh} \nID:{self.__id}"
        return info
    
    def add_yosh(self,yosh): # yosh qo'shadigan funksiya
        if yosh>=0:
            self.__yosh += yosh
        else:
            return "Yoshni kamaytirib bo'lmaydi"
    
    def get_id(self):
        return self.__id
    
shaxs1 = Shaxs("Shahzod","Rahimberdiyev","AA8545725",1998)
shaxs1.add_yosh(22)
print(shaxs1.get_info())
print(Shaxs.get_num_shaxs())

#2
class Talaba:
    __num_talaba = 0
    def __init__(self,ism,familiya,tyil,kurs=0):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.__kurs = kurs
        Talaba.__num_talaba += 1
        
    @classmethod 
    def get_num_talaba(cls):
        return cls.__num_talaba
          
    def tanishtir(self):
        print(f"\nIsmim: {self.ism} {self.familiya}"
               f"\n{self.tyil} yilda tug'ilganman"
               f"\n{self.__kurs}-kurs talabasiman")
        
    def add_kurs(self,kurs):
        if kurs>=0:
            self.__kurs += kurs
        else: 
            return "Kursni kamaytirib bo'lmaydi"
            
talaba1 = Talaba("Anvar","Valiyev",1998)
talaba1.add_kurs(3)
print(talaba1.tanishtir())
print(Talaba.get_num_talaba())


            
    
            
            
            
    

    

        
    
        