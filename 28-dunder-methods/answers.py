# AMALIYOT
#1
class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,yosh):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.yosh = yosh
        
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.yosh})"
        return info 
    
    def __repr__(self):
        """Obyekt haqida ma'lumot"""
        return f"Shaxs: {self.ism} {self.familiya} \nPassport {self.passport}\
            \nYoshi {self.yosh}"

shaxs1 = Shaxs("Shahzod","Rahimberdiyev","FD001122",23)
print(shaxs1)


class Talaba:
    """Talaba klassi"""
    def __init__(self,ism,familiya,bosqich):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.bosqich = bosqich
        
    def __repr__(self):
        """Talaba haqida ma'lumot"""
        return f"\n{self.ism} {self.familiya}\n{self.bosqich}-bosqich"
    
    def __lt__(self,boshqa_kurs):
        """Kichik"""
        return self.bosqich < boshqa_kurs.bosqich
    
    def __le__(self,boshqa_kurs):
        """Kichik yoki teng"""
        return self.bosqich <= boshqa_kurs.bosqich
    
    def __eq__(self,boshqa_kurs):
        """Tenglik"""
        return self.bosqich == boshqa_kurs.bosqich        

talaba1 = Talaba("Kozim","Saburov",3)
talaba2 = Talaba("Alijon","Valiyev",3)
print(talaba1==talaba2)



            
            
            
    



    

