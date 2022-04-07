# AMALIYOT
#1
ismlar = ['Kozim', 'Shalola', 'Ixtiyor']
print("Salom", ismlar[0], "ishlaring yaxshimi?")
print("Salom", ismlar[1], "ahvollaring yaxshimi?")
print("Salom", ismlar[2], "tuzukmisan?")

#2
sonlar = [2, 3.0, -5, 7, -9]
sonlar[0] = 13 # 1-sonni o'zgartiramiz
sonlar.append(24) # oxiriga son qo'shamiz
sonlar.remove(3.0) # sonni qo'shamiz
print(sonlar)
sonlar[0] = sonlar[0]+3 # 3 ni qo'shamiz
sonlar[2] = sonlar[2]-5 # 5 ni ayiramiz
sonlar[4] = sonlar[4]/2 # 2 ga bo'lamiz
print(sonlar)

#3
t_shaxslar = ['Ibn Sino', 'Islom Karimov', 'Sharof Rashidov']
z_shaxslar = ['Ilon Mask', 'Murad Nazarov', 'Jo Bayden']
t_sh = t_shaxslar.pop(1)
z_sh = z_shaxslar.pop(0)
print("Men tarixiy shaxslardan " + t_sh + " bilan, zamoviy shaxslardan esa " + z_sh + " bilan suhbat qilishni istar edim")

#4
friends = []
friends = ['Kozim', 'Shalola', 'Sitora', 'Ixtiyor', "To'lqin"]
x = friends.remove('Kozim')
friends.insert(0, 'Doston')
friends.insert(2, 'Tohir')
friends.append('Abdulla')
# print(friends)

mehmonlar = []
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(3))
print("Mehmonga kelganlar: ", mehmonlar)
print("Mehmonga kelmaganlar: ", friends)


















