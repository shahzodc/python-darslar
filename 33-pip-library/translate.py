# pip install googletrans==3.1.0a0
from googletrans import Translator
tarjimon = Translator() # Translator - bu maxsus klass (tarjimon esa obyekt)

matn_uz = "Python - dunyodagi enf mashhur dasturlash tili"

tarjima = tarjimon.translate(matn_uz)
print(tarjima.origin) # asl matnni chiqaradi
print(tarjima.text) # tarjima qiladi
print(tarjima.src) # asl matn tilini chiqaradi

# RUS TILIGA TARJIMA QILISH
tarjima_ru = tarjimon.translate(matn_uz, dest='ru')
print(tarjima_ru.text)

# O'ZBEK TILIGA TARJIMA QILISH
matn_en = "Tashkent - is the capital of uzbekistan"
tarjima_uz = tarjimon.translate(matn_en, dest='uz')
print(tarjima_uz.text)

# AGAR MATN TILINI HAM ALOHIDA KO'RSATMOQCHI BO'LSAK
text_uz = "Tashkent - O'zbekistonning poytaxti"
tarjimaa_en = tarjimon.translate(text_uz,src='uz',dest='en')
print(tarjimaa_en.text)







