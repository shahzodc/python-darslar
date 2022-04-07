# KLASSLAR 

x = 10
print(type(x))
matn = "salom"
print(type(matn))

def salom_ber():
    print("Assalomu alaykum")
print(type(salom_ber))

# METODLAR
matn = "salom"
print(matn.upper())
son  = 20
# print(son.lower()) # matnlar uchun ishlatiladigan metodlarni
# sonlar uchun qo'llab bo'lmaydi

# KLASS YARATAMIZ
class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil  
        
        
# KLASSDAN OBYEKT YARATISH
talaba1  = Talaba("Alijon","Valiyev",2000)

# OBYEKTNING XUSUSIYATLARINI KO'RISH
print(talaba1.ism)
print(talaba1.familiya)
print(talaba1.tyil)

# KLASSDAN BIR NECHTA OBYEKTLAR YARATISH
talaba2 = Talaba('Shahzod','Rahimberdiyev',1998)
talaba3 = Talaba('Olim','Akbarov',2004)
talaba4 = Talaba('Hasan','Akbarov',2002)
print(talaba2.ism)
print(talaba4.familiya) 

# KLASSGA METODLAR QO'SHAMIZ
class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
    
    def tanishtir(self):
        print(f"Ismim {self.ism} {self.familiya}. "
              f"{self.tyil} yilda tug'ilganman")    
        
# KLASSIMIZ ISTALGANCHA METODLARGA EGA BO'LISHI MUMKIN
    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism
    
    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya
    
    def get_fullname(self):
        """Talabaning ism-familiyasini qaytaradi"""
        return f"{self.ism} {self.familiya}"
            
# ARGUMENT QABUL QILUVCHI METODLAR
    def get_age(self,yil):
        """Talabaning yoshini qaytaradi"""
        return yil-self.tyil
    
# OBYEKTNING METODLARIGA MUROJAAT ETAMIZ
talaba5 = Talaba("Hasan",'Akbarov',1999)
talaba5.tanishtir()
print(talaba5.get_name())
print(talaba5.get_lastname())
print(talaba5.get_fullname())
print(talaba5.get_age(2021))

# PASS OPERATORI
class User:
    def __init__(self,name,username,email):
        self.name = name
        self.uname = username
        self.mail = email
        
    def describe():
        pass
    
    def get_email():
        pass
    
    
    










        
        
        
        
        
        
        