# # FUNKSIYA VA RO'YXAT

def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism=ismlar.pop()
        baho=input(f"{ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar

# talabalar = ['ali','vali','hasan','husan']
# baholar = bahola(talabalar)
# # print(baholar)

# # RO'YXATGA O'ZGARTIRISH KIRITISH 
# talabalar = ['ali','vali','hasan','husan']
# baholar = bahola(talabalar)
# print(talabalar)

# ASL RO'YXATGA O'ZGARTIRISH KIRITISHNING OLDINI OLISH
talabalar = ['ali','vali','hasan','husan']
baholar = bahola(talabalar[:])
print(talabalar)





