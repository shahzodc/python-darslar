# AMALIYOT

#1
son = lambda x : x * 10
print(son(3))

#2
son = lambda x, y : x + y
print(son(12,12)) 

#3
import random as r
sonlar = r.sample(range(1000),10)
kvadratlar = list(map(lambda x:x*x,sonlar))
print(sonlar)
print(kvadratlar)

toq_sonlar = list(filter(lambda son: son%2==1,sonlar))
print(sonlar)
print(toq_sonlar)

















