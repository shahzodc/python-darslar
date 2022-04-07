# VORISLIK VA POLIMORFIZM
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
    
inson = Shaxs("Hasan","Alimov","FB001122",1998)
print(f"{inson.get_info()}. {inson.get_age(2021)} yoshda.")
     
# VORIS KLASS YARATISH
class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self,ism,familiya,passport,tyil,id):
        """Talabaning xususiyatlari"""
        super().__init__(ism,familiya,passport,tyil)
        self.idraqam = id
        self.bosqich = 1
        
# VORIS KLASSGA XOS XUSUSIYATLAR VA METODL
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

talaba = Talaba("Valijon","Aliyev","FA112299",2000,"00000012")
print(f"{talaba.get_info()}. ID:{talaba.get_id()}")
print(f"{talaba.get_bosqich()}-bosqich talabasi")
print(talaba.get_info())





    








    