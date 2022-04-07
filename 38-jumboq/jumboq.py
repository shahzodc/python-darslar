# 1 dan 100 gacha sonlar ro'yxatidan qolib ketgan sonni topish

import random 
n=100
numbers = list(range(1,n+1))
x = numbers.pop(random.randint(1,n+1))
print(x)

summa = n*(n+1)/2
print(summa - sum(numbers))



















