#számláló ciklus
i = 0
while i <= 10:
    print(i)
    i+=1

for i in range(11):
    print(i)

#visszaszamlalas
a = 10
while a >= 1:
    print(a)
    a-=1

#addig kér a felhasználótól számot, ameddig nem azt ad meg!
number = 1
while number % 2 != 0: #páros
    number = int(input("Adj meg egy páros számot: "))
print(f"{number} páros szám!")


#nulla kizárása
number = 0
while number % 2 != 0 or number == 0: #páros
    number = int(input("Adj meg egy páros számot: "))
print(f"{number} páros szám!")