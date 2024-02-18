#Írj egy Python eljárást, amely paraméterként kap egy egész számot és kiírja a képernyőre az ennél kisebb értékű elemeit a Fibonacci sornak!

#Első megoldás
a = int(input("Adj meg egy számot: "))
b, c = 0, 1
while b < a:
    print(b)
    b, c = c, b + c


#Második megoldás
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b

szam = int(input("Kérem, adjon meg egy egész számot: "))

if szam >= 0:
    fibonacci(szam)
else:
    print("A megadott szám nem lehet negatív.")


#Harmadik megoldás
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049] #Remélem ennyi is elég...
number = int(input("Adj egy számot!\n"))

for i in range(len(fibonacci)):
    if fibonacci[i] < number:
        print(fibonacci[i], end=", ")

#Negyedik megoldás
def fibonacci():
    n = int(input("Adjon meg egy számot: "))
    fibonacci=0
    fibonacci2=1
    fibonacci3=fibonacci+fibonacci2
    print(fibonacci,fibonacci2,fibonacci3,end=" ")
    while n>fibonacci3:
        fibonacci=fibonacci2
        fibonacci2=fibonacci3
        fibonacci3=fibonacci+fibonacci2
        if fibonacci3<n:
            print(fibonacci3,end=" ")
if fibonacci() != None:
    print(fibonacci())


#Ötödik megoldás
szam = int(input("Adj meg egy pozitív egész számot: "))

if szam > 0:
    a, b = 0, 1

    print("A Fibonacci sorozatban az ennél kisebb elemek: ")

    while a < szam:
        print(a, end=' ')
        a, b = b, a + b

else:
    print("A szám nem lehet negatív!")


#Hatodik megoldás
szam = int(input("Adj meg egy számot: "))
fibo = 0
fiboossz = 1

while szam > fiboossz:
	temp = fiboossz
	fiboossz = fiboossz + fibo
	fibo = temp
	print(fibo)

#Hetedik megoldás
n = int(input("Kérek egy számot!\n"))
szam1 = 0
szam2 = 1
kov_szam = szam2  
lepesek = 1
 
while lepesek <= n:
    if kov_szam < n:
        print(kov_szam, end=" ")
        lepesek += 1
        szam1, szam2 = szam2, kov_szam
        kov_szam = szam1 + szam2
    else:
        break
print()