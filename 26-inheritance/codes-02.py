# OBYEKT ICHIDA OBYEKT

class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}, "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug'ilgan"
        return info
    
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    
# inson = Shaxs("Hasan","Alimov","FB001122",1998)
# print(f"{inson.get_info()}. {inson.get_age(2021)} yoshda.")
     
# VORIS KLASS YARATISH
class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self,ism,familiya,passport,tyil,id,manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism,familiya,passport,tyil)
        self.idraqam = id
        self.bosqich = 1
        self.manzil = manzil
        
# VORIS KLASSGA XOS XUSUSIYATLAR VA METODLAR   
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
# POLIMORFIZM -
# SUPER KLASS METODLARINI QAYTA YOZISH
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID:{self.idraqam}"
        return info
    
class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self,uy,kocha,tuman,viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy 
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
    
    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil
    
manzil = Manzil(12,'Olmazor',"Bog'bon","Samarqand")
talaba = Talaba('Valijon','Aliyev','FA112233',2000,"0000012",manzil)
print(talaba.manzil.get_manzil())
print(talaba.manzil.tuman)
    
    
    
