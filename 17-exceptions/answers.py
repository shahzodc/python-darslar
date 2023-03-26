# AMALIYOT
# try-except
x = (input("son kiriting: "))
y = (input("yana bir son kiriting: "))
try:
    x = int(x)
    y = int(y) 
    print(x, '/', y, '=', x/y)
except:
    print("Butun son kiritmadingiz")

# while 
while True:
    x = (input("son kiriting: "))
    y = (input("yana bir son kiriting: "))
    if x.isdigit() and y.isdigit():
        x = int(x)
        y = int(y) 
        break
print(x, '/', y, '=', x/y)
