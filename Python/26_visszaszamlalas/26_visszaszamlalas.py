#visszaszamlalas
#A számok megadásának sorrendjét ne figyelje
"""
#Első megoldás
print("Visszaszámlálás!")
a = int(input("Adj meg egy számot"))
b = int(input("Adj meg egy számot"))


if a > b:
    tol = a
    ig = b
else:
    tol = b
    ig = a
"""

"""
#Második megoldás
print("Visszaszámlálás!")
tol = int(input("Adj meg egy számot"))
ig = int(input("Adj meg egy számot"))
temp = None

if tol < ig:
    temp = tol
    tol = ig
    ig = temp
"""


#Harmadik megoldás
print("Visszaszámlálás!")
tol = int(input("Adj meg egy számot"))
ig = int(input("Adj meg egy számot"))
if tol < ig:
    tol, ig = ig, tol

#Visszaszámlálás
#Első megoldás
print(f"Visszaszámlál {tol}-{ig}")
for i in range(tol, ig-1, -1):          #tol >= i > ig+1 pl. ha tol=56, ig =23 akkor 56 >= i > 24 (vagyis: 23+1)
    if i != ig:
        print(i, end="; ")
    else:
        print(i)


print(f"Visszaszámlál {tol}-{ig}")
a = tol
while a >= ig:
    print(tol, end="; ")
    a -= 1


    

