from pywebio.input import input
from pywebio.output import put_text, popup
import random 

# 1-QISM
def sontop(x=10):
    tasodifiy_son = random.randint(1,x)
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(f"SON TOPISH O'YINI "
                           f"(Men 1 dan {x} gacha son o'yladim. Topa olasizmi?)"))
        if taxmin<tasodifiy_son:
            put_text(f"{taxmin} soni xato. Men o'ylagan son bundan kattaroq. Yana harakat qiling:")
        elif taxmin>tasodifiy_son:
            put_text(f"{taxmin} soni xato. Men o'ylagan son bundan kichikroq. Yana harakat qiling:")
        else:
            put_text(f"Topdingiz. Men o'ylagan son {taxmin} edi.")
            break
    popup(f"Tabriklaymiz. Men {taxmin} sonini o'ylagan edim. {taxminlar} ta taxmin bilan topdingiz!")
    return taxminlar

# 2-QISM
def sontop_pc(x=10):
    input(f"Endi siz 1 dan {x} gacha son o'ylang va Enter tugmasini bosing. Men topaman!")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t), "
                      f"men o'ylagan son bundan katta (+), yoki kichikroq (-): ")
 
        if javob =="-":
            put_text(f"{taxmin} soni xato")
            yuqori = taxmin - 1
        elif javob == "+":
            put_text(f"{taxmin} soni xato")
            quyi = taxmin + 1
        else: 
            put_text(f"Topdingiz. Men o'ylagan son {taxmin} edi.")
            break
    popup(f"Topdim. Siz {taxmin} sonini o'ylagan ekansiz. Men {taxminlar} ta taxmin bilan topdim")
    return taxminlar
         
# 3-QISM  
def play(x=10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)
        
        if taxminlar_user>taxminlar_pc:
            popup("Men yutdim")
        elif taxminlar_user<taxminlar_pc:
            popup("Siz yutdingiz")
        else:
            popup("Durrang")
        yana = int(input("Yana o'ynaysizmi? Ha(1)/Yo'q(0): "))
        
        
