valtozo = 1
#Több szóból álló változó nevek (szokások)
#Cebab Case
#number-of-donuts = 34

#Snake Case
number_of_donuts = 34

#Camel Case
numberOfDonuts = 34

#Pascal Case
NumberOfDonuts = 34

numberofdonuts = 34
numberofdonuts = "harmincnégy"

#lehetséges változó nevek
_valtozo = 1
_val_to_zo = 1
VALTOZO1 = 1
VALTOZO2 = 1

#szintaktikai hiba, változó nevek, amelyek nem használthatóak (szabály)
# 1valtozo = 1 hibás
# fánkokszáma = 1 ékezeteket egyes esetekben nem fogja elfogadni
# fankok szama = 1 szóköz se lehet

#Karakterlánc = String
a = "Python"
b = 'Python'
c = """Python
1
programozási
nyelv!"""
print(a, end='\n\n')
print(b, end='\n\n')
print(c, end='\n\n')


#Karakter
d = 'n'
print("")
print()

print(d, end='\n\n')

#number
#integer = egész számok
e = 203456 #10-es számrendszer
f = 0b1011011 #2-es számrendszer
g = 0o320 #8-as (octal)
h = 0x12b #16-os (hexadecimális)
i = -245 #negatív

print(e, f, g, h, i, sep='\n', end='\n\n')


#float
j = 23.6
k = 10.0

print(j, k, sep='\n', end='\n\n')
print(float(e), int(j), sep='\n', end='\n\n')

n = 0.233e5
print(n, end='\n\n')

#Speciális
o = None

#Bool = logika
p = True 
q = 7 + False #az eredmény szám lesz True = 1, False = 0, ebben az esetben itt nincs szintaktikai hiba, de ebben az esetben ez már integer

print(p, type(q), sep='\n', end='\n\n')











