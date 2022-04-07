# OBYEKT ELEMENTLARIGA MUROJAAT ETISH

class Avto:
    __num_avto = 0 
    """Avtombil klassi"""
    def __init__(self,make,model,rang,yil,narx):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
        Avto.__num_avto += 1
        
    def __repr__(self):
        """Obyekt haqida ma'lumot"""
        return f"Avto: {self.rang} {self.make} {self.model}"
    
    def __eq__(self,boshqa_avto):
        """Tenglik"""
        return self.narx == boshqa_avto.narx

    def __lt__(self,boshqa_avto):
        """Kichik"""
        return self.narx < boshqa_avto.narx
    
    def __le__(self,boshqa_avto):
        """Kichik yoki teng"""
        return self.narx <= boshqa_avto.narx
    
class AvtoSalon:
    """Avtosalon klassi"""
    def __init__(self,name):
        self.name = name
        self.avtolar = []
        
    def __repr__(self):
        return f"{self.name} avtosaloni"
            
    def __len__(self):
        return len(self.avtolar)
    
    def __getitem__(self,index):
        return self.avtolar[index]
    
    def __setitem__(self,index,value):
        if isinstance(value,Avto):
            self.avtolar[index]=value

# OPERATORLARNI QAYTA TALQIN QILISH
    def add_avto(self,*qiymat):
        for avto in qiymat:
            if isinstance(avto,Avto):
                self.avtolar.append(avto)
            else:
                print("Avto obyektini kiriting")
                
    def __add__(self,qiymat):
        if isinstance(qiymat,AvtoSalon):
            yangi_salon=AvtoSalon(f"{self.name} {qiymat.name}")
            yangi_salon.avtolar=self.avtolar + qiymat.avtolar
            return yangi_salon
        elif isinstance(qiymat,Avto):
            self.add_avto(qiymat)
        else:
            print(f"AvtoSalonga {type(qiymat)} qo'shib bo'lmaydi")
    
# PARAMET BILAN CHAQIRISH
    def __call__(self,*param):
        if param: # agar parametr bo'lsa
            for avto in param:
                self.add_avto(avto)
        else: # agar parametr bo'lmasa
            return [avto for avto in self.avtolar]
                              
salon1 = AvtoSalon("MaxAvto")
salon2 = AvtoSalon("Avto Lider")

avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Gentra","Oq",2020,40000)
avto3 = Avto("Mazda","6","Qizil",2015,35000)
avto4 = Avto("Telsa",'K5','Yaxshil',2018,32000)
avto5 = Avto("BMW","X7","Oq",2021,34000)
avto6 = Avto("Honda","Accord","Oq",2017,42000)
salon1.add_avto(avto1, avto2, avto3)
salon2.add_avto(avto4, avto5, avto6)































