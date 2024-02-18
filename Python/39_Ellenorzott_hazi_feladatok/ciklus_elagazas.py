#b

#Írj egy Python eljárást, amely paraméterként kap egy pozitív egész számot és kiír a képernyőre ennyi karaktert úgy, hogy minden harmadik karakter pluszjel (+) legyen a többi viszont mínuszjel (-)! A programodban hívd is meg ezt az alprogramot!

#Első megoldás
szam = int(input("Adj meg egy pozitív egész számot!\n"))

for i in range(1, szam + 1):
    if i % 3 == 0:
        print("+", end="")
    else:
        print("-", end="")

#Második megoldás
a = int(input("Adj meg egy számot: "))
char = ""
for i in range(a):
    if (i+1) % 3 == 0:
        char += "+"
    else:
        char += "-"
print(char)


#Harmadik megoldás
def eljaras(szá):
    for i in range(0, szá):
        if (i+1)%3==0:
            print("-", end=" ")
        else:
            print("+", end=" ")

szá=int(input("adj meg egy számot\n  "))
eljaras(szá)


#Negyedik megoldás
szam = int(input("Adj meg egy pozitív egész számot: "))

if szam > 0:
    char = ''
    for i in range(szam):
        if (i + 1) % 3 == 0:
            char += '+'  
        else:
            char += '-' 
    print(char)
else:
    print("A megadott szám nem használható!")

#Ötödik megoldás
def szamok(mennyiseg):
    for i in range(mennyiseg):
        if (i+1) % 3 == 0:
            print("+", end=" ")
        else:
            print("-", end=" ")

input_mennyiseg = int(input("Kérem, adjon meg egy pozitív egész számot: "))
    
if input_mennyiseg > 0:
    szamok(input_mennyiseg)
else:
    print("A megadott szám nem pozitív!")



#Hatodik megoldás
pozitiv_szam = int(input("Kérem, adjon meg egy pozitív egész számot: "))
if pozitiv_szam > 0:
    karakterlanc = ''.join(['+' if (i + 1) % 3 == 0 else '-' for i in range(pozitiv_szam)])
    print(karakterlanc)
else:
    print("A megadott szám nem pozitív egész.")