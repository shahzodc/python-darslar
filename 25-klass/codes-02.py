# NUQTA YOKI METOD ?

class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1
        
    def set_bosqich(self,bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = bosqich
        
    def update_bosqich(self):
        """Talabaning bosqichini 1 taga ko'paytirish"""
        self.bosqich += 1
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
    
    def get_name(self):
        """Talabaning ismini qayataradi"""
        return self.familiya
    
    def get_lastname(self):
        """Talabaning ism-familiyasini qaytaradi"""
        return self.familiya
    
    def get_fullname(self):
        """Talabaning ism-familiyasini qaytaradi"""
        return f"{self.ism} {self.familiya}"

    def get_age(self,yil):
        """Talabaning yoshini qaytaradi"""
        return yil-self.tyil

    
# XUDDI SHU KABI YAKUNIY KLASIMIZNI KO'RINISHI 
class Fan():
    """Fan nomli klass"""
    def __init__(self,nomi):
        self.nomi = nomi 
        self.talabalar_soni = 0
        self.talabalar = []
        
    def add_student(self,talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1
        
    def get_name(self):
        """Fan nomi"""
        return self.nomi
    
    def get_students(self):
        """Fanga yozilgan talabalar haqida ma'lumot"""
        return [x.get_info() for x in self.talabalar]
    
    def get_students_num(self):
        """Fanga yozilgan talabalar soni"""
        return self.talabalar_soni 
    
# METODLARNI QAYTARUVCHI FUNKSIYA YOZAMIZ
def see_methods(klass):
    return [method for method in dir(klass) if \
            method.startswith('__') is False]
        
print(see_methods(Fan))

talaba1 = Talaba("Alijon","Valijon",2000) 
print(talaba1.__dict__) # OBYEKTNING XUSUSIYATLARINI LUG'AT KO'RINISHIDA QAYTARADI
print(talaba1.__dict__.keys()) # KALITLARINI AJRATIB OLSAK OBYEKTNING XUSUSIYATLARI CHIQADI
 




    
    
    
    
    
    
    
        
        