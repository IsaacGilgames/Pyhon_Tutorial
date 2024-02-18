#Írj egy Python programot, amely paraméterként kap 2 egész számot (N és M) és kiír a képernyőre a
#csillag (*) karaktereket M darab sorban és N darab oszlopban (tehát NxM darab karaktert egy
#téglalap alakú képernyőrészre)! A programhoz két db egymásba ágyazott ciklust használj!


#Első megoldás
N = int(input("Adja meg az oszlopok számát (N): "))
M = int(input("Adja meg a sorok számát (M): "))

if N > 0 and M > 0:
    for i in range(M):
        for j in range(N):
            print("*", end=" ")
        print()
else:
    print("A megadott számoknak pozitívnak kell lenniük.")

#Második megoldás
def valami(N, M):
    for i in range(M):
        sor = ""
        for j in range(N):
            sor += "*"
        print(sor)

N = int(input("Írd be az oszlopok számát: "))
M = int(input("Írd be a sorok számát: "))
valami(N, M)


#Harmadik megoldás
N = int(input("Adj meg egy számot: ")) # oszlop
M = int(input("Adj meg egy másik számot: ")) # sor


def csillag(N, M: int):
    while M > 0:
        for i in range(0, N):
            print("*", end=" ")
        print()
        M -= 1

csillag(N, M)