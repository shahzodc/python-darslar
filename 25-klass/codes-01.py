# OBYEKTLAR BILAN ISHLASH

# XUSUSIYATLARGA STANDART QIYMAT BERISH
class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1 # Standart qiymat
        
    def get_info(self):
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi."
    
    # OBYEKTNING XUSUSIYATLARINI YANGILOVCHI METODI
    def set_bosqich(self,bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = bosqich
        
    # XUSUSIYATLARNI YANGILASHNI YANA BIR USULI
    def update_bosqich(self):
        """Talabaning bosqichini 1 taga ko'paytirish"""
        self.bosqich += 1
    
    
# talaba1 = Talaba('Alijon','Valiyev',2000)
# print(talaba1.get_info())

# # STANDART QIYMATNI O'ZGARTIRISH
# talaba1.bosqich = 2
# talaba1.set_bosqich(3)
# print(talaba1.get_info())
# talaba1.update_bosqich()
# print(talaba1.get_info())

# OBYEKTLAR O'RTASIDA MUNOSABAT
class Fan():
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []
        
    def add_student(self,talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni +=1
        
    def get_students(self):
        return [talaba.get_info() for talaba in self.talabalar]
    
matematika = Fan("Oliy Matematika")
talaba1 = Talaba("Alijon","Valiyev",2000)
talaba2 = Talaba("Hasan","Alimov",2001)
talaba3 = Talaba("Akrom","Alimov",2001)
 
matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)
print(matematika.talabalar_soni)

mat_talabalar = matematika.get_students()
print(mat_talabalar)






       
        
        
        




