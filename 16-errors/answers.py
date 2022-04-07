# AMALIYOT
#1
son = int(input("Juft son kiriting: "))
if son%2!=0:
    print('Bu juft son emas')
else:
    print("Raxmat")
    
#2
yosh = int(input("Yoshingiz nechchida? "))

if yosh<=4 or yosh>=60:
    narx = 0
elif yosh<18:
    narx = 10000
else:
    narx = 20000
print(f"Chipta {narx} so'm")

#3
x = int(input("Birinchi sonni kiriting: "))
y = int(input("Ikkinchi sonni kiriting: "))
if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f"{x}<{y}")
else:
    print(f"{x}>{y}")

#4
mahsulotlar = ['un',"yog'","sovun",'tuxum','piyoz',
            'kartoshka','olma','banan','uzum','qovun']

savat = []   
for n in range(5):
    savat.append(input(f"{n+1}-mahsulotni qo'shing: "))
if savat:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
        else:
            print(f"Do'konimizda {mahsulot} yo'q")
else:
    print("Savatingiz bo'sh")

#5
users = ['alisher1983','aziza','yasina','umar']
login = input("Yangi login tanglang: ")
if login in users:
    print("Login band, yangi login tanlang")
else:
    print("Xush kelibsiz")
          
          
          
        





    
    
    