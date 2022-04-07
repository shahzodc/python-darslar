# AMALIYOT
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
        return yil-self.tyil
    
# inson = Shaxs("Hasan","Alimov","FB001122",1998)
# print(f"{inson.get_info()}. {inson.get_age(2021)} yoshda.")
     