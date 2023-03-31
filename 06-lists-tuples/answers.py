# # AMALIYOT
#1
countries = ['Uzbekistan', 'Russia', 'Japan', 'Poland']
print("Elementlar soni:", len(countries))

#2
print(sorted(countries))  # aflibo ketma-ketligida lekin tarkibi o'zgarmaydi
print(sorted(countries, reverse=True)) # teskari ketma-ketlikda
print(countries) 

#3
countries.sort() # alifbo ketma-ketligida
print(countries)
countries.sort(reverse=True) # teskari ketma-ketlikga
print(countries)

#4 
sonlar = list(range(120,1200,2)) # sonlar ro'yxatini tuzamiz  
print(sonlar) 
jami = sum(sonlar) # sonlar yig'insini hisoblaymiz
print(jami)
print(max(sonlar)-min(sonlar)) # katta va kichik sonlar o'rtasidagi ayirmani hisoblaymiz
print(len(sonlar)) # elementlar sonini hisoblaymiz

#5
print(sonlar[:20]) # boshidan
print(sonlar[260:280]) # o'rtasidan
print(sonlar[520:540]) # oxiridan 

#6
taomlar = ['osh', 'lavash', 'mastava', 'manti']
nonushta = taomlar[:] # nusxa olamiz
nonushta.remove("osh") # o'chiramiz
nonushta.remove("lavash") # o'chiramiz
nonushta.append("tuxum") # qo'shamiz
nonushta.append("kolbasa") # qo'shamiz
# print("Taomlar", taomlar)
# print("Nonushta", nonushta)

#7
nonushta = tuple(nonushta) # o'zgarmas ro'yxatga aylantirdik
# nonushta[0] = "qaymoq va non" # o'zgartirib bo'lmaydi
nonushta = list(nonushta) # oddiy ro'yxatga aylantirdik
nonushta[1] = "qaymoq va non" # element qo'shdik
nonushta = tuple(nonushta) # o'zgarmas ro'yxatga aylantirdik
print(nonushta)
